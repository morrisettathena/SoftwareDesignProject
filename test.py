"""***************************************************************
test.py

Written by: Danh Le, Thomas MacGregor, John Morriset, Will Hurwitz

File which contains the testing portion of the program.

***************************************************************"""

import unittest
import calculation
import main
import reader
import util
import globals as g
import pandas as pd
import io
import random

class TestCalculationMethods(unittest.TestCase):

    """Code adapted from https://stackoverflow.com/questions/22604564/create-pandas-dataframe-from-a-string"""
    def testCalculateSectionData(self):
        print("\nTESTING calculateSectionData METHOD")

        data1 = """{0};{1}
        D;1.0
        C;2.0
        B;3.0
        A;4.0
        A-;3.67
        I;
        W;
        """.format(g.GRADE_HEADER, g.GRADE_VALUE_HEADER)

        data2 = """{0};{1}
        B-;2.67
        A;4
        A-;3.67
        B+;3.33
        W;
        F;0
        D;1.0
        W;
        NP;
        NP;
        W;
        P;
        C-;1.67
        B-;2.67
        C+;2.33
        """.format(g.GRADE_HEADER, g.GRADE_VALUE_HEADER)

        df1 = pd.read_csv(io.StringIO(data1), sep = ";")
        sec1data = {g.DATA_FIELD: df1}
        dict1 = calculation.calculateSectionData(sec1data)

        #test to make sure that values are the same as independently calculated values
        DATA1MEAN = 2.73
        DATA1STDDEV = 1.23
        DATA1STUDCOUNT = 7
        self.assertAlmostEqual(dict1[g.MEAN_FIELD], DATA1MEAN)
        self.assertAlmostEqual(dict1[g.STDDEV_FIELD], DATA1STDDEV)
        self.assertEqual(dict1[g.NUM_STUD_FIELD], DATA1STUDCOUNT)
        print("data 1: program results vs independently calculated:")
        print("Mean:         {0} = {1}".format(dict1[g.MEAN_FIELD], DATA1MEAN))
        print("Stddev:       {0} = {1}".format(dict1[g.STDDEV_FIELD], DATA1STDDEV))
        print("Num_students: {0} = {1}".format(dict1[g.NUM_STUD_FIELD], DATA1STUDCOUNT))

        df2 = pd.read_csv(io.StringIO(data2), sep = ";")
        sec2data = {g.DATA_FIELD: df2}
        dict2 = calculation.calculateSectionData(sec2data)

        #test to make sure that values are the same as independently calculated values
        DATA2MEAN = 2.37
        DATA2STDDEV = 1.30
        DATA2STUDCOUNT = 15
        self.assertAlmostEqual(dict2[g.MEAN_FIELD], DATA2MEAN)
        self.assertAlmostEqual(dict2[g.STDDEV_FIELD], DATA2STDDEV)
        self.assertEqual(dict2[g.NUM_STUD_FIELD], DATA2STUDCOUNT)

        print("data 2: program results vs independently calculated:")
        print("Mean:         {0} = {1}".format(dict2[g.MEAN_FIELD], DATA2MEAN))
        print("Stddev:       {0} = {1}".format(dict2[g.STDDEV_FIELD], DATA2STDDEV))
        print("Num_students: {0} = {1}".format(dict2[g.NUM_STUD_FIELD], DATA2STUDCOUNT))

        print("calculateSectionData IS SUCCESFUL\n")
        
    def testCalculateGroupData(self):
        print("\nTESTING calculateGroupData METHOD")

        sec1 = """Grades;GradeVal
        NP;
        B-;2.67
        C;2
        P;
        B-;2.67
        A;4
        C-;1.67
        C+;2.33
        I;
        D;1.0
        """

        sec2 = """Grades;GradeVal
        B+;3.33
        I;
        C+;2.33
        C-;1.67
        C-;1.67
        D;1.0
        B-;2.67
        D;1.0
        D;1.0
        C+;2.33
        C+;2.33
        C+;2.33
        A;4
        B;3
        A;4
        A-;3.67
        F;0
        I;
        D+;1.33
        P;
        C+;2.33
        B;3
        A;4
        """

        sec3 = """Grades;GradeVal
        D+;1.33
        A-;3.67
        F;0
        D+;1.33
        B+;3.33
        C+;2.33
        B-;2.67
        NP;
        A;4
        A-;3.67
        B-;2.67
        P;
        I;
        B+;3.33
        """

        sec1df = pd.read_csv(io.StringIO(sec1), sep = ";")
        sec2df = pd.read_csv(io.StringIO(sec2), sep = ";")
        sec3df = pd.read_csv(io.StringIO(sec3), sep = ";")

        sec1dict = {g.DATA_FIELD: sec1df}
        sec2dict = {g.DATA_FIELD: sec2df}
        sec3dict = {g.DATA_FIELD: sec3df}

        sec1dict = calculation.calculateSectionData(sec1dict)
        sec2dict = calculation.calculateSectionData(sec2dict)
        sec3dict = calculation.calculateSectionData(sec3dict)

        sections = {
            "sec1": sec1dict,
            "sec2": sec2dict,
            "sec3": sec3dict
        }

        group_sections = ["sec1", "sec2", "sec3"]
        newdata = calculation.calculateGroupData(sections, group_sections)

        #test to make sure that values are the same as independendently calculated values
        DATAMEAN = 2.41
        DATASTDDEV = 1.11
        DATASTUDCOUNT = 47
        DATAZTEST1 = -0.07
        DATAZTEST2 = -0.05
        DATAZTEST3 = 0.15
        self.assertAlmostEqual(newdata[g.MEAN_FIELD], DATAMEAN)
        self.assertAlmostEqual(newdata[g.STDDEV_FIELD], DATASTDDEV)
        self.assertEqual(newdata[g.NUM_STUD_FIELD], DATASTUDCOUNT)
        self.assertAlmostEqual(newdata[g.ZTEST_FIELD]["sec1"], DATAZTEST1)
        self.assertAlmostEqual(newdata[g.ZTEST_FIELD]["sec2"], DATAZTEST2)
        self.assertAlmostEqual(newdata[g.ZTEST_FIELD]["sec3"],  DATAZTEST3)

        print("program results vs independently calculated:")
        print("Mean:         {0} = {1}".format(newdata[g.MEAN_FIELD], DATAMEAN))
        print("Stddev:       {0} = {1}".format(newdata[g.STDDEV_FIELD], DATASTDDEV))
        print("Num_students: {0} = {1}".format(newdata[g.NUM_STUD_FIELD], DATASTUDCOUNT))
        print("Z-test 1:     {0} = {1}".format(newdata[g.ZTEST_FIELD]["sec1"], DATAZTEST1))
        print("Z-test 2:     {0} = {1}".format(newdata[g.ZTEST_FIELD]["sec2"], DATAZTEST2))
        print("Z-test 3:     {0} = {1}".format(newdata[g.ZTEST_FIELD]["sec3"], DATAZTEST3))

        print("calculateGroupData IS SUCCESFUL\n")

