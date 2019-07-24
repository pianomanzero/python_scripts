#!/usr/bin/env python
from __future__ import print_function
from builtins import input
from optparse import OptionParser

"""
https://docs.python.org/3/library/optparse.html
optparse is a more convenient, flexible, and powerful library for parsing command-line options 
than the old getopt module. optparse uses a more declarative style of command-line parsing: 
you create an instance of OptionParser, populate it with options, and parse the command line. 
optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally 
generates usage and help messages for you.
"""

parser=OptionParser()
parser.add_option("-f", "--file", dest="filename", help="use FILE for these actions", metavar="FILE")
parser.add_option("-q", "--quiet", action="store_false", dest="verbose", default=True, 
help="don't print status messages to stdout")
(options, args) = parser.parse_args()

print("Your file: " + options.filename)

# closing lines for script execution
if __name__ == "__main__":
    import sys
