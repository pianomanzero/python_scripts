#!/usr/bin/env python3
from __future__ import print_function
from builtins import input
import sys
import os
import subprocess
import re

# func to read nodes_info file and return nested list of contents
def splitThisFile(file):
    workfile = file
    nodes = open(workfile, "r")
    listOfLines = nodes.readlines()
    nodes = []
    for L in range(len(listOfLines)):
        thisline = listOfLines[L] 
        nodes.append(thisline.split())
    # print(nodes)
    return nodes

#func to read OS and build information
def readOneFSvers(node1):
    unamePath = os.path.join(node1, "uname")
    osVersFH = open(unamePath)
    versionLine = osVersFH.readline()
    versList = versionLine.split()
    return versList

def readPatchList(localdir):
    patchfileName = os.path.join(localdir, "local", "patch_list")
    pList = []
    patchFH = open(patchfileName)
    for line in patchFH:
        if re.search('Patch Name', line):
            pList.append(line.strip())

    return pList


def main():
    # check to see that nodes_info is in the current dir, else die
    if os.path.exists("nodes_info"):
        # assign root of logs
        logrootdir = os.getcwd()
        localdir = os.path.join(logrootdir, "local")
        #get our nested list of node info, index 0 will be header
        theseNodes = splitThisFile("nodes_info")
        numberOfNodes = len(theseNodes)
        # get our nested list of OneFS vers and build        
        osList = readOneFSvers(theseNodes[1][2])
        patchList = readPatchList(logrootdir)

        print("OneFS version: " + osList[3])
        print("Build: " + osList[7])
        print("\nInstalled patches: ")
        for p in patchList:
            print(p)
    else:
        print("Are you sure you're at the root of the log directory? " + os.curdir)

    
   
 
## end main()   

# closing lines for script execution
if __name__ == "__main__":
    main()
