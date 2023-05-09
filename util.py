"""***************************************************************
util.py

Written by: Danh Le, Thomas MacGregor, John Morriset, Will Hurwitz

File which contains utility functions for use by the program.

***************************************************************"""

import globals as g

# Mapping of grades to GPA score.
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

def isRegistered(s: str):
    """
    Function which determines if a string is a valid grade type
    """
    return s in GRADEMAP

def gradeToValue(s: str):
    """
    Function which converts a valid grade type to its GPA equivalent
    """
    if not isRegistered(s):
        raise ValueError("not a registered grade type")
    return GRADEMAP[s]

def constructPath(path: str, filename: str):
    """
    Function which takes a directory and filename and constructs their
    path.
    """
    return path + g.FILE_SEP + filename

def getOrder(s: str):
    """
    Function which orders the GradeMap based on GPA.  If it is a 
    non-standard grade, like P, return -1 to indicate lowest priority
    """
    if not isRegistered(s):
        raise ValueError("not a registered grade type")
    else:
        val = GRADEMAP[s]
        if val == None:
            val = -1.0
        return val
    