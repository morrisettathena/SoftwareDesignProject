"""***************************************************************
reader.py

Written by: Danh Le, Thomas MacGregor, John Morriset, Will Hurwitz

Reading module.  Contains functions that read and format data from
.RUN, .GRP, and .SEC files.
***************************************************************"""

import pandas as pd
import globals as g
import os
import util as u

def formatSecData(data: pd.DataFrame): #Converts the list into a pandas Dataframe
    """
    Function which formats a dataframe so that data can be used cleanly
    """
    list1 = []
    
    #Split data by commas, and remove any quotations for easy readability
    for x in range(data.shape[0]):
        list2 = data.iloc[x][0].split(",")
        list2 = [x.replace("\"", "") for x in list2]
        list1 = list1 + list2

    list1.pop(0) #Pop first item, the headers
    bruh3 = {g.FIRST_NAME_HEADER:[], g.LAST_NAME_HEADER:[], g.ID_HEADER:[], g.GRADE_HEADER:[], g.GRADE_VALUE_HEADER:[]}
    df = pd.DataFrame(bruh3) #new data frame
    for x in range(0, len(list1), 4): #Insert insert items formatted in correct order into dataframe
        df.loc[int(x/4+1)] = [list1[x].strip(), list1[x+1].strip(), list1[x+2].strip(), list1[x+3].strip(), u.gradeToValue(list1[x+3])]
    return df

def readSecFile(filename: str):
    """
    Reads a section file and returns a dictionary with the raw data
    from the SEC file
    """
    bruh = pd.read_csv(filename, sep=" ", header=None) #read in the filename

    creditHours = bruh.iloc[0][len(bruh.iloc[0])-1]
    df = formatSecData(bruh)

    secData = {
        "data": df,
        "creditHours": creditHours
    }
    return secData

def readGrpFile(filename: str):
    """
    Function which reads in a .GRP file and returns a list of .SEC
    files that it contains
    """
    contents = open(filename, 'r')
    data = contents.readlines()
    data.pop(0) #Remove the header line
    data = [item.strip() for item in data if not item.isspace()] #Don't include whitespace
    return data

def readRunFile(filename: str):
    """
    Function which reads in a .RUN file and returns a list of .GRP
    files that it contains
    """
    contents = open(filename, 'r')
    data = contents.readlines()
    data.pop(0) #Remove the header line
    data = [item.strip() for item in data if not item.isspace()] #Don't include whitespace
    return data

def getFileType(filename: str):
    """
    Returns the type of file associated with the program
    """
    if filename.endswith(g.RUN_EXT):
        return g.RUN_EXT
    elif filename.endswith(g.GRP_EXT):
        return g.GRP_EXT
    elif filename.endswith(g.SEC_EXT):
        return g.SEC_EXT
    else:
        return g.OTH_TYP
    
def getFolderData(path: str):
    """
    Function which returns a dictionary containing all 
    of the various types of files in a folder
    """
    files_list = os.listdir(path)

    files = {
        g.RUN_EXT: [],
        g.GRP_EXT: [],
        g.SEC_EXT: [],
        g.OTH_TYP: [],
    }

    for file in files_list:
        fileType = getFileType(u.constructPath(path, file))
        files[fileType].append(file)

    return files

