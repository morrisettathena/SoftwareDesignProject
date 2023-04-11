import pandas as pd
from .globals import *
from util import *



def getSecData(data: pd.DataFrame): #converts data into a list
    list1 = []
    
    for x in range(data.shape[0]):
        list2 = data.iloc[x][0].split(",")
        list2 = [x.replace("\"", "") for x in list2]
        list1 = list1 + list2

    return list1

def formatSecData(data: pd.DataFrame): #Converts the list into a pandas Dataframe
    data.pop(0)
    bruh3 = {FIRST_NAME_HEADER:[], LAST_NAME_HEADER:[], ID_HEADER:[], GRADE_HEADER:[], GRADE_VALUE_HEADER:[]}
    df = pd.DataFrame(bruh3)
    for x in range(0, len(data), 4):
        df.loc[int(x/4+1)] = [data[x].strip(), data[x+1].strip(), data[x+2].strip(), data[x+3].strip(), gradeToValue(data[x+3])]
    return df

def readSecData(filename: str):
    bruh = pd.read_csv(filename, sep=" ", header=None)
    creditHours = bruh.iloc[0][1]
    bruh2 = getSecData(bruh)
    df = formatSecData(bruh2)

    secData = {
        "data": df,
        "creditHours": creditHours
    }
    return secData

def readGrpData(filename: str):
    contents = open(filename, 'r')
    data = contents.readlines()
    data.pop(0)
    data = [item.strip() for item in data if not item.isspace()]
    return data

def readRunData(filename: str):
    contents = open(filename, 'r')
    data = contents.readlines()
    data.pop(0)
    data = [item.strip() for item in data if not item.isspace()]
    return data

