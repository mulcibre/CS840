#   C++ parser
#   CSC840
#   Samuel Gluss
#   Jozo Dujmovic
#   3/24/2016
#
from subprocess import call
import re
#import pdb; pdb.set_trace()

sourceFilename = 'D:\Sam\Documents\CS840\project 3\BM1default1.cpp'

cppTypes = 'int|double|float|char|long|bool|short|long int|long long|long double'
print 'types in C++: ' + cppTypes
print

# Open desired file, with keyword closes automatically
with open(sourceFilename, 'r') as file:
    # read in source code
    sourceCode = file.read()
     
semiCount = len(re.findall(';',sourceCode))        
print 'found ' + str(semiCount) + ' semicolons'

#   Count For loops
#   match 'for' followed by 0 or more spaces, then '('
#   match anything, then a ';' twice, then anything, followed by ')'
forCount = len(re.findall('for{1} *\({1}(.*?;{1}){2}.*?\){1}',sourceCode))
print 'found ' + str(forCount) + ' for loops'

newLineCount = len(re.findall('\\n',sourceCode))
print 'found ' + str(newLineCount) + ' newlines'

blankLinesCount = len(re.findall('\\n *\\n',sourceCode))
print 'found ' + str(blankLinesCount) + ' blank lines'

varInittypeRE = '(?=[^' + cppTypes + '] *' + cppTypes + '{1} *'
varInitRE = varInittypeRE + '([A-Za-z0-9] *, *)*[A-Za-z0-9]+)'
varInit = len(re.findall(varInitRE,sourceCode))
print 'found ' + str(varInit) + ' var initializations'

print
PLOC = newLineCount - blankLinesCount
print 'PLOC: ' + str(PLOC)