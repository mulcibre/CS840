import re
from subprocess import call
import os
import sys

#   open source file for reading
pathToSource = ["../cpp/fizbuz/fizbuz/","source.cpp"]
pathToOutfile = "../outfiles/"
outfileName = "fizbuzout.txt"

def buildAndRunExe():
    #   change working directory to location of source file
    CWD = os.getcwd()
    os.chdir(os.path.join(CWD, pathToSource[0]))

    #   set up the required environment for compiling and linking, then compile
    call(["vcvars32.bat", "&&", "cl.exe" ,"/EHsc", "".join(["instrumented", pathToSource[1]])])

    #   run resulting executable, slice extension and change to exe
    call(["".join(["instrumented",pathToSource[1][:-3],"exe"])])

    #   return to original directory
    os.chdir(CWD)

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
                        'outfile << programBodyCounters[i] << ",";',
                        '}',
                        'outfile << programBodyCounters[arraySize - 1];',
                        'outfile.close();'])

    sourceData = "\n".join([sourceData[:exitPos],
                            ofsStr,
                            sourceData[exitPos:]])

    return sourceData

with open("".join([pathToSource[0], pathToSource[1]]), 'r') as file:
    # read source code into string
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

    buildAndRunExe()

#   load block run counts
with open("".join([pathToOutfile, outfileName]), 'r') as file:
    #   Read source code into string
    sourceData = file.readlines()
    runCounts = sourceData[0].split(",")

    runCountStack = []

    #   Print source code, annotated with run counts when applicable
    with open("".join([pathToSource[0], pathToSource[1]]), 'r') as file:
        # read source code into string
        sourceData = file.read()

        print "\nLLOC runcount for original sourcecode below:\n"
        printBuf = ""
        #   only print runcount if state is 1
        state = 0

        for i in sourceData:
            if i == '{':
                #   Add new scope run count to stack
                runCountStack.append(runCounts[0])
                runCounts.pop(0)
            elif i == '}':
                runCountStack.pop()
            elif i == ';':
                #   if we read a LLOC, print the run count
                state = 1
            elif i == '\n':
                if state == 1 and runCountStack:
                    printBuf += "".join(['\t', "// Ran ", runCountStack[-1], ' times'])
                    sys.stdout.write(printBuf)
                    state = 0
                    printBuf = ""
                else:
                    sys.stdout.write(printBuf)
                    printBuf = ""
                    state = 0
            printBuf += i
        sys.stdout.write(printBuf)