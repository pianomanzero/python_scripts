#!/usr/bin/env python

#script to go over reading a file from a passed param at the cmd line

from __future__ import print_function
from builtins import input
from sys import argv
script, filename = argv

prompt=">"

txt = open(filename)

print("This is the filename you passed: %r" % filename)

print(txt.read())

print("Type the filename again:")
file_again = input(prompt)

txt_again = open(file_again)

print(txt_again.read())
