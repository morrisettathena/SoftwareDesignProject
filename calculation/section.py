import pandas as pd

def calculateSectionAvg(secdata: pd.DataFrame):
    return secdata["grades"].mean()

def getNumStudents(secdata: pd.DataFrame):
    return secdata

data = {
    "grades": [1, 3, 9, 14, 3.7, None]
}

df = pd.DataFrame(data)



s = "\"hello\""

print(s)

s = s.replace("\"", "")
print(s)