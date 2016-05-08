class SWParams:
    name = ""
    exeSize = -1
    salary = -1
    requiredSoftwareReliabilitySetting = -1
    dbSizeSetting = -1
    productComplexitySetting = -1
    executionTimeConstraintSetting = -1
    mainStorageConstraintSetting = -1
    virtualMachineVolatilitySetting = -1
    computerTurnaroundTimeSetting = -1
    analystCapabilitiesSetting = -1
    applicationsExperienceSetting = -1
    programmerCapabilitySetting = -1
    virtualMachineExperienceSetting = -1
    programmingLanguageExperienceSetting = -1
    useOfModernProgrammingPracticesSetting = -1
    useOfSoftwareToolsSetting = -1
    requiredDevelopmentScheduleSetting = -1
    requirementsVolatilitySetting = -1
    levelOfDetail = -1
    mode = -1

    #   Constructor
    def __init__(self, filepath):

        with open(filepath, 'r') as file:
            # read a list of lines into source code
            txtData = file.readlines()

        #   get name of software (slice eliminates newline at end)
        self.name = txtData[2][:-1]

        #   get size of program
        self.exeSize = int(txtData[5][:-1])

        #   Get salary per month of software engineers (devs? people whacking on computers?)
        self.salary = int(txtData[8][:-1])

        #   get m vars
        levelOfDetail = txtData[11][:-1]
        #   check for valid Level of Detail
        if levelOfDetail != '0' and levelOfDetail != '1' and levelOfDetail != '2':
            print "invalid level of detail entered in " + filepath
            exit(-1)

        self.levelOfDetail = int(levelOfDetail)

        #   get mode
        mode = txtData[14][:-1]
        #   By skipping the first letter, this will work with whatever case is used in the input file
        if mode.count("rganic"):
            self.mode = 0
        elif mode.count("emidetached"):
            self.mode = 1
        elif mode.count("mbedded"):
            self.mode = 2
        else:
            print "Invalid entry for mode in file " + filepath





        #   file search cursor
        fileCursor = [0]

        #   get m values as indicated by level of detail
        if levelOfDetail == '1' or levelOfDetail == '2':
            self.requiredSoftwareReliabilitySetting = parseMVal(txtData, fileCursor, "m1. requiredSoftwareReliability")
            self.dbSizeSetting = parseMVal(txtData, fileCursor, "m2. dbSize")
            self.productComplexitySetting = parseMVal(txtData, fileCursor, "m3. productComplexity")
            self.executionTimeConstraintSetting = parseMVal(txtData, fileCursor, "m4. executionTimeConstraint")
            self.mainStorageConstraintSetting = parseMVal(txtData, fileCursor, "m5. mainStorageConstraint")
            self.virtualMachineVolatilitySetting = parseMVal(txtData, fileCursor, "m6. virtualMachineVolatility")
            self.computerTurnaroundTimeSetting = parseMVal(txtData, fileCursor, "m7. computerTurnaroundTime")
            self.analystCapabilitiesSetting = parseMVal(txtData, fileCursor, "m8. AnalystCapabilities")
            self.applicationsExperienceSetting = parseMVal(txtData, fileCursor, "m9. applicationsExperience")
            self.programmerCapabilitySetting = parseMVal(txtData, fileCursor, "m10. programmerCapability")
            self.virtualMachineExperienceSetting = parseMVal(txtData, fileCursor, "m11. virtualMachineExperience")
            self.programmingLanguageExperienceSetting = parseMVal(txtData, fileCursor, "m12. programmingLanguageExperience")
            self.useOfModernProgrammingPracticesSetting = parseMVal(txtData, fileCursor, "m13. useOfModernProgrammingPractices")
            self.useOfSoftwareToolsSetting = parseMVal(txtData, fileCursor, "m14. useOfSoftwareTools")
            self.requiredDevelopmentScheduleSetting = parseMVal(txtData, fileCursor, "m15. requiredDevelopmentSchedule")
        if levelOfDetail == '2':
            self.requirementsVolatilitySetting = parseMVal(txtData, fileCursor, "m16. requirementsVolatility")

def parseMVal(file, cursor, anchor):
    lineNo = getLineOfData(file, cursor, anchor)

    #   in order of likelihood, slice newline off
    lineData = file[lineNo][:-1]
    if lineData == "nominal":
        return 2
    elif lineData == "low":
        return 1
    elif lineData == "high":
        return 3
    elif lineData == "very low":
        return 0
    elif lineData == "very high":
        return 4
    elif lineData == "extra high":
        return 5
    else:
        print "Failed at line " + str(lineNo)
        exit(-1)

def getLineOfData(file, cursor, anchor):
    #   scan for anchor, if found return next line which should have data
    for i in range(cursor[0], len(file)):
        if file[i].count(anchor):
            cursor[0] = i + 1
            return cursor[0]

    #   couldn't find anchor, something bad happened
    print "could not find string to match: " + anchor
    exit(-1)
