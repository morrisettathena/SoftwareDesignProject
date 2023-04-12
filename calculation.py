import pandas as pd
import globals as g

def calculateSectionData(secdata: dict):
    df: pd.DataFrame = secdata["data"]

    secdata["mean"] = round(df[g.GRADE_VALUE_HEADER].mean(), g.DEC_PREC)
    secdata["stddev"] = round(df[g.GRADE_VALUE_HEADER].std(ddof=0), g.DEC_PREC)
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
    newdata["mean"] = round(grp[g.GRADE_VALUE_HEADER].mean(), g.DEC_PREC)
    newdata["stddev"] = round(grp[g.GRADE_VALUE_HEADER].std(), g.DEC_PREC)
    newdata["numstudents"] = grp.shape[0]
    newdata["gradecounts"] = dict(grp["Grades"].value_counts())
    
    for sec in grpSecs:
        ztests[sec] = round((secData[sec]["mean"] - newdata["mean"])/newdata["stddev"], g.DEC_PREC)
    newdata["ztests"] = ztests

    return newdata