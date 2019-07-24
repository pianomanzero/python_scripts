#!/usr/bin/env python

""" execute something outside of Python
"""
from __future__ import print_function

import subprocess

retcode = subprocess.call(['ls', '-l', '/home'])
print("returned", retcode)

retcode = subprocess.call(['ls', '-l', '/home/nobody'])
print("returned", retcode)
