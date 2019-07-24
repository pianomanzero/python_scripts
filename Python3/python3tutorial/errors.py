#!/usr/bin/env python
# https://docs.python.org/3/tutorial/errors.html

from __future__ import print_function
from builtins import input
import sys

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

"""
8.3. Handling Exceptions
It is possible to write programs that handle selected exceptions.
"""

while True:
    try:
        x = int(input("Please enter a number: "))
        print("You entered {}".format(str(x)))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again.")

"""
A class in an except clause is compatible with an exception if it is the same class or a base class thereof 
(but not the other way around — an except clause listing a derived class is not compatible with a base class). 
For example, the following code will print B, C, D in that order:
"""
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
# Note that if the except clauses were reversed (with except B first), 
# it would have printed B, B, B — the first matching except clause is triggered.
# Use this with extreme caution, since it is easy to mask a real programming error in this way! 

"""
The try … except statement has an optional else clause, which, when present, must follow all except clauses. 
It is useful for code that must be executed if the try clause does not raise an exception. For example:
The use of the else clause is better than adding additional code to the try clause because it avoids accidentally 
catching an exception that wasn’t raised by the code being protected by the try … except statement.
"""
# execute script with existing filename to see else clause...
# execute script with name of nonexitent file to trigger exception...
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()




if __name__ == "__main__":
    import sys