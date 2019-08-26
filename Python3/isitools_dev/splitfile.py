#!/usr/bin/env python3
from __future__ import print_function
from builtins import input
from optparse import OptionParser
import sys
import os
import subprocess
import re


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

def main():
    parser=OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="use FILE for these actions", metavar="FILE")
    (options, args) = parser.parse_args()
    print(type(options.filename))
    listsOfThings = splitThisFile(options.filename)
    print(listsOfThings)

# closing lines for script execution
if __name__ == "__main__":
    import sys
    main()