"""***************************************************************
main.py

Written by: Danh Le, Thomas MacGregor, John Morriset, Will Hurwitz

File responsible for interfacing with the GUI and the calculation
and read modules.  Performs the fetch function, which
gets the necessary data from the specified path.

***************************************************************"""

import reader
import calculation
import util as u

def fetch(originalpath: str):
        """
        Function which calls the read and calculate modules and outputs
        dictionaries containing section and group data.\n
        originalpath: path to the run file
        """

        #split path into directory and run file path
        runFile = originalpath[originalpath.rindex("/")+1:]
        path = originalpath[:originalpath.rindex("/")]

        #Read the run file, get the list of groups
        grps: list = reader.readRunFile(u.constructPath(path, runFile))
        secs = []

        #Get list of section files
        for grpFile in grps:
            grpSecs = reader.readGrpFile(u.constructPath(path, grpFile)) #read grp
            for secFile in grpSecs:
                if secFile not in secs: #only append if the file hasn't appeared, no duplicates
                    secs.append(secFile)

        secData = {}
        grpData = {}

        #Form dictionary maping section file name to section file data
        for secFile in secs:
                secData[secFile] = calculation.calculateSectionData(reader.readSecFile(u.constructPath(path, secFile)))

        #Form dictionary mapping group file name to group file mapping
        for grpFile in grps:
            grpSecs = reader.readGrpFile(u.constructPath(path, grpFile)) #Get list of group files from grp data
            grpData[grpFile] = calculation.calculateGroupData(secData, grpSecs)

        return [secData, grpData]
