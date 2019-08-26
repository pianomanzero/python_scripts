#!/usr/bin/env python3
from __future__ import print_function
from builtins import input
import sys
import os
import subprocess
from optparse import OptionParser
import pandas as pd

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
    parser.add_option("-s", "--sort-by", dest="sortby", default="TimeInQ", help="order output by this column")
    parser.add_option("-f", "--file", dest="file_dest", default="screen", help="output to file location")
    # open isi_statistics_drive for reading
    (options, args) = parser.parse_args()

    drivestats = splitThisFile("isi_statistics_drive")
    #print(drivestats[0])

    headers = drivestats[0]
    myData = []
    for r in range(2,len(drivestats)-2):
        myData.append(drivestats[r])
    #print(headers)
    #print(myData)
    myframe = pd.DataFrame(data=myData, columns=headers)
    print(myframe.sort_values(by=options.sortby, ascending=False))

# closing lines for script execution
if __name__ == "__main__":
    main()