#!/usr/bin/env python
# https://docs.python.org/3/tutorial/inputoutput.html 

from __future__ import print_function
from builtins import input
import json

"""
7.2. Reading and Writing Files
open() returns a file object, and is most commonly used with two arguments: open(filename, mode).
The first argument is a string containing the filename. The second argument is another string 
containing a few characters describing the way in which the file will be used
r = read only (default if mode omitted)
w = write only
a = append 
r+ = reading and writing

ex:
f = open('workfile', 'w')
f.close()

It is good practice to use the with keyword when dealing with file objects. 
The advantage is that the file is properly closed after its suite finishes, 
even if an exception is raised at some point. Using with is also much shorter 
than writing equivalent try-finally blocks. If you’re not using the with keyword, 
then you should call f.close() to close the file.
After a file object is closed, either by a with statement or by calling f.close(), 
attempts to use the file object will automatically fail.
"""
with open('workfile') as f:
    read_data = f.read()
# with statements automatically close file when done with block
# check whether the file handle has been closed... should return 'True'
# print(f.closed)


"""
7.2.1. Methods of File Objects
To read a file’s contents, call f.read(size), which reads some quantity of data and returns 
it as a string (in text mode) or bytes object (in binary mode). size is an optional numeric 
argument. When size is omitted or negative, the entire contents of the file will be read and 
returned; it’s your problem if the file is twice as large as your machine’s memory. 
Otherwise, at most size bytes are read and returned. If the end of the file has been reached, 
f.read() will return an empty string ('').
For reading lines from a file, you can loop over the file object. 
This is memory efficient, fast, and leads to simple code:
If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().

with open('testfile.txt') as tfile:
    for line in tfile:
        print(line, end='')
"""

        

tf = open('testfile.txt', 'r')
print(tf.readline())
tf.close()

"""
f.write(string) writes the contents of string to the file, returning the number of characters written.
Other types of objects need to be converted – either to a string (in text mode) or a 
bytes object (in binary mode) – before writing them

"""
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
# if open used with 'r+' apparently rw actually means read/append, see added lines to testfile
with open('testfile.txt', 'r+') as tfile:
    tfile.write('This is a test written from rw_files.py\n')
    tfile.write(s  + '\n')
    tfile.readlines()

"""
f.tell() returns an integer giving the file object’s current position in the file 
represented as number of bytes from the beginning of the file when in binary mode 
and an opaque number when in text mode
To change the file object’s position, use f.seek(offset, from_what). 
Position computed from adding offset to a reference point; 
reference point selected by the from_what argument. 
from_what value of 0 measures from the beginning of the file, 
1 uses the current file position, 
and 2 uses the end of the file as the reference point. 
from_what can be omitted and defaults to 0, using the beginning of the file as the reference point.
"""
# the below returns are always expressed as byte locations, note not returning string from file
with open('workfile', 'rb+') as wfile:
    wfile.write(b'derpderpderp')
    print("6th byte in file: " + str(wfile.seek(5)))
    print("7th byte in file: " + str(wfile.seek(6)))
    print("This will give us a location in b'X' format: " + str(wfile.read(1)))
    print("3rd byte before the end: " + str(wfile.seek(-3, 2)))


"""
7.2.2. Saving structured data with json
Numbers take a bit more effort, since the read() method only returns strings, which will have to 
be passed to a function like int(), which takes a string like '123' and returns its numeric value 123. 
complex data types like nested lists and dictionaries, parsing and serializing by hand becomes complicated.
Python allows for use of JSON which can take Python data hierarchies, and convert them to string representations
datastructure -> string = serialization
string -> datastructure = deserialization

"""
print(json.dumps([1, 'simple', 'list']))

"""
Another variant of the dumps() function, called dump(), 
simply serializes the object to a text file. 
So if f is a text file object opened for writing, we can do this:
"""
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
    }
tf = open('testfile.txt', 'a')
json.dump(states, tf)
# states2 = json.load(tf)
tf.close()

if __name__ == "__main__":
    import sys