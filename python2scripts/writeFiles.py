#!/usr/bin/env python
#reading and writing files

from __future__ import print_function
from builtins import input
from sys import argv



script, filename = argv

print("We will now erase the following file: %r" % filename)
print("If you do not want to erase %r, hit CTRL-C." % filename)
print("If you wish to continue, press ENTER")

input("?")

print("Opening file...")
target = open(filename, 'w')

print("Truncating file now...")
target.truncate()
print("The content of %r has been erased." % filename)
print("\n")
print("We will now write some additional content to %r." % filename)
print("Write three lines:")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Your three lines will now be written to %r" % filename)

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Now closing %r" % filename)
target.close()
