#!/usr/bin/env python
import os
import sys
import subprocess


def mkdirs():
  curDir = os.getcwd()
  curDir += '/'
  print "Enter the name of your new directory:"
  newdir = raw_input()
  print "Enter the number of directories to create:"
  count = raw_input()
  for x in range(int(count)):
    out_str = ''
    out_str += curDir
    out_str += newdir
    out_str += str(x)
    os.makedirs(out_str)
    
    print 'created directory: ' + out_str
    
    command = ''
    command += "touch ./" + out_str + "/test.txt"
    
    file_path = out_str + '/' + 'test.txt'
    
    file = open(file_path, 'w')
    file.write('this file is located at ' + file_path)
    file.close()
    print 'created file: ' +  file_path

mkdirs()
