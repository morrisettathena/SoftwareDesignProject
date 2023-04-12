import globals as g

GRADEMAP = {
    "A": 4,
    "A-": 3.67,
    "B+": 3.33,
    "B": 3,
    "B-": 2.67,
    "C+": 2.33,
    "C": 2,
    "C-": 1.67,
    "D+": 1.33,
    "D": 1.0,
    "F": 0,
    "I": None,
    "P": None,
    "NP": None,
    "W": None
}

def getEmptyGradeCounts():
    gradeCounts = {}
    for item in GRADEMAP.keys():
        gradeCounts[item] = 0
    return gradeCounts

def isRegistered(s: str):
    return s in GRADEMAP

def gradeToValue(s: str):
    if not isRegistered(s):
        raise ValueError("not a registered grade type")
    return GRADEMAP[s]

def isStandard(s: str):
    if not isRegistered(s):
        raise ValueError("not a registered grade type")
    return GRADEMAP[s] == "N"

def constructPath(path: str, filename: str):
    return path + g.FILE_SEP + filename
    