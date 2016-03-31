#   a program to compile a bunch of cpp files
#   record compile times and filesizes
#   Samuel Gluss
#   3/27/2016
#import pdb; pdb.set_trace()
import re,glob, os, time
from subprocess import call,check_output

#   path vars
outputFilename = 'compilerTestOutfile.txt'
getEnvVars = 'vcvars32.bat'
compilerCommand = 'cl'
compilerFlag = '/Bt'

#   get list of cpp files
cppFiles = []
for file in glob.glob("*.cpp"):
    cppFiles.append(file)
    
#   clear outfile
open(outputFilename, 'w').close()

#   get environment vars
call(getEnvVars)

for file in cppFiles:
    #   get cpp size in bytes
    cppSize = os.path.getsize(file)
    cppSize = re.search('[0-9]+', str(cppSize)).group(0)
    with open(outputFilename, "a") as outfile:
        #   The below line of code seeks to the end of the outfile
        outfile.seek( 0, 2 )
        
        startTime = time.clock()
        compilerOutput = check_output([compilerCommand,file,'/O2'])
        endTime = time.clock()
        #   getting duration of compiling
        #duration = re.search('Final\: Total time \= ([0-9\.]+)', compilerOutput)
        #compileTime = duration.group(1)
        compileTime = endTime - startTime
        
        #   getting size of file
        execFilename = re.search('[a-zA-Z0-9]+', file)
        exeName = execFilename.group(0)
        exeSize = os.path.getsize(exeName + '.exe')
        exeSize = re.search('[0-9]+', str(exeSize)).group(0)

        #   get number of benchmark
        fileName = re.search('BM1bigcode([0-9]+)', file)
        benchNo = fileName.group(1)

        #   write everything to the outfile
        outfile.write(','.join([str(benchNo), str(cppSize), str(exeSize), str(compileTime)]))
        outfile.write('\n')