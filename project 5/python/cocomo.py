#   Samuel Gluss
#   4-10-2016
#   CSC 840
#   Jozo Dujmovic
#   Project 5: COCOMO calculator
#
####################################
from costDrivers import Drivers
from getSWParams import SWParams

gccPath = "../projectSpecs/gcc.txt"
linuxKernelPath = "../projectSpecs/linuxkernel.txt"
#   costDrivers.py contains all the cost drivers, modes, and levels of detail for COCOMO
drs = Drivers()

#    development schedule parameters
r = 2.5
s = [0.38,0.35,0.32]

def runCOCOMO(pathToConfig):
    settings = SWParams(pathToConfig)

    #   Get LLOC from exe size using formula determined in project 3
    #   Adjust this by a factor of 1000 to get KLLOC
    KLLOC = (settings.exeSize - 188000) / (28.8314 * 1000)

    #   Compute m as composite of driver files
    m = 1
    m *= drs.computeM(settings)

    #   Effort Formula
    #   Values come from COCOMO Parameters table, indexing on Mode and Level of Detail
    a = drs.COCOMOParam[settings.mode][settings.levelOfDetail][0]
    b = drs.COCOMOParam[settings.mode][settings.levelOfDetail][1]

    Effort = a * (KLLOC ** b) * m

    #   Productivity formula
    Productivity = KLLOC / Effort

    #   Development Schedule Formula
    devTime = r * (Effort ** s[settings.mode])

    #   Average Staffing Formula
    staffCount = Effort / devTime

    cost = settings.salary * Effort

    #   round cost to nearest cent
    print " ".join(["The project", settings.name ,"will cost", '$' + str('%.2f'%cost), "to produce"])

#   execute calculations
runCOCOMO(gccPath)
runCOCOMO(linuxKernelPath)