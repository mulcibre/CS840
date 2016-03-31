#   Samuel Gluss
#   2/25/2016
#   Driver program for python Matrix Multiplication

#import pdb; pdb.set_trace()
#   external library which allows cmd calls
from subprocess import call

'''
   String resources
'''

mathOps =   ['ij+=ik*kj', 
             'ij+=ik*jk',
             'ij+=ki*kj',
             'ij+=ki*jk',
             'ji+=ik*kj',
             'ji+=ik*jk',
             'ji+=ki*kj',
             'ji+=ki*jk' ]

forLoops =  ['i',
            'j',
            'k']
'''
    Begin Function section
'''

#   adds appropriate elements for each for loop configuration
def addPermToOutput(permutation, output):
    outputString = ""
    for i in range(0,8):
        if outputString != "":    
            outputString += ','
        for j in permutation:
            outputString += forLoops[j]
        outputString += ":"
        outputString += mathOps[i]
        
    #   add outputstring to output
    output.append(outputString)
   
def createPermutations(inputList, outputList, output):
    #   base case: print result if there is only one possibility left
    if len(inputList) <= 1:
        #   once a permutation is completed, produce the appropriate source code
        addPermToOutput(outputList + inputList, output)
    else:
        #   Due to python, new lists must be allocated for each recursion
        for element in inputList:
            newInput = list(inputList)
            newOutput = list(outputList)
            newInput.remove(element)
            newOutput.append(element)
            createPermutations(newInput,newOutput, output)
            
def main():
    output = []
    createPermutations(list(range(0,3)),[],output)
    with open("labels.txt", 'w') as outfile:
        outfile.write(','.join(output))

    print "execution completed"
    
main()