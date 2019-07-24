#!/usr/bin/env python
from __future__ import print_function
import time

ten_things = "Apples Oranges Crows Telephones Lights Sugar"

print("Ten things: ", ten_things)

time.sleep(1)

print("Um, wait, that's not ten things...", time.sleep(1), "let's fix that..")

#using the split list function, passing delimiter
stuff = ten_things.split(' ')
more_stuff = ["day","night","song","frisbee","corn","banana","girl","boy"]

while len(stuff) != 10:
#use the pop list function to pop an antry from a list into another var
  next_one = more_stuff.pop()
  print("Adding: ", next_one)
  #take popped value dropped into next_one and append to stuff list using append list function
  stuff.append(next_one)
  print("There's now %d items in the stuff list" % len(stuff))

print("There we go: ", stuff)

print("Let's do some more things with stuff")

time.sleep(1)

print("stuff[1]: ", stuff[1])

time.sleep(1)

print("stuff[-1]: ", stuff[-1])
print("using stuff.pop() ", stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

