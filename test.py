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
        self.assertAlmostEqual(dict1[g.MEAN_FIELD], 2.73)
        self.assertAlmostEqual(dict1[g.STDDEV_FIELD], 1.23)
        self.assertEqual(dict1[g.NUM_STUD_FIELD], 7)

        df2 = pd.read_csv(io.StringIO(data2), sep = ";")
        sec2data = {g.DATA_FIELD: df2}
        dict2 = calculation.calculateSectionData(sec2data)

        #test to make sure that values are the same as independently calculated values
        self.assertAlmostEqual(dict2[g.MEAN_FIELD], 2.37)
        self.assertAlmostEqual(dict2[g.STDDEV_FIELD], 1.30)
        self.assertEqual(dict2[g.NUM_STUD_FIELD], 15)

    def testCalculateGroupData(self):
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
        self.assertAlmostEqual(newdata[g.MEAN_FIELD], 2.41)
        self.assertAlmostEqual(newdata[g.STDDEV_FIELD], 1.11)
        self.assertEqual(newdata[g.NUM_STUD_FIELD], 47)
        self.assertAlmostEqual(newdata[g.ZTEST_FIELD]["sec1"], -0.07)
        self.assertAlmostEqual(newdata[g.ZTEST_FIELD]["sec2"], -0.05)
        self.assertAlmostEqual(newdata[g.ZTEST_FIELD]["sec3"],  0.15)

class TestUtilMethods(unittest.TestCase):

    def testIsRegistered(self):
        for item in util.GRADEMAP.keys():
            self.assertTrue(util.isRegistered(item))
        self.assertFalse(util.isRegistered("erawoier"))
        self.assertFalse(util.isRegistered("+"))
        self.assertFalse(util.isRegistered("-"))

    def testGradeToValue(self):
        for item in util.GRADEMAP.items():
            util.GRADEMAP[item[0]] == item[1]

    def testConstructPath(self):
        path = "testing"
        file = "x"
        pathconstruct = util.constructPath(path, file)
        self.assertEqual("testing/x", pathconstruct)

    def testGetOrder(self):
        for item in util.GRADEMAP.items():
            if item[1] == None:
                self.assertEqual(-1, util.getOrder(item[0]))
            else:
                self.assertEqual(item[1], util.getOrder(item[0]))

        with self.assertRaises(ValueError):
            util.getOrder("willFail")

class TestReaderMethods(unittest.TestCase):

    def testReadSecFile(self):
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

    def testReadGrpFile(self):
        c110_data = reader.readGrpFile("testdata/COMSC110.GRP")
        testlist = ["COMSC110S20.SEC", "COMSC110S21.SEC"]

        for i in range(len(testlist)):
            self.assertEqual(c110_data[i], testlist[i])

    def testReadRunFile(self):
        testrun_data = reader.readRunFile("testdata/TESTRUN.RUN")
        testlist = ["COMSC110.GRP", "COMSC200.GRP"]

        for i in range(len(testlist)):
            self.assertEqual(testrun_data[i], testlist[i])

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

