import reader
import globals as g
import calculation
import util as u
from collections import OrderedDict

PRINTSECTIONSTATS = True
PRINTGROUPSTATS = True
DEBUG = True

def getFolder():
    if DEBUG:
        return "./data"
    else:
        return input("Select folder")
    
def selectRun(runData: list):
    while True:
        print("Select run file: ")
        
        print(", ".join(runData))
        runFile = input("Choice (name or number):")
        if runFile.isdigit():
            index = int(runFile)
            if index < len(runData) and index >= 0:
                return runData[index]
            else:
                print("index out of bounds")
        else:

            if runFile not in runData:
                print("not a valid run file")
            else:
                return runFile
        print()
        
def checkGrps(folderData: dict, grps: list):

    for grp in grps:
        if grp not in folderData[g.GRP_EXT]:
            return False
    return True
        
def checkSecs(folderData: dict, secs: list):
    for sec in secs:
        if sec not in folderData[g.SEC_EXT]:
            return False
    return True

def useSameFolder():
    return input("Use same folder? y/n").lower().startswith("y")

def printSecStats(secData: dict):
    for item in secData:
        print("\n" + item + " stats:")
        for i in secData[item]:
            if type(secData[item][i]) == dict:
                print(i + ": " + str(OrderedDict(sorted(secData[item][i].items()))))
            else:
                print(i + ": " + str(secData[item][i]))

        print("*"*30)

def printGrpStats(grpData: dict):
    for item in grpData:
        print("\n" + item + " stats:")
        for i in grpData[item]:
            if type(grpData[item][i]) == dict:
                print(i + ": " + str(OrderedDict(sorted(grpData[item][i].items()))))
            else:
                print(i + ": " + str(grpData[item][i]))
        print("*"*30)

def fetch(originalpath: str):
        runFile = originalpath[originalpath.rindex("/")+1:]
        path = originalpath[:originalpath.rindex("/")]

        grps: list = reader.readRunFile(u.constructPath(path, runFile))
        secs = []

        #if not checkGrps(folderData, grps):
            #print("Could not use Run file, a group from the Run file was not found in folder\n")
            #break

        for grpFile in grps:
            grpSecs = reader.readGrpFile(u.constructPath(path, grpFile))
            for secFile in grpSecs:
                if secFile not in secs:
                    secs.append(secFile)

        #if not checkSecs(folderData, secs):
            #print("Could not use Run file, a section from one of the Group files was not found in folder\n")
            #break

        secData = {}
        grpData = {}

        for secFile in secs:
                secData[secFile] = calculation.calculateSectionData(reader.readSecFile(u.constructPath(path, secFile)))

        for grpFile in grps:
            grpSecs = reader.readGrpFile(u.constructPath(path, grpFile))
            grpData[grpFile] = calculation.calculateGroupData(secData, grpSecs)

        return [secData, grpData]