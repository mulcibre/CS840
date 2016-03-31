#   Samuel Gluss
#   2/25/2016
#   Driver program for python Matrix Multiplication

#import pdb; pdb.set_trace()
#   external library which allows cmd calls
from subprocess import call

'''
   String resources
'''

#   update the value below to set the location of the first for loop
indentLevel = 4
firstLoopLine = 39
compilerPath = "javac"
sourceFilename = "C:\Users\sam\IdeaProjects\cs840project2javamatmult\src\matmult.java"
outputFilename = 'outfiles/javaoutfile.txt'
input = list(range(0,3))

mathOps =   ['c[i][j] += a[i][k]*b[k][j];\n', 
             'c[i][j] += a[i][k]*b[j][k];\n',
             'c[i][j] += a[k][i]*b[k][j];\n',
             'c[i][j] += a[k][i]*b[j][k];\n',
             'c[j][i] += a[i][k]*b[k][j];\n',
             'c[j][i] += a[i][k]*b[j][k];\n',
             'c[j][i] += a[k][i]*b[k][j];\n',
             'c[j][i] += a[k][i]*b[j][k];\n' ]

forLoops =  ['for (int i = 0; i < rowCount; i++) {\n',
            'for (int j = 0; j < rowCount; j++) {\n',
            'for (int k = 0; k < rowCount; k++) {\n']
'''
    Begin Function section
'''

def ptabs(numTabsToPrint):
    numTabsToPrint += indentLevel
    tabs = ""
    for i in range(0,numTabsToPrint):
        tabs += '    '
    return tabs

def executeTestFile():
    #   compile step, if needed (keep this for the C++ code)
    call([compilerPath, "-d", ".",sourceFilename])

    #   execute source code, writing results to outfile
    with open(outputFilename, "a") as outfile:
        #   The below line of code seeks to the end of the outfile
        outfile.seek( 0, 2 ) 
        call(["java", "matmult"], stderr=outfile, stdout=outfile)
        
    
def modifySourceCode(permutation, sourceCode):
    #   modify for loops once per permutation
    #   source code lines index on 1
    sourceCode[firstLoopLine-1] = ptabs(0) + forLoops[permutation[0]]
    sourceCode[firstLoopLine] = ptabs(1) + forLoops[permutation[1]]
    sourceCode[firstLoopLine+1] = ptabs(2) + forLoops[permutation[2]]
    
    #   run each of 8 math op orders per for loop permutation
    for i in range(0,8):
        sourceCode[firstLoopLine+2] = ptabs(3) + mathOps[i]
        
        # write changes back to source code
        with open(sourceFilename, 'w') as file:
            file.writelines( sourceCode )
        
        executeTestFile()
        
        print "executed for loop config " + str(permutation) + " with inner op #" + str(i)
    
def createPermutations(inputList, outputList, sourceCode):
    #   base case: print result if there is only one possibility left
    if len(inputList) <= 1:
        #   once a permutation is completed, produce the appropriate source code
        modifySourceCode(outputList + inputList, sourceCode)
    else:
        #   Due to python, new lists must be allocated for each recursion
        for element in inputList:
            newInput = list(inputList)
            newOutput = list(outputList)
            newInput.remove(element)
            newOutput.append(element)
            createPermutations(newInput,newOutput, sourceCode)
            
def runTest():
    #   clear outfile
    open(outputFilename, 'w').close()

    # Open desired file, with keyword closes automatically
    with open(sourceFilename, 'r') as file:
        # read a list of lines into source code
        sourceCode = file.readlines()
    
    #   generate for loop permutations, test resulting source code
    createPermutations(list(range(0,3)),[],sourceCode)      
    
    print "Test execution completed"
runTest()