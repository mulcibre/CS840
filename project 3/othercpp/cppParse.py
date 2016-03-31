#sam is the master
import re,glob
#import pdb; pdb.set_trace()
from enum import Enum

outputFilename = 'outfile.txt'

cppTypes = '(long\slong|long\sdouble|long\sint|char|bool|short|int|long|float|double)'
controls = '(for|while|if)'

class State(Enum):
    normal = 0
    startComment =1
    string=2
    preprocessing=3
    char=4
    lineComment=5
    blockComment=6
    blockCommentEnd=7
    specialString=8
    specialChar=9

    #   function which eliminates any comments/preprocessor/other nonlogical lines
def getNormalCode(source):
    retVal = []
    state = State.normal
    for character in source:
        if state == State.normal:
            if character == '/':
                state = State.startComment
            elif character == '"':
                state = State.string
            elif character == '#':
                state = State.preprocessing
            elif character == '\'':
                state = State.char
            else:
                state = State.normal
        elif state == State.preprocessing:
            if character == '\n':
                state = State.normal
            else:
                state = State.preprocessing
        elif state == State.startComment: 
            if character == '/': 
                state = State.lineComment
            elif character ==  '*':
                state = State.blockComment
            else: 
                state = State.normal
        elif state == State.lineComment: 
            if character == '\n':
                state = State.normal
            else:
                state = State.lineComment
        elif state == State.blockComment: 
            if character == '*': 
                state = State.blockCommentEnd
            else:
                state = State.blockComment
        elif state == State.blockCommentEnd: 
            if character == '/': 
                state = State.normal
            elif character == '*': 
                state = State.blockCommentEnd
            else: 
                state = State.blockComment
        elif state == State.string: 
            if character == '\\':
                state = State.specialString
            elif character == '"': 
                state = State.normal
            else: 
                state = State.string
        elif state == State.specialString: 
            state = State.string
        elif state == State.char: 
            if character == '\\': 
                state = State.specialChar
            elif character == '\'': 
                state = State.normal   
            else: 
                state = State.char
        elif state == State.specialChar: 
            state = State.char
        if state == State.normal:
            retVal.append(character)
    return(''.join(retVal))

    #   function which cleans contents of brackets for certain counting ops
def stripBrackets(source):
    retVal = []
    bracketLevel = 0
    for character in source:
        if character == '{' or character == '[':
            bracketLevel += 1
        elif character == '}' or character == ']':
            bracketLevel -= 1
        elif bracketLevel == 0:
            retVal.append(character)
    return(''.join(retVal))

def getCounts(filepath):
    with open(filepath,'r') as f:
        code = f.read()
    #semiCount = code.count(';')

    code = getNormalCode(code)

    #   determine PLOC by finding all nonempty lines
    #   lines must have something other than space, or curly braces
    newLineCount = len(re.findall('[a-zA-Z0-9]+[^\n]*\n',code))
    #blankLinesCount = len(re.findall('\n[\s\{\}]*?\n',code))
    PLOC = newLineCount# - blankLinesCount

    ifCount = len(re.findall('[^a-zA-Z0-9]if[\s\(]',code))
    forCount = len(re.findall('[^a-zA-Z0-9]for[\s\(]',code))
    whileCount = len(re.findall('[^a-zA-Z0-9]while[\s\(]',code))
    semiCount = len(re.findall('[^;\n];',code))
    switchCount = len(re.findall('[^a-zA-Z0-9]switch[\s\(]',code))
    caseCount = len(re.findall('[^a-zA-Z0-9]case[^:]*:',code))
    funcs = re.findall('(' + cppTypes+'\s+[a-zA-Z0-9]+[\(]{1}[^\)]*[\)]{1}[\n\s]*[\{]{1})',code)
    funcCount = len(funcs)

    #   only get logical AND OR inside control statements, switch cases
    matches = re.findall(controls+'\s*([^)]+)',code)
    logANDCount = 0
    logORCount = 0
    for match in matches:
        logANDCount += match.count('&&')
        logORCount += match.count('||')

    #   get all lines where variables are defined or initialized
    matches = re.findall('('+cppTypes+'\s+[^;\{\}]+;)',code)
    commas = 0
    equals = 0
    for match in matches:
        match = stripBrackets(match)
        commas += match.count(',')
        equals += match.count('=')

    #   LLOC calculation
    LLOC = equals + commas + semiCount + ifCount + forCount + whileCount + switchCount + funcCount

    cyclomaticComplexity = ifCount + whileCount + forCount + caseCount + logANDCount + logORCount

    #   debug print
    #print('program code after cleaning:\n')
    #print(code)
    #print

    #   aggregate output string
    outStr = ''
    outStr += str(commas) + ','
    outStr += str(equals) + ','
    outStr += str(ifCount)+ ','
    outStr += str(forCount)+ ','
    outStr += str(whileCount)+ ','
    outStr += str(semiCount)+ ','
    outStr += str(switchCount)+ ','
    outStr += str(caseCount)+ ','
    outStr += str(logANDCount)+ ','
    outStr += str(logORCount)+ ','
    outStr += str(PLOC)+ ','
    outStr += str(LLOC)+ ','
    outStr += str(cyclomaticComplexity) + '\n'

    return outStr

#   get list of cpp files
cppFiles = []
for file in glob.glob("*.cpp"):
    cppFiles.append(file)

#   clear outfile
    open(outputFilename, 'w').close()

for file in cppFiles:
    with open(outputFilename, "a") as outfile:
        #   The below line of code seeks to the end of the outfile
        outfile.seek( 0, 2 )
         
        #   get number of benchmark
        fileName = re.search('part([0-9]+)', file)
        fileNo = fileName.group(1)
        
        outfile.write(str(fileNo) + ',')
        outfile.write(getCounts(file))
