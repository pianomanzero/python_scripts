#!/usr/bin/env python


from __future__ import print_function
from builtins import input
from sys import argv
import subprocess


def splitThisFile(file):
    workfile = file
    nodes = open(workfile, "r")
    listOfLines = nodes.readlines()
    nodes = []
    for L in range(len(listOfLines)):
        thisline = listOfLines[L] 
        #nodes.append(thisline.split())
        nodes.append(thisline)
    # print(nodes)
    return nodes


def main():
    myfile = "mycommands"
    cmdList = splitThisFile(myfile)
    
    if len(argv) < 2:
        print()
        for c in range(0,len(cmdList)):
            print(cmdList[c])
        print()

    else:
        script, var1 = argv
        #index = int(var1)
        if isinstance(int(var1), int):
            index = int(var1)
            print(cmdList[index])
        else:
            print("I need an integer")
            quit()

# closing lines for script execution
if __name__ == "__main__":
    import sys
    # if main is defined, uncomment next line
    main()
