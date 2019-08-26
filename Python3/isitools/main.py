#!/usr/bin/env python
from __future__ import print_function
from builtins import input
import sys
from splitThisFile import splitThisFile
from sys import argv

def main():
    script, var1 = argv
    headers = splitThisFile(var1)
    print(headers)




# closing lines for script execution
if __name__ == "__main__":
   
    # if main is defined, uncomment next line
    main()
