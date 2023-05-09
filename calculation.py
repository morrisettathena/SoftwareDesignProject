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
    df: pd.DataFrame = secdata[g.DATA_FIELD]
    secdata[g.MEAN_FIELD] = round(df[g.GRADE_VALUE_HEADER].mean(), g.DEC_PREC)
    secdata[g.STDDEV_FIELD] = round(df[g.GRADE_VALUE_HEADER].std(ddof=1), g.DEC_PREC)
    secdata[g.NUM_STUD_FIELD] = df.shape[0]
    secdata[g.GRADE_COUNTS_FIELD] = dict(df[g.GRADE_HEADER].value_counts())

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
        grp = pd.concat([secData[sec][g.DATA_FIELD], grp])

    newdata[g.SECTION_FIELD] = grpSecs
    newdata[g.MEAN_FIELD] = round(grp[g.GRADE_VALUE_HEADER].mean(), g.DEC_PREC)
    newdata[g.STDDEV_FIELD] = round(grp[g.GRADE_VALUE_HEADER].std(), g.DEC_PREC)
    newdata[g.NUM_STUD_FIELD] = grp.shape[0]
    newdata[g.GRADE_COUNTS_FIELD] = dict(grp[g.GRADE_HEADER].value_counts())
    
    for sec in grpSecs: #Z-test calculation.
        ztests[sec] = round((secData[sec][g.MEAN_FIELD] - newdata[g.MEAN_FIELD])/newdata[g.STDDEV_FIELD], g.DEC_PREC)
    newdata[g.ZTEST_FIELD] = ztests

    return newdata
