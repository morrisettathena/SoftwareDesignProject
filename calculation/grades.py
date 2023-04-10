from decimal import Decimal, getcontext
from .globals import PREC

GRADEMAP = {
    "A": "4",
    "A-": "3.7",
    "B+": "3.3",
    "B": "3",
    "B-": "2.7",
    "C+": "2.3",
    "C": "2",
    "C-": "1.7",
    "D+": "1.3",
    "D": "1.0",
    "F": "0",
    "I": "N",
    "P": "N",
    "NP": "N",
    "W": "N"
}

def isRegistered(s: str):
    return s in GRADEMAP

def gradeToValue(s: str):

    getcontext().prec = PREC
    if not isRegistered(s):
        raise ValueError("not a registered grade type")
    val = GRADEMAP[s]
    if val == "N":
        return None
    return Decimal(val)

def isStandard(s: str):
    if not isRegistered(s):
        raise ValueError("not a registered grade type")
    return GRADEMAP[s] == "N"