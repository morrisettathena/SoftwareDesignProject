import reader
import globals as g
import calculation
import util as u

PRINTSECTIONSTATS = True
PRINTGROUPSTATS = True
DEBUG = True


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

def fetch(originalpath: str):
        runFile = originalpath[originalpath.rindex("/")+1:]
        path = originalpath[:originalpath.rindex("/")]

        grps: list = reader.readRunFile(u.constructPath(path, runFile))
        secs = []

        for grpFile in grps:
            grpSecs = reader.readGrpFile(u.constructPath(path, grpFile))
            for secFile in grpSecs:
                if secFile not in secs:
                    secs.append(secFile)

        secData = {}
        grpData = {}

        for secFile in secs:
                secData[secFile] = calculation.calculateSectionData(reader.readSecFile(u.constructPath(path, secFile)))

        for grpFile in grps:
            grpSecs = reader.readGrpFile(u.constructPath(path, grpFile))
            grpData[grpFile] = calculation.calculateGroupData(secData, grpSecs)

        return [secData, grpData]
