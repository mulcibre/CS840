#import pdb; pdb.set_trace()

input = list(range(0,3))
output = []

forLoops =  ['for i in range(0,numRows):',
            'for j in range(0,numRows):',
            'for k in range(0,numRows):']
oneTab = '    '
#print(forLoops)
#print(input)
#print

def printLoops(indexList):
    count = 0
    for index in indexList:
        for i in range(0,count):
            print oneTab,
        print forLoops[index]
        count += 1
    print

def createPermutations(inputList, outputList):
    #   base case: print result if there is only one possibility left
    if len(inputList) <= 1:
        printLoops(outputList + inputList)
    else:
        #   Due to python, new lists must be allocated for each recursion
        for element in inputList:
            newInput = list(inputList)
            newOutput = list(outputList)
            newInput.remove(element)
            newOutput.append(element)
            createPermutations(newInput,newOutput)
           
createPermutations(input,[])