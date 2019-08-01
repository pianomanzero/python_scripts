#!/usr/bin/env python3
"""
Refs:
https://docs.python.org/3/library/sqlite3.html
http://www.sqlitetutorial.net/sqlite-python/ 
https://github.com/ActiveState/code/tree/master/recipes/Python 
https://github.com/ActiveState/code/tree/master/recipes/Python/189858_Python_text_to_pdf_converter

"""


from __future__ import print_function
from builtins import input
import sys
import os
import subprocess
import sqlite3
from sqlite3 import Error

# create db conn
def create_connection (db_file):
    """ create a database connection to the SQLite database
    specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return None


def prepfile(filename):



def main():


    #end main()

# closing lines for script execution
if __name__ == "__main__":
    main()