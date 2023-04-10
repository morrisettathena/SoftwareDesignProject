import pandas as pd

def getSecData(data: pd.DataFrame): #converts data into a list
    list1 = []
    
    for x in range(data.shape[0]):
        list2 = data.iloc[x][0].split(",")
        list2 = [x.replace("\"", "") for x in list2]
        list1 = list1 + list2

    return list1

def formatSecData(data: pd.DataFrame): #Converts the list into a pandas Dataframe
    data.pop(0)
    print(data[0])
    
    bruh3 = {"First Name":[], "Last Name":[], "ID":[], "Grades":[]}
    
    df = pd.DataFrame(bruh3)
    
    for x in range(0, len(data), 4):
        df.loc[x] = [data[x], data[x+1], data[x+2], data[x+3]]
    return df

def readSecData(filename: str):
    bruh = pd.read_csv(filename, sep=" ", header=None)
    bruh2 = getSecData(bruh)
    df = formatSecData(bruh2)
    return df

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

print(readRunData("./data/TESTRUN.RUN"))