#!/usr/bin/env python
from __future__ import print_function
from builtins import input
from sys import argv


if len(argv) < 3:
    print("gdbcore -b <BUILD> -f release /usr/likewise/sbin/lwsmd <COREFILE>")
else:
    script, var1, var2 = argv
    print("gdbcore -b {0} -f release /usr/likewise/sbin/lwsmd {1}".format(var1,var2))



if __name__ == "__main__":
    import sys
    # easygdb(int(sys.argv[1]))