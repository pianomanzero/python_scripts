#!/usr/bin/env python
# https://docs.python.org/3/tutorial/inputoutput.html 

from __future__ import print_function
from builtins import input

print("With print() we can print some output")
print("Sometimes you'll want to write in other ways")

"""
Formatted string literals (also called f-strings for short) let you include the value of 
Python expressions inside a string by prefixing the string with f or F and writing 
expressions as {expression}.
"""
year = 2016
event = 'referendum'
print(f'results of the {year} {event}')
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


"""
The str.format()
The brackets and characters within them (called format fields) are replaced with the 
objects passed into the str.format() method. A number in the brackets can be used to
 refer to the position of the object passed into the str.format() method
The str.format() method of strings requires more manual effort. 
You’ll still use { and } to mark where a variable will be substituted 
and can provide detailed formatting directives, but you’ll also need 
to provide the information to be formatted.
If keyword arguments are used in the str.format() method, 
their values are referred to by using the name of the argument.
"""
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

"""
The str() function is meant to return representations of values which are fairly human-readable, 
while repr() is meant to generate representations which can be read by the interpreter 
(or will force a SyntaxError if there is no equivalent syntax). 
For objects which don’t have a particular representation for human consumption, 
str() will return the same value as repr(). Many values, such as numbers or structures 
like lists and dictionaries, have the same representation using either function. 
Strings, in particular, have two distinct representations.
"""

s = 'Hello, world.'
print(str(s))
print(repr(s))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)







if __name__ == "__main__":
    import sys