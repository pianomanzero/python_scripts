#!/usr/bin/env python

#
# Script to monitor the state of netlogon(d) on an Isilon system, and alert
# if the process size exceeds a given threshold, and optionally restart
# at a second threshold
#
# Tim Wright, timothy.wright@isilon.com
# Mon Jul  2 15:45:03 GMT 2012
# Version: $Id$

import errno
import getopt
import os
import re
import signal
import sys
import time
import shutil
import platform
import datetime

from isi.app.lib import procs as procs
from isi.app.lib.emailer import Emailer
import isi.misc as misc

# Script debugging
Debug = True

# Restart netlogon(d)?
Restart_enabled = False

# gcore netlogon(d)?
Gcore_enabled = False

# VSZ threshold above which we warn (kB)
# netlogond memory limit on 6.5 is 512MB
# netlogon memory limit on 7.0+ is 1GB
VM_WARN_THRESH_PRE7=(450 * 1024)
VM_WARN_THRESH_POST7=(450 * 1024)
# VM threshold above which we will (optionally) restart netlogon(d)
VM_RESTART_THRESH_PRE7=(480 * 1024)
VM_RESTART_THRESH_POST7=(480 * 1024)
# Where to save out cores
CORE_DIR="/ifs/data/Isilon_Support/cores"

# Who to send the alerts to (Python list of strings)
Recipients = [ 'first.last@xyz.com', 'timothy.wright@isilon.com' ]
# Who does the mail appear to come from (must be permitted to relay)
Sender = 'first.last@xyz.com'


def isys(cmd):
	try:
		(error, output) = procs.get_cmd_output(cmd)
		if not error:
			return map(lambda x: x.rstrip(), output)
#       else:
#           print error, output
	except Exception, e:
		print "ERROR: ", e

def pidof(cmd):
	pidstr = isys("pgrep %s" % cmd)
	if pidstr:
		return pidstr.pop()
	return pidstr

def send_email(subject, body, attachments):
	global Recipients, Sender
	try:
		Emailer.send_email(Recipients, body, from_address=Sender, subject=subject, attachments=attachments)
	except:
		pass	# error handling?

def send_alert(subject="Monitor netlogon(d) alert", body="", attachments=[]):
	# Send the string str to whoever by whatever means
	send_email(subject, body, attachments)
	return

def check_netlogond_mem(pid):
	global Netlogond_name
	netlogond_threads = isys('ps -xo "pid, %%cpu, %%mem, vsz, rss" -p%s' % pid)
	for thread in netlogond_threads:
		(tpid, cpu, mem, vsz, rss) = thread.split()
		if tpid == 'PID':
			continue	# ignore header line
		if Debug:
			print "check_netlogond %s size is %s" % (Netlogond_name, vsz)
		return int(vsz)

def gcore_netlogond(pid):
	global Netlogond_name
	print "Collecting core for %s" % Netlogond_name
	t=datetime.datetime.today()
	isys("gcore -s -c %s/core.%s.%s.%s %s" %
		(CORE_DIR, Netlogond_name, platform.node(), t.strftime("%m%d-%H%M%S"), pid))

def restart_netlogond():
	global Netlogond_name
	print "Restarting %s" % Netlogond_name
	isys("killall -9 %s" % Netlogond_name)
	time.sleep(60);
	return

def main(argv):
	global Debug, Restart_enabled
	global Netlogond_name

	alert_counter = 0
	(node, version) = os.uname()[1:3]
	major_version = version[1]
	if major_version == '6':
		if Debug:
			print "Running on OneFS 6.x"
		VM_WARN_THRESH = VM_WARN_THRESH_PRE7
		VM_RESTART_THRESH = VM_RESTART_THRESH_PRE7
		Netlogond_name = 'netlogond'
	elif major_version == '7':
		if Debug:
			print "Running on OneFS 7.x"
		VM_WARN_THRESH = VM_WARN_THRESH_POST7
		VM_RESTART_THRESH = VM_RESTART_THRESH_POST7
		Netlogond_name = 'netlogon'
	else:
		print "unsupported os version %s" % version
		sys.exit(1)
	if Gcore_enabled:
		isys("mkdir -p %s" % CORE_DIR)
	while True:
		netlogond_pid = pidof(Netlogond_name)
		if not netlogond_pid:
			if Debug:
				print "Unable to find %s process!" % Netlogond_name
			send_alert("%s is apparently not running on node %s, retrying in 30 seconds" % (Netlogond_name, node))
			time.sleep(30);
			continue
		if (Debug):
			print "%s pid = %s" % (Netlogond_name, netlogond_pid)
		cur_vsz = check_netlogond_mem(netlogond_pid)
		if (cur_vsz > VM_WARN_THRESH):
			if alert_counter > 0:
				alert_counter = alert_counter - 1
				if Debug:
					print "over size alert squelched"
			else:
				if Debug:
					print "WARNING: %s process size %d KB > %d KB warning threshold" % (Netlogond_name, cur_vsz, VM_WARN_THRESH)
				send_alert("WARNING: %s vsz %d KB exceeded threshold %d KB on node %s" % (Netlogond_name, cur_vsz, VM_WARN_THRESH, node))
				if Gcore_enabled:
					gcore_netlogond(netlogond_pid)
				alert_counter = 20	# squelch for 10 minutes (20 * 30 seconds)
		if (cur_vsz > VM_RESTART_THRESH):
			if Restart_enabled:
				send_alert("ERROR: %s process size %d KB > %d KB restart threshold on node %s - restarting" % (Netlogond_name, cur_vsz, VM_RESTART_THRESH, node))
				restart_netlogond()
			else:
				if Debug:
					print "Would have restarted %s here" % Netlogond_name
		time.sleep(30);

if __name__ == "__main__":
    main(sys.argv)

