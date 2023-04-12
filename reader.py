import pandas as pd
import globals as g
import os
import util as u

def getSecData(data: pd.DataFrame): #converts data into a list
    list1 = []
    
    for x in range(data.shape[0]):
        list2 = data.iloc[x][0].split(",")
        list2 = [x.replace("\"", "") for x in list2]
        list1 = list1 + list2

    return list1

def formatSecData(data: pd.DataFrame): #Converts the list into a pandas Dataframe
    data.pop(0)
    bruh3 = {g.FIRST_NAME_HEADER:[], g.LAST_NAME_HEADER:[], g.ID_HEADER:[], g.GRADE_HEADER:[], g.GRADE_VALUE_HEADER:[]}
    df = pd.DataFrame(bruh3)
    for x in range(0, len(data), 4):
        df.loc[int(x/4+1)] = [data[x].strip(), data[x+1].strip(), data[x+2].strip(), data[x+3].strip(), u.gradeToValue(data[x+3])]
    return df

def readSecFile(filename: str):
    bruh = pd.read_csv(filename, sep=" ", header=None)

    creditHours = bruh.iloc[0][len(bruh.iloc[0])-1]
    bruh2 = getSecData(bruh)
    df = formatSecData(bruh2)

    secData = {
        "data": df,
        "creditHours": creditHours
    }
    return secData

def readGrpFile(filename: str):
    contents = open(filename, 'r')
    data = contents.readlines()
    data.pop(0)
    data = [item.strip() for item in data if not item.isspace()]
    return data

def readRunFile(filename: str):
    contents = open(filename, 'r')
    data = contents.readlines()
    data.pop(0)
    data = [item.strip() for item in data if not item.isspace()]
    return data

def getFileType(filename: str):
    if filename.endswith(g.RUN_EXT):
        return g.RUN_EXT
    elif filename.endswith(g.GRP_EXT):
        return g.GRP_EXT
    elif filename.endswith(g.SEC_EXT):
        return g.SEC_EXT
    else:
        return g.OTH_TYP
    
def getFolderData(path: str):
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

