#!/usr/bin/env python
from __future__ import print_function
from sys import argv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', nargs='+', help="the port(s) you would like to telnet to", type=int)
parser.add_argument('-i', '--IP', nargs='+', help="the IP address(es) you would like to telnet to", type=str)

args = parser.parse_args()
print(args.IP)
print(args.port)


