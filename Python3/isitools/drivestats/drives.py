#!/usr/bin/env python3
"""
Refs:
https://docs.python.org/3/library/sqlite3.html
https://www.tutorialspoint.com/sqlite/sqlite_python 
https://cmdlinetips.com/2018/02/how-to-sort-pandas-dataframe-by-columns-and-row/


TODO: rewrite hard-coded insert statement

"""


from __future__ import print_function
from builtins import input
import sys
import os
import subprocess
import sqlite3
import humanfriendly
from sqlite3 import Error
from optparse import OptionParser
import pandas as pd


# func to read nodes_info file and return nested list of contents
def splitThisFile(file):
    workfile = file
    nodes = open(workfile, "r")
    listOfLines = nodes.readlines()
    nodes = []
    for L in range(len(listOfLines)):
        thisline = listOfLines[L] 
        nodes.append(thisline.split())
    # print(nodes)
    return nodes


def main():
    
    parser=OptionParser()
    parser.add_option("-o", "--order-by", dest="orderby", default="TimeInQ", help="order SQL query descending by this column")
    parser.add_option("-i", "--insert", dest="insert_action", default=False, help="read file and insert")
    # open isi_statistics_drive for reading
    (options, args) = parser.parse_args()

    # print("Insert action: " + str(options.insert_action))

    ids=open('isi_statistics_drive', 'r')
    driveHeader=ids.readline()
    headers=driveHeader.split()
    dashes=ids.readline()
    
    # this is how to access each header looped
    """
    for h in headers:
        print(h)
    """
    # print(len(headers))

    database="drivestats.db"
    
    """
    The next several lines have to do with building the statement which we will use to create the initial table
    We will use the header from the file itself to act as column names
    """
    conn = sqlite3.connect(database)
    # print(sqlite3.version + " connected")
    sql_create_drivestats_table = """ CREATE TABLE IF NOT EXISTS drivestats (
        id integer primary key,
        Drive double,
        Type double,
        OpsIn double,
        BytesIn double,
        SizeIn double,
        OpsOut double,
        BytesOut double,
        SizeOut double,
        TimeAvg double,
        Slow double,
        TimeInQ double,
        Queued double,
        Busy double,
        Used double,
        Inodes double); 
    """

        
    # check our statement for accuracy...
    #print(sql_create_drivestats_table)
    

    # create a cursor, use to execute the create table statement
    try:
        c = conn.cursor()
        c.execute(sql_create_drivestats_table)
    except Error as e:
        print(e)

    
    # build insert statement intro, then add per line    
    # loop through each line of file, load into list named ins
    insIterator = 0
    for rline in ids:
        
        insline = """INSERT INTO drivestats (Drive,Type,OpsIn,BytesIn,SizeIn,OpsOut,BytesOut,SizeOut,TimeAvg,Slow,TimeInQ,Queued,Busy,Used,Inodes) values ('"""
        
        ins = rline.split()
        # loopy-doodle through listy-wisty
        for i in range(1,len(ins)):
            if i == len(ins)-1:
                insline += ins[i] + "')"
            else:
                if i > 2 and i < len(ins) -7:
                    insline += str(humanfriendly.parse_size(ins[i])) + "','"
                else:
                    insline += ins[i] + "','"

        # uncomment this line to check the insline insert statement
        #print(insline)
        
       
        try:
            i = conn.cursor()
            # inserting in this manner, where we've built a dynamic SQL line, requires us to use the
            # executescript method of the cusrsor obj
            if options.insert_action:
                i.executescript(insline)

        except Error as e:
            print(e)
        
    
    selectStatement = "Select Drive,Type,OpsIn,BytesIn,SizeIn,OpsOut,BytesOut,SizeOut,TimeAvg,Slow,TimeInQ,Queued,Busy,Used,Inodes from drivestats order by " + options.orderby + " desc"
    #print(selectStatement)
    try:
        i.execute(selectStatement)
    except Error as e:
        print(e)
    
    results = i.fetchall()
    #print(results)

    """

    TODO: REWRITE SELECT SECTION TO PLUG RESULTS BACK INTO A LIST OF TUPLES 
            - at this point we can pretty-up and 'humanfriendly' the fields
            - fix the milliseconds problem.... we don't need to pretty up prior to inserting...
    
    pheader=""
    for h in range(1,len(headers)):
        pheader += str(headers[h]) + "  "

    print(pheader)
    for row in results:
        
        rows=""
        for e in range(1,len(row)):
            
            if e > 2 and e < len(row) -3:
                #rows += str(row[e]) + "\t"
                if row[e] < 999:
                    rows += str(row[e]) + "\t"
                else:
                    rows += humanfriendly.format_size(row[e]) + "  "
            else:
                rows += str(row[e]) + "\t"
        print(rows)    
        
    """
    df = pd.read_sql_query(selectStatement, conn)
    resultsToDS = df.head(n=15)
    # print(resultsToFile)
    print(type(resultsToDS))
    resultsToFile = list(resultsToDS.itertuples(index=False, name=None))
    print(type(resultsToFile))
    pheader=""
    for h in range(1,len(headers)):
        pheader += str(headers[h]) + "  "

    rows=""
    for e in range(1,len(row)):
        if e > 2 and e < len(row) -3:
        #rows += str(row[e]) + "\t"
            if row[e] < 999:
                rows += str(row[e]) + "\t"
            else:
                rows += humanfriendly.format_size(row[e]) + "  "
        else:
            rows += str(row[e]) + "\t"
        print(rows)  

    print(pheader)
    with open("myfile.txt", "w") as outfile:
        outfile.write(str(resultsToFile))
    

# closing lines for script execution
if __name__ == "__main__":
    main()