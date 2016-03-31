#   Samuel Gluss
#   Jozo Dujmovic
#   CS840 Project 2
#   Evaluation of Memory Access patterns
#   In Matrix Multiplication Performance
#   Python

import time
#import pdb; pdb.set_trace()

durations = []
#   test NxN matrices from 20x20 to 500x500 in step size 20
for matSize in range(20,520,20):
    #   number of times to repeat test at each size to minimize timer error, minimum of 1
    repCount = 1 + pow(100, 3) / pow(matSize, 3)
    
    startTime = time.clock()
    for rep in range(0,repCount):
        #   Matrix initialization
        a = [[2.0002 if i == j else 1.0001 for i in range(0,matSize)] for j in range(0,matSize)]
        b = [[2.0002 if i == j else 1.0001 for i in range(0,matSize)] for j in range(0,matSize)]
        c = [[0 for i in range(0,matSize)] for j in range(0,matSize)]
           
        #   Matrix multiplication op
        for k in range(0,matSize):
            for j in range(0,matSize):
                for i in range(0,matSize):
                    c[j][i] += a[k][i]*b[j][k]
                    
    #   calculate and append duration of test
    endTime = time.clock()
    durations.append((endTime - startTime) / repCount)

print ','.join(map(str, durations))