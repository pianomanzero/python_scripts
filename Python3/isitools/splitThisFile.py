#!/usr/bin/env python3


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

def splitFileInternal(incomingFile):
    splitThisFile(incomingFile)

# closing lines for script execution
if __name__ == "__main__":
    splitFileInternal()