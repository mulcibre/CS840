class Drivers:
    #   Product Attributes
    requiredSoftwareReliability = [0.75,0.88,1,1.15,1.4,0]
    dbSize = [0,0.94,1,1.08,1.16,0]
    productComplexity = [0.7,0.85,1,1.15,1.3,1.65]

    #   Computer Attributes
    executionTimeConstraint = [0,0,1,1.11,1.3,1.66]
    mainStorageConstraint = [0,0,1,1.06,1.21,1.56]
    virtualMachineVolatility = [0,0.87,1,1.15,1.3,0]
    computerTurnaroundTime = [0,0.87,1,1.07,1.15,0]

    #   Personnel Attributes
    analystCapabilities = [1.46,1.19,1,0.86,0.71,0]
    applicationsExperience = [1.29,1.13,1,0.91,0.82,0]
    programmerCapability = [1.42,1.17,1,0.86,0.7,0]
    virtualMachineExperience = [1.21,1.10,1,0.90,0,0]
    programmingLanguageExperience = [1.14,1.07,1,0.95,0,0]

    #   Project Attributes
    useOfModernProgrammingPractices = [1.24,1.10,1,0.91,0.82,0]
    useOfSoftwareTools = [1.24,1.10,1,0.91,0.83,0]
    requiredDevelopmentSchedule = [1.23,1.08,1,1.04,1.10,0]

    #   Defines how much the specifications of the product are expected to change
    requirementsVolatility = [0,0.91,1,0,0,1.62]

    # nesting level: [mode][Level of Detail][ai,bi]
    COCOMOParam = [[[2.4,1.05],[3.2,1.05],[2.6,1.08]],
                   [[3.0,1.12],[3.0,1.12],[2.9,1.12]],
                   [[3.6,1.2],[2.8,1.2],[2.9,1.2]]]

    def computeM(self, settings):
        mVal = 1
        if settings.levelOfDetail != 0:
            mVal *= self.multiplyIfValid(self.requiredSoftwareReliability,settings.requiredSoftwareReliabilitySetting,0)
            mVal *= self.multiplyIfValid(self.dbSize,settings.dbSizeSetting,1)
            mVal *= self.multiplyIfValid(self.productComplexity,settings.productComplexitySetting,2)
            mVal *= self.multiplyIfValid(self.executionTimeConstraint,settings.executionTimeConstraintSetting,3)
            mVal *= self.multiplyIfValid(self.mainStorageConstraint,settings.mainStorageConstraintSetting,4)
            mVal *= self.multiplyIfValid(self.virtualMachineVolatility,settings.virtualMachineVolatilitySetting,5)
            mVal *= self.multiplyIfValid(self.computerTurnaroundTime,settings.computerTurnaroundTimeSetting,6)
            mVal *= self.multiplyIfValid(self.analystCapabilities,settings.analystCapabilitiesSetting,7)
            mVal *= self.multiplyIfValid(self.applicationsExperience,settings.applicationsExperienceSetting,8)
            mVal *= self.multiplyIfValid(self.programmerCapability,settings.programmerCapabilitySetting,9)
            mVal *= self.multiplyIfValid(self.virtualMachineExperience,settings.virtualMachineExperienceSetting,10)
            mVal *= self.multiplyIfValid(self.programmingLanguageExperience,settings.programmingLanguageExperienceSetting,11)
            mVal *= self.multiplyIfValid(self.useOfModernProgrammingPractices,settings.useOfModernProgrammingPracticesSetting,12)
            mVal *= self.multiplyIfValid(self.useOfSoftwareTools,settings.useOfSoftwareToolsSetting,13)
            mVal *= self.multiplyIfValid(self.requiredDevelopmentSchedule,settings.requiredDevelopmentScheduleSetting,14)
            if settings.levelOfDetail == 2:
                mVal *= self.multiplyIfValid(self.requirementsVolatility,settings.requirementsVolatilitySetting,15)
        return mVal

    #   drunk sam is not amused, why is there not a comment describing wtf this does??
    #   Hari says hi!
    def multiplyIfValid(self,driverArr, setting, index):
        if driverArr[setting] == 0:
            print "Invalid setting for m" + str(index)
            exit(-1)
        else:
            return driverArr[setting]