class TestUtilMethods(unittest.TestCase):

    def testIsRegistered(self):
        print("\nTESTING isRegistered METHOD")
        for item in util.GRADEMAP.keys():
            self.assertTrue(util.isRegistered(item))
            print("Grade {0} is recognized".format(item))
        self.assertFalse(util.isRegistered("erawoier"))
        self.assertFalse(util.isRegistered("+"))
        self.assertFalse(util.isRegistered("-"))
        print("Grade \"erawoier\" sucessfully discarded")
        print("Grade \"+\" sucessfully discarded")
        print("Grade \"-\" sucessfully discarded")
        print("isRegistered IS SUCCESFUL\n")

    def testGradeToValue(self):
        print("\nTESTING gradeToValue METHOD")
        print("program results vs map:")
        for item in util.GRADEMAP.items():
            util.GRADEMAP[item[0]] == item[1]
            print("{0} = {1}".format(item[0], util.GRADEMAP[item[0]]))
        print("gradeToValue IS SUCCESFUL\n")

    def testConstructPath(self):
        print("\nTESTING constructPath METHOD")
        path = "testing"
        file = "x"
        pathconstruct = util.constructPath(path, file)

        EXPLICIT_STRING = "testing/x"
        self.assertEqual(EXPLICIT_STRING, pathconstruct)
        print("program results vs explicit string:")
        print("{0} = {1}".format(EXPLICIT_STRING, pathconstruct))
        print("constructPath IS SUCCESFUL\n")

    def testGetOrder(self):
        print("\nTESTING getOrder METHOD")
        print("program results vs map:")
        for item in util.GRADEMAP.items():
            if item[1] == None:
                self.assertEqual(-1, util.getOrder(item[0]))
                print("{0} = {1}".format(item[0], -1))
            else:
                self.assertEqual(item[1], util.getOrder(item[0]))
                print("{0} = {1}".format(item[0], util.GRADEMAP[item[0]]))

        with self.assertRaises(ValueError):
            util.getOrder("willFail")
        
        print("getOrder IS SUCCESFUL\n")

