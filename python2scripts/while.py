#!/usr/bin/env python

from __future__ import print_function
i = 0
numbers = []

while i < 6:
  print("At the top i is %d" % i)
  numbers.append(i)

  i = i + 1
  print("Numbers now: ", numbers)
  print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
  print(num)
