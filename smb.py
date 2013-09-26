#!/usr/bin/env python

# Install Instructions
# cd /ifs/data/Isilon_Support
# nano SMB_CleanShareRegistry.py
# Copy and paste this entire script from start to finish
# type control x
# type y to save

#Running the script: 
# python SMB_CleanShareRegistry.py
#or can be run with verbose
# python SMB_CleanShareRegistry.py -v
#Corrections are made to /ifs/.ifsvar/main_config.gc
#Changes are logged in /ifs/.ifsvar/main_config_changes.log

import optparse
import isi.gconfig as gcfg


def processArgs():
  usage = "usage: %prog [options]"
  parser = optparse.OptionParser(usage=usage)
  parser.add_option('--verbrose','-v', dest='verbrose',action='store_true', default=False)
  (options, args) = parser.parse_args()
  return (options, args)


class GlobalStrings:
  # global strings to key from having stupid typos
  def __init__(self):
	self.REGPATH_SRV_SHARES = "registry.Services.lwio.Parameters.Drivers.srv.shares._multi_sz"
	self.REGPATH_SRV_SHARE_ACLS = "registry.Services.lwio.Parameters.Drivers.srv.shares.security._binary"
	self.REGPATH_ONEFS_SHARES = "registry.Services.lwio.Parameters.Drivers.onefs.shares._key"

  nameKey   = '_name'

g = GlobalStrings()

# 
def expandString(str):
  str = str.replace(" ","%20")
  str = str.replace("-","%2d")
  return str.replace("$","%24") 

                       
def run():
  ShareDict = dict()

  cfg = gcfg.open(gcfg.gcfg_main)
  ctx = cfg.ctx_new()
  allShares = ctx.read(g.REGPATH_SRV_SHARES)

  for share in allShares:
    if options.verbrose==True:
      print "found share ", share[g.nameKey]
  ShareDict[share[g.nameKey]] = "SRV"

  # Now look at the onefs share parts and we must
  # match 1:1 for the data to be okay
  allShares = ctx.read(g.REGPATH_ONEFS_SHARES)

  for share in allShares:
    if share[g.nameKey] not in ShareDict:
      if options.verbrose==True:
        print "deleting ophaned share",expandString(share[g.nameKey])
      ctx.delete(g.REGPATH_ONEFS_SHARES+"."+expandString(share[g.nameKey]))
    else:
      del ShareDict[share[g.nameKey]]

        # Now we have to remove the leftover shares
    for shareName in ShareDict:
      if options.verbrose==True:
        print "removing removing",expandString(shareName)
      ctx.delete(g.REGPATH_SRV_SHARES+"."+expandString(shareName))

    # For next pass a valid share list is needed
    ShareDict = dict()
    allShares = ctx.read(g.REGPATH_SRV_SHARES)

    for share in allShares:
      if options.verbrose==True:
        print "Found complete share ", share[g.nameKey] 
      ShareDict[share[g.nameKey]] = "SRV"

    # check for any abandoned ACLs
    allShares = ctx.read(g.REGPATH_SRV_SHARE_ACLS)

    for share in allShares:
      if share[g.nameKey] not in ShareDict:
        if options.verbrose==True: 
          print "Removing abandoned ACLs for share", share[g.nameKey]
        ctx.delete(g.REGPATH_SRV_SHARE_ACLS+"."+expandString(share[g.nameKey]))

    ctx.commit()  # needed to actually updated the file. 


  #
(options, args) = processArgs() 
#print "opts: ", options
#print "args: ", args
if options.verbrose==True:
        print "making noise"

run()
print "Done! Now 'isi smb shares list' should work"
#Finish 
