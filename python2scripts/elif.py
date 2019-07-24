#!/usr/bin/env python
#example of using if/elif/else

from __future__ import print_function
from builtins import input
people = int(input("enter number of people: "))
cars = int(input("enter number of cars: "))
buses = int(input("enter number of busses; "))

if cars > people:
  print("We should take more cars")
elif cars < people:
  print("We should not take more cars")
else:
  print("We can't decide what to do!!!")

if buses > cars:
  print("That's too many busses")
elif buses < cars:
  print("Maybe we should use the bus...")
else:
  print("We still can't decide what to do!!!")

if people > buses:
  print("Alright, let's just take the buss!")
else:
  print("Fine, we're just gonna stay home, cause we just can't decide what to do!!!")

