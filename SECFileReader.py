import pandas as pd

def getData(data): #converts data into a list
    list1 = []
    
    for x in range(6):
        list2 = data.iloc[x][0].split(",")
        list1 = list1 + list2
    return list1

def addData(data): #Converts the list into a pandas Dataframe
    data.pop(0)
    
    bruh3 = {"First Name":[], "Last Name":[], "ID":[], "Grades":[]}
    
    df = pd.DataFrame(bruh3)
    
    for x in range(0, len(data), 4):
        df.loc[x] = [data[x], data[x+1], data[x+2], data[x+3]]
    return df

bruh = pd.read_csv("COMSC110S21.SEC", sep=" ", header=None)

bruh2 = getData(bruh) 

df = addData(bruh2)
