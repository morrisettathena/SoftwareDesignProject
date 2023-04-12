import pandas as pd
import globals as g

def calculateSectionData(secdata: dict):
    df: pd.DataFrame = secdata["data"]

    secdata["mean"] = df[g.GRADE_VALUE_HEADER].mean()
    secdata["stddev"] = df[g.GRADE_VALUE_HEADER].std(ddof=0)
    secdata["numstudents"] = df.shape[0]
    secdata["gradecounts"] = dict(df['Grades'].value_counts())

    return secdata

def calculateGroupData(secData: dict, grpSecs: list):
    newdata = {}
    ztests = {}
    grp = {
        g.FIRST_NAME_HEADER:[], 
        g.LAST_NAME_HEADER:[], 
        g.ID_HEADER:[], 
        g.GRADE_HEADER:[], 
        g.GRADE_VALUE_HEADER:[]
    }
    grp = pd.DataFrame()

    for sec in grpSecs:
        grp = pd.concat([secData[sec]["data"], grp])

    newdata["sections"] = grpSecs
    newdata["mean"] = grp[g.GRADE_VALUE_HEADER].mean()
    newdata["stddev"] = grp[g.GRADE_VALUE_HEADER].std()
    newdata["numstudents"] = grp.shape[0]
    newdata["gradecounts"] = dict(grp["Grades"].value_counts())
    
    for sec in grpSecs:
        ztests[sec] = (secData[sec]["mean"] - newdata["mean"])/newdata["stddev"]
    newdata["ztests"] = ztests

    return newdata