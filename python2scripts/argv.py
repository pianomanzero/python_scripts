#!/usr/bin/env python
from __future__ import print_function
from builtins import input
from sys import argv

script, var1, var2, var3 = argv

print("The name of the script is: ", script)
print("The first var you passed is: ", var1)
print("The second var you passed is: ", var2)
print("The third var you passed is: ", var3)

print("\n")
print("Now we're going to work with raw_input\n")


prompt='>'

print("This is a question")
answer1=input(prompt)

print("this is another question")
answer2 = input(prompt)

print("last question")
answer3 = input(prompt)

print("""
Here's your answers: %r, %r, %r
""" %(answer1, answer2, answer3))
