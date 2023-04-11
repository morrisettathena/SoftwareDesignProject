import pandas as pd
import reader.globals as readerGlobals
from util import GRADEMAP, getEmptyGradeCounts

def calculateSectionData(secdata: dict):
    df: pd.DataFrame = secdata["data"]

    secdata["mean"] = df[readerGlobals.GRADE_VALUE_HEADER].mean()
    secdata["stddev"] = df[readerGlobals.GRADE_VALUE_HEADER].std(ddof=0)
    secdata["numstudents"] = df.shape[0]
    secdata["gradecounts"] = dict(df['Grades'].value_counts())

    return secdata

def calculateGroupData(secData: dict, grpSecs: list):
    newdata = {}
    ztests = {}
    grp = {
        readerGlobals.FIRST_NAME_HEADER:[], 
        readerGlobals.LAST_NAME_HEADER:[], 
        readerGlobals.ID_HEADER:[], 
        readerGlobals.GRADE_HEADER:[], 
        readerGlobals.GRADE_VALUE_HEADER:[]
    }
    grp = pd.DataFrame()

    for sec in grpSecs:
        grp = pd.concat([secData[sec]["data"], grp])

    newdata["sections"] = grpSecs
    newdata["mean"] = grp[readerGlobals.GRADE_VALUE_HEADER].mean()
    newdata["stddev"] = grp[readerGlobals.GRADE_VALUE_HEADER].std()
    newdata["numstudents"] = grp.shape[0]
    newdata["gradecounts"] = dict(grp["Grades"].value_counts())
    
    for sec in grpSecs:
        ztests[sec] = (secData[sec]["mean"] - newdata["mean"])/newdata["stddev"]
    newdata["ztests"] = ztests

    return newdata