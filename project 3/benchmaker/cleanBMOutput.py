# replace all non-numeric characters with blank space or commas
import re

BMOut = 'bm1outpar.txt'

with open(BMOut, 'r') as file:
        # read a list of lines into source code
        text = file.readlines()

newOutFile = ''
sawNum = False
sawM = False
text = ''.join(text)
for character in text:
    if re.search('[a-zA-Z]', character):
        sawNum = False
        if character == 'M':
            sawM = True
        else:
            sawM = False
    else:
        if character == ' ' or character == '.':
            if sawNum == True:
                newOutFile += ','
            sawNum = False
        else:
            if not sawM:
                newOutFile += character
                if character != '\n':
                    sawNum = True
                else:
                    sawNum = False
        sawM = False

with open('cleanBM1out.txt', "a") as outfile:
    outfile.write(newOutFile)