class TestReaderMethods(unittest.TestCase):

    def testReadSecFile(self):
        print("\nTESTING readSecFile METHOD")
        c110S20_data = reader.readSecFile("testdata/COMSC110S20.SEC")
        teststring = """First Name;Last Name;ID;Grades;GradeVal
    Pfssb;Hcfw;6713436;C+;2.33
      Pfckb;Owrob;6758502;C;2.00
       Qczs;Robwsz;6704310;C;2.00
       Qfin;Xsggwqo;6724981;C+;2.33
    Rspzcwg;Qoggobrfo;6719465;I;NaN
       Vwzz;Psbxoawb;6727795;W;NaN
        """
        testdf = pd.read_csv(io.StringIO(teststring), sep = ";", skipinitialspace=True)

        for i in range(len(testdf.index)):
            for j in range(len(testdf.columns)):
                self.assertEqual(str(testdf.iloc[i][j]), str(c110S20_data[g.DATA_FIELD].iloc[i][j]))

        print("read in program df vs test df based on same text file")
        print("program:")
        print(c110S20_data[g.DATA_FIELD])
        print("test:")
        print(testdf)

        print("readSecFile IS SUCCESFUL\n")
        
    def testReadGrpFile(self):
        print("\nTESTING readGrpFile METHOD")
        c110_data = reader.readGrpFile("testdata/COMSC110.GRP")
        testlist = ["COMSC110S20.SEC", "COMSC110S21.SEC"]

        for i in range(len(testlist)):
            self.assertEqual(c110_data[i], testlist[i])

        print("read in program group data vs list based on same text file")
        print("program:")
        print(c110_data)
        print("test:")
        print(testlist)

        print("readGrpFile IS SUCCESFUL\n")

    def testReadRunFile(self):
        print("\nTESTING readRunFile METHOD")
        testrun_data = reader.readRunFile("testdata/TESTRUN.RUN")
        testlist = ["COMSC110.GRP", "COMSC200.GRP"]

        for i in range(len(testlist)):
            self.assertEqual(testrun_data[i], testlist[i])

        print("read in program run data vs list based on same text file")
        print("program:")
        print(testrun_data)
        print("test:")
        print(testlist)

        print("readRunFile IS SUCCESFUL\n")

class TestMainMethods(unittest.TestCase):

    def testFetch(self):
        data = main.fetch("testdata/TESTRUN.RUN")



def generateRandomSection():
    """
    Method used for testing purposes, generates random grades
    """

    datastr = g.GRADE_HEADER + ";" + g.GRADE_VALUE_HEADER + "\n"
    items = list(util.GRADEMAP.items())
    for i in range(15):
        temp = items[random.randrange(0, len(items))]
        datastr += temp[0] + ";"
        if temp[1] != None:
            datastr += str(temp[1])
        datastr += "\n"

    df = pd.read_csv(io.StringIO(datastr), sep = ";")

    #print(datastr)
    #print(df)

if __name__ == '__main__':
    unittest.main()

