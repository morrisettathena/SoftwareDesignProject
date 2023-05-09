"""***************************************************************
calculation.py

Written by: Danh Le, Thomas MacGregor, John Morriset, Will Hurwitz

Calculation module.  File responsible for performing calculations
on read-in data from read.py.  Accomplished using pandas dataframes
***************************************************************"""

import pandas as pd
import globals as g

def calculateSectionData(secdata: dict):
    """
    Returns a dictionary containing all statistical information
    about a given section.
    """
    df: pd.DataFrame = secdata["data"]
    secdata["mean"] = round(df[g.GRADE_VALUE_HEADER].mean(), g.DEC_PREC)
    secdata["stddev"] = round(df[g.GRADE_VALUE_HEADER].std(ddof=1), g.DEC_PREC)
    secdata["numstudents"] = df.shape[0]
    secdata["gradecounts"] = dict(df['Grades'].value_counts())

    return secdata

def calculateGroupData(secData: dict, grpSecs: list):
    """
    Returns a dictionary containing all statistical information
    about a given group.\n
    secData:  Complete list of data calculated from calculateSectionData()
    grpSecs:  List of sections the group contains
    """
    newdata = {} #data to be returned
    ztests = {} #Section to z-test mapping
    grp = { #temporary pandas dataframe used to calculate group statistics
        g.FIRST_NAME_HEADER:[], 
        g.LAST_NAME_HEADER:[], 
        g.ID_HEADER:[], 
        g.GRADE_HEADER:[], 
        g.GRADE_VALUE_HEADER:[]
    }
    grp = pd.DataFrame()

    for sec in grpSecs: #Form grp dataframe
        grp = pd.concat([secData[sec]["data"], grp])

    newdata["sections"] = grpSecs
    newdata["mean"] = round(grp[g.GRADE_VALUE_HEADER].mean(), g.DEC_PREC)
    newdata["stddev"] = round(grp[g.GRADE_VALUE_HEADER].std(), g.DEC_PREC)
    newdata["numstudents"] = grp.shape[0]
    newdata["gradecounts"] = dict(grp["Grades"].value_counts())
    
    for sec in grpSecs: #Z-test calculation.
        ztests[sec] = round((secData[sec]["mean"] - newdata["mean"])/newdata["stddev"], g.DEC_PREC)
    newdata["ztests"] = ztests

    return newdata
