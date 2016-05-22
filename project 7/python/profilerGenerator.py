import re

#   open source file for reading
pathToSource = ["../cpp/fizbuz/fizbuz/","source.cpp"]
outfileName = "fizbuzout.txt"

def addStreamLibs(sourceData):
    #   make sure required libraries
    if not hasIOStream:
        sourceData = "".join(["#include <iostream>\n", sourceData])
    if not hasFStream:
        iostrLoc = re.search('\#include[ ]+\<iostream\>', sourceData)
        sourceData = "\n".join([sourceData[:iostrLoc.end()],
                                '#include <fstream>',
                                sourceData[iostrLoc.end():]])
    return sourceData

def addCounters(sourceData):
    #   Instrument code by adding counters after every left curly brace
    counter, mark = 0, 0
    temp = ""
    for i in range(0, len(sourceData)):
        if sourceData[i] == "{":
            #   build counter string
            countStr = "".join(['programBodyCounters[', str(counter), ']++;'])

            #   Add counter string after curly brace
            temp = "\n".join([temp, sourceData[mark:i + 1], countStr])
            mark = i + 1
            counter += 1

    # Add remainder of program
    temp = "".join([temp, sourceData[mark:]])
    return temp

def addCounterArr(sourceData):
    #   Add profiler counter array to wherever fstream directive is
    #   this is done after the code is instrumented to prevent the initializer here
    #   from being instrumented as well!
    fstrLoc = re.search('\#include[ ]+\<fstream\>', sourceData)
    counterStr = "".join(['int programBodyCounters[', str(numLeftCurlies), '] = { 0 };'])
    sourceData = "\n".join([sourceData[:fstrLoc.end()],
                            counterStr,
                            sourceData[fstrLoc.end():]])
    return sourceData

def addOutfilePrint(sourceData, outfileName):
    #   find the exit point of the main function.
    #   Output to file will go right before this
    mainFuncPos = re.search('int main\(\)[ \n]*\{', sourceData).end()
    exitPos = re.search('[ \t]*return 0;', sourceData[mainFuncPos:]).start() + mainFuncPos - 1

    #   build outfile print string
    ofsStr = "\n".join(['ofstream outfile;',
                        'outfile.open("../../../outfiles/' + outfileName + '");',
                        'int arraySize = sizeof(programBodyCounters) / sizeof(int);',
                        'for (int i = 0; i < arraySize - 1; i++)',
                        '{',
                        'outfile << programBodyCounters[i] << ", ";',
                        '}',
                        'outfile << programBodyCounters[arraySize - 1];',
                        'outfile.close();'])

    sourceData = "\n".join([sourceData[:exitPos],
                            ofsStr,
                            sourceData[exitPos:]])

    return sourceData

with open("".join([pathToSource[0], pathToSource[1]]), 'r') as file:
    # read a list of lines into source code
    sourceData = file.read()

    numLeftCurlies = sourceData.count('{')
    hasFStream = re.match('\#include[ ]+\<fstream\>',sourceData)
    hasIOStream = re.match('\#include[ ]+\<iostream\>',sourceData)

    #   make sure source code has required fstream and iostream libraries
    sourceData = addStreamLibs(sourceData)

    #   instrument code with counters
    sourceData = addCounters(sourceData)

    #   add array of counters to beginning of source code
    sourceData = addCounterArr(sourceData)

    #   Add code to print to appropriate outfile
    sourceData = addOutfilePrint(sourceData, outfileName)

    #   Write Instrumented source code to new file
    with open("".join([pathToSource[0], "instrumented", pathToSource[1]]), 'w') as file:
        #   write back to gnuplot file
        file.writelines(sourceData)