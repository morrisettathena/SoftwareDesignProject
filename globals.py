"""***************************************************************
globals.py

Written by: Danh Le, Thomas MacGregor, John Morriset, Will Hurwitz

Contains global values used by the program
***************************************************************"""

#___________File extensions___________________#
RUN_EXT = ".RUN"
GRP_EXT = ".GRP"
SEC_EXT = ".SEC"
STATS_EXT = ".STATS"
OTH_TYP = "other"
FILE_SEP = "/"

#___________MISC______________________________#
DEC_PREC = 2 #Decimal precision
LOW_Z_SIG = -2 #Lower bound on z-score
HIGH_Z_SIG = 2 #Higher bound on z-score

#___________Dataframe Headers_________________#
FIRST_NAME_HEADER = "First Name"
LAST_NAME_HEADER = "Last Name"
ID_HEADER = "ID"
GRADE_HEADER = "Grades"
GRADE_VALUE_HEADER = "GradeVal"

#___________Dictionary data fields____________#
MEAN_FIELD = "mean"
STDDEV_FIELD = "stddev"
NUM_STUD_FIELD = "numstudents"
GRADE_COUNTS_FIELD = "gradecounts"

#___________GRP dictionary data fields________#
SECTION_FIELD = "sections"
ZTEST_FIELD = "ztests"

#___________SEC dictionary data fields________#
DATA_FIELD = "data"
CREDIT_HOURS_FIELD = "creditHours"