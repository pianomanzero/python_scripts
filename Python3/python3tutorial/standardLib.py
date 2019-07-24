#!/usr/bin/env python
from __future__ import print_function
from builtins import input
import os
import shutil
import glob
import sys
import re
import math
import random
import statistics
from urllib.request import urlopen
from datetime import date
from timeit import Timer



# https://docs.python.org/3/tutorial/stdlib.html

"""
The os module provides dozens of functions for interacting with the operating system:
Be sure to use the import os style instead of from os import *. 
This will keep os.open() from shadowing the built-in open() function which operates much differently.
The built-in dir() and help() functions are useful as interactive aids for working with large modules like os:

firstDir = os.getcwd()
print(os.getcwd())
os.chdir('/Users/morrit10/Documents')
print(os.getcwd())
os.chdir(firstDir)
print(os.getcwd())
os.system('mkdir testdir')
os.chdir('testdir')
print(os.getcwd())
os.chdir(firstDir)
print(os.getcwd())
os.system('rmdir testdir')
"""

"""
For daily file and directory management tasks, the shutil module provides a higher level interface that is easier to use:
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
"""

"""
The glob module provides a function for making file lists from directory wildcard searches:

"""
# print list of files currently in pwd
print(glob.glob('*.py'))


"""
Common utility scripts often need to process command line arguments. 
These arguments are stored in the sys module’s argv attribute as a list. 
For instance the following output argv optinos passed at the command line:

"""
print(sys.argv)

"""
The re module provides regular expression tools for advanced string processing. 
For complex matching and manipulation, regular expressions offer succinct, optimized solutions:
"""
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
"""
When only simple capabilities are needed, string methods are preferred because they are easier to read and debug:
"""
print('tea for too'.replace('too', 'two'))

"""
The math module gives access to the underlying C library functions for floating point math:
The random module provides tools for making random selections:
The statistics module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data:
The SciPy project <https://scipy.org> has many other modules for numerical computations.

"""
print(math.cos(math.pi / 4))
print(math.log(1024, 2))

# random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))   # sampling of 10 from range of 100 without replacement
print(random.random())    # random float
print(random.randrange(6))    # random integer chosen from range(6)

# statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print("mean: " + str(statistics.mean(data)))
print("median: " + str(statistics.median(data)))
print("variance: " + str(statistics.variance(data)))



"""
https://docs.python.org/3/tutorial/stdlib.html#internet-access
There are a number of modules for accessing the internet and processing internet protocols. 
Two of the simplest are urllib.request for retrieving data from URLs and smtplib for sending mail:


# this example takes a minute, take it out of the docstring to let it run
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)
"""

"""
https://docs.python.org/3/tutorial/stdlib.html#dates-and-times
The datetime module supplies classes for manipulating dates and times in both simple and complex ways. 
While date and time arithmetic is supported, the focus of the implementation is on efficient member 
extraction for output formatting and manipulation. 
The module also supports objects that are timezone aware.

"""
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# dates support calendar arithmetic
birthday = date(1981, 3, 25)
age = now - birthday
print("you are " + str(age.days) + " days old")
print("you are " + str(age.days/50) + " weeks old")
print("you are " + str(age.days/365) + " years old")
print("you are " + str((age.days/365)/10) + " decades old")



"""
https://docs.python.org/3/tutorial/stdlib.html#performance-measurement
Some Python users develop a deep interest in knowing the relative performance of different 
approaches to the same problem. Python provides a measurement tool that answers those questions immediately.
The timeit module quickly demonstrates a modest performance advantage.
In contrast to timeit’s fine level of granularity, the profile and pstats modules provide tools for 
identifying time critical sections in larger blocks of code.
https://docs.python.org/3/library/timeit.html#module-timeit
https://docs.python.org/3/library/profile.html#module-profile 
https://docs.python.org/3/library/profile.html#module-pstats

"""
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

"""

10.12. Batteries Included
Python has a “batteries included” philosophy. This is best seen through the sophisticated 
and robust capabilities of its larger packages. For example:

The xmlrpc.client and xmlrpc.server modules make implementing remote procedure calls into an 
almost trivial task. Despite the modules names, no direct knowledge or handling of XML is needed.

The email package is a library for managing email messages, including MIME and other 
RFC 2822-based message documents. Unlike smtplib and poplib which actually send and receive 
messages, the email package has a complete toolset for building or decoding complex message 
structures (including attachments) and for implementing internet encoding and header protocols.

The json package provides robust support for parsing this popular data interchange format. 
The csv module supports direct reading and writing of files in Comma-Separated Value format, 
commonly supported by databases and spreadsheets. XML processing is supported by the 
xml.etree.ElementTree, xml.dom and xml.sax packages. Together, these modules and packages 
greatly simplify data interchange between Python applications and other tools.

The sqlite3 module is a wrapper for the SQLite database library, providing a persistent database 
that can be updated and accessed using slightly nonstandard SQL syntax.

Internationalization is supported by a number of modules including gettext, locale, 
and the codecs package.

"""





# closing lines for script execution
if __name__ == "__main__":
    import sys
