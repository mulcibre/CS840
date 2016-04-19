#   Samuel Gluss
#   4-10-2016
#   CSC 840
#   Jozo Dujmovic
#   Project 5: COCOMO calculator
#
####################################
from costDrivers import Drivers

LLOC = 1000

#   costDrivers.py contains all the cost drivers, modes, and levels of detail for COCOMO
drs = Drivers()

#   initial selection for all parameters is nominal or middle value
productAttr = [2,2,2]
computerAttr = [2,2,2,2]
personnelAttr = [2,2,2,2,2]
projectAttr = [2,2,2]
reqVolatility = 2
settings = productAttr+computerAttr+personnelAttr+projectAttr+[reqVolatility]

#   mode, level of detail
COCOparam = [2,2]

#   Compute m as composite of driver files
m = 1
m *= drs.computeM(settings)

#   Effort Formula
a = drs.COCOMOParam[COCOparam[0]][COCOparam[1]][0]
b = drs.COCOMOParam[COCOparam[0]][COCOparam[1]][1]

Effort = a * (LLOC ** b) * m

#   Productivity formula
Productivity = LLOC / Effort

#   Development Schedule Formula
devTime =