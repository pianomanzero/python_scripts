#!/usr/bin/env python
from __future__ import print_function
from builtins import input
import reprlib
import textwrap
from string import Template


"""
https://docs.python.org/3/tutorial/stdlib2.html#output-formatting
The reprlib module provides a version of repr() customized for abbreviated displays 
of large or deeply nested containers:

"""
print(reprlib.repr(set('supercalifragilisticexpialidocious')))

"""
The textwrap module formats paragraphs of text to fit a given screen width:

"""
doc = """The wrap() method is just like fill() except that it returns a list of strings instead 
of one big string with newlines to separate the wrapped lines.
This one is wrapped at 50 chars long
"""
# print(textwrap.wrap(doc, width=50))
print(textwrap.fill(doc, width=50))

"""
https://docs.python.org/3/tutorial/stdlib2.html#templating
The string module includes a versatile Template class with a simplified syntax suitable for editing 
by end-users. This allows users to customize their applications without having to alter the application.
The format uses placeholder names formed by $ with valid Python identifiers (alphanumeric characters and 
underscores). Surrounding the placeholder with braces allows it to be followed by more alphanumeric 
letters with no intervening spaces. Writing $$ creates a single escaped $:
"""
t = Template('${village} folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))

"""
The substitute() method raises a KeyError when a placeholder is not supplied in a dictionary or a 
keyword argument. For mail-merge style applications, user supplied data may be incomplete and the 
safe_substitute() method may be more appropriate — it will leave placeholders unchanged if data is missing:

"""
t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
# t.substitute(d) ### throws KeyError
print(t.safe_substitute(d))



# closing lines for script execution
if __name__ == "__main__":
    import sys
