#   Samuel Gluss
#   4-10-2016
#   CSC 840
#   Jozo Dujmovic
#   Project 5: COCOMO calculator
#
####################################
from costDrivers import Drivers
from getSWParams import SWParams
import re

gccPath = "../projectSpecs/gcc.txt"
linuxKernelPath = "../projectSpecs/linuxkernel.txt"
accessPath = "../projectSpecs/access.txt"
excelPath = "../projectSpecs/excel.txt"
onenotePath = "../projectSpecs/onenote.txt"
powerpointPath = "../projectSpecs/powerpoint.txt"
wordPath = "../projectSpecs/word.txt"

genericPath = "../projectSpecs/generic.txt"
#   costDrivers.py contains all the cost drivers, modes, and levels of detail for COCOMO
drs = Drivers()

#    development schedule parameters
r = 2.5
s = [0.38,0.35,0.32]

def exeSizeToKLLOC(sizeInBytes):
    retVal = (sizeInBytes - 188000) / (28.8314 * 1000)
    return retVal

def runCOCOMO(pathToConfig, filePos, KLLOC=-1, name=""):
    settings = SWParams(pathToConfig)

    if name == "":
        match = re.findall("(/)([^/.]+)(\.txt)",pathToConfig)
        name = match[0][1]
        #   make sure name is capitalized
        if name[0] >= 'a' and name[0] <= 'z':
            name = chr(ord(name[0]) - 32) + name[1:]

    #   Compute m as composite of driver files
    m = 1
    m *= drs.computeM(settings)

    #   Effort Formula
    #   Values come from COCOMO Parameters table, indexing on Mode and Level of Detail
    a = drs.COCOMOParam[settings.mode][settings.levelOfDetail][0]
    b = drs.COCOMOParam[settings.mode][settings.levelOfDetail][1]

    #   KLLOC may be passed in for test programs, otherwise it will be computed from the exe size
    #   Get LLOC from exe size using formula determined in project 3
    #   Adjust this by a factor of 1000 to get KLLOC
    if KLLOC == -1:
        KLLOC = exeSizeToKLLOC(settings.exeSize)
    else:
        #   set custom name as well, for generic projects
        settings.name = name

    Effort = a * (KLLOC ** b) * m

    #   Productivity formula
    Productivity = KLLOC / Effort

    #   Development Schedule Formula
    devTime = r * (Effort ** s[settings.mode])

    #   Average Staffing Formula
    staffCount = Effort / devTime

    cost = settings.salary * Effort

    #   round cost to nearest cent
    #   execute source code, writing results to outfile
    with open(outputFilename, "a") as outfile:
        #   The below line of code seeks to the end of the outfile
        outfile.seek(0, 2)
        outfile.write(",".join([str(filePos[0]), settings.name, name, str('%.2f'%cost), str('%.2f'%staffCount), str('%.2f'%devTime),str(KLLOC)]) + "\n")
        filePos[0]+=1

outputFilename = "../gnuplot/outfile.txt"
#   clear outfile
open(outputFilename, 'w').close()

#   Output file cursor
filePos = [0]

#   execute calculations
#   get results for typical projects
runCOCOMO(genericPath,filePos,2,"Small Project")
runCOCOMO(genericPath,filePos,8,"Intermediate Project")
runCOCOMO(genericPath,filePos,32,"Medium Project")
runCOCOMO(genericPath,filePos,128,"Large Project")
runCOCOMO(genericPath,filePos,512,"Very Large Project")

#   get results for specific projects
runCOCOMO(gccPath,filePos)
runCOCOMO(linuxKernelPath,filePos)

#   Results for Microsoft products
runCOCOMO(accessPath,filePos)
runCOCOMO(excelPath,filePos)
runCOCOMO(onenotePath,filePos)
runCOCOMO(powerpointPath,filePos)
runCOCOMO(wordPath,filePos)