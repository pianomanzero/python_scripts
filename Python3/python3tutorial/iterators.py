#!/usr/bin/env python
# https://docs.python.org/3/tutorial/classes.html#iterators

from __future__ import print_function
from builtins import input

"""
By now you have probably noticed that most container objects can be looped over using a for statement.
This style of access is clear, concise, and convenient. The use of iterators pervades and unifies Python.

"""

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one-key':1, 'two-key':2, 'three-key':3}:
    print(key)
for char in "123":
    print(char)
# for line in open("myfile.txt"):
#    print(line, end='')

"""
Behind the scenes, the for statement calls iter() on the container object. 
The function returns an iterator object that defines the method __next__() which accesses elements 
in the container one at a time. When there are no more elements, __next__() raises a 
StopIteration exception which tells the for loop to terminate. 
You can call the __next__() method using the next() built-in function; 
this example shows how it all works:
"""

s = 'abc'
it = iter(s)
# print loc of iterator obj
print(it)
print("Next: " + next(it)) # a
print("Next: " + next(it)) # b
print("Next: " + next(it)) # c
# adding another instance of the above throws exception 'StopIteration'
# print("Next: " + next(it)) 

"""
Generators are a simple and powerful tool for creating iterators. 
They are written like regular functions but use the yield statement 
whenever they want to return data. Each time next() is called on it, 
the generator resumes where it left off 
(it remembers all the data values and which statement was last executed). 
An example shows that generators can be trivially easy to create:
"""
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)



if __name__ == "__main__":
    import sys

