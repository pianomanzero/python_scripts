#!/usr/bin/env python3
from __future__ import print_function
from builtins import input
import sys
import os
import subprocess
import humanfriendly

def main():
    mystr="63.3k"
    print("mystr is a " + str(type(mystr)) + " and holds the value: " + mystr)
    #myconvstr = float(mystr)
    myconvstr = humanfriendly.parse_size(mystr)
    print("myconvstr is a " + str(type(myconvstr)) + " and holds the value: " + str(myconvstr))
    print("lets see if we can convert it back again...")
    mystr2 = humanfriendly.format_size(myconvstr)
    print("mystr2 is of type " + str(type(mystr2)) + " and holds the value: " + mystr2)
    


# closing lines for script execution
if __name__ == "__main__":
    main()