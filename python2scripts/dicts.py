#!/usr/bin/env python
#script to illustrate use of dictionaries
from __future__ import print_function
from builtins import input
import __future__

#initiate dict
stuff = {'name':'Zed', 'age':36, 'height': 6*12+2}

print(("stuff: ", stuff))

print(("stuff['name']: ", stuff['name']))
print(("stuff['age']: ", stuff['age']))
print(("stuff['height']: ", stuff['height']))
print ("set a city name to add to the stuff dictionary:")
stuff['city'] = input("> ")
print(("stuff['city']: ", stuff['city']))

#dicts can also be addressed with numbered indexes instead of strings
stuff[1] = "Boom!"
stuff[2] = "Wow!"

print(("stuff[1]: ", stuff[1]))
print(("stuff[2]: ", stuff[2]))
print(("stuff dict: ", stuff))

print ("You can delete entries from dictionaries as well:")

del stuff['city']
del stuff[1]
del stuff[2]
print (stuff)
