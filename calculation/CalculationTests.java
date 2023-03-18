package calculation;

/****************************************************
 * CalculationTests.java
 * 
 * File that runs unit and integration tests on 
 * GradeTye, SectionData,and GroupData objects.
*****************************************************/

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.math.BigDecimal;

class CalculationTests {
	
	/// Function that takes an array of String representations of grades
	/// and converts them to an array of GradeType objects
	GradeType[] convertToGrades(String[] arr) {
		GradeType[] grades = new GradeType[arr.length];
		for (int i = 0; i < grades.length; i++) {
			grades[i] = GradeType.fromRep(arr[i]);
		}
		return grades;
	}
	

	final String START_STR 		= "TEST START:   ";
	final String FAIL_STR 		= "TEST FAIL:    ";
	final String SUCCESS_STR 	= "TEST SUCCESS: ";
	
	/// Unit test that sees if Grades can be initialized to correct values
	@Test
	void testInitializeGrades() {
		String t = "GRADES INITIALIZE";
		System.out.println(START_STR + t);
		String f = FAIL_STR + t;
		
		// Test both types of initialization
		GradeType a = GradeType.fromRep("A");
		GradeType a2 = GradeType.A;
		assertEquals(a.getValue(), new BigDecimal(4.0, Globals.CONTEXT), f);
		assertEquals(a, a2, f);
		assertTrue(a.isStandard(), f);
		
		// Test several grade types to see if they behave as expected
		GradeType aplus = GradeType.fromRep("A-");
		assertEquals(aplus.getValue(), new BigDecimal(3.7, Globals.CONTEXT), f);
		GradeType bplus = GradeType.fromRep("B+");
		assertEquals(bplus.getValue(), new BigDecimal(3.3, Globals.CONTEXT), f);
		GradeType i = GradeType.fromRep("I");
		assertEquals(i.getValue(), null, f);
		assertFalse(i.isStandard(), f);
		assertFalse(a.equals(i), f);
		
		// Test to make sure that grades can only be initialized from correct
		// representation
		try {
			GradeType err = GradeType.fromRep("err");
			fail(f);
		} catch (IllegalArgumentException e) {}
		System.out.println(SUCCESS_STR + t);
	}
	
	/// Unit test that determines if section data can be initialized sucesfully
	@Test
	void testInitializeSectionData() {
		String t = "SECTION DATA INITIALIZE";
		System.out.println(START_STR + t);
		String f = FAIL_STR + t;
		
		String[] temp1 = {
				"A", "B", "C+", "A-", "D", "A"
		};
		BigDecimal avg1 = new BigDecimal(3, Globals.CONTEXT); //average calculated outside of program
		GradeType[] test1 = convertToGrades(temp1);
		SectionData data = new SectionData("TEST", test1);
		
		//check to make sure that the average and number of grades is tracked correctly
		assertEquals(data.getName(), "TEST", f);
		assertEquals(data.getPopulation(), 6, f);
		assertEquals(data.getPopulation(), data.getPopulationStandardGrades(), f);
		
		assertEquals(data.getNumGradeType(GradeType.A), 2, f);
		assertEquals(data.getNumGradeType(GradeType.B), 1, f);
		assertEquals(data.getNumGradeType(GradeType.I), 0, f);

		assertEquals(data.getGpa(), avg1);
		
		System.out.println(SUCCESS_STR + t);
	}
	
	/// Unit test that sees if section data can take in non-standard grades and
	/// still perform precise calculations
	@Test
	void testInitializeSectionDataNonStandard() {
		String t = "NONSTANDARD SECTION DATA";
		System.out.println(START_STR + t);
		String f = FAIL_STR + t;
		
		String[] temp1 = {
				"A", "A", "A", "I", "NP", "P", "W", "I"
		};
		BigDecimal avg1 = new BigDecimal(4, Globals.CONTEXT);
		GradeType[] test1 = convertToGrades(temp1);
		SectionData data = new SectionData("TEST", test1);
		
		//check to make sure that nonstandard grades are factored in correctly to calculation
		assertEquals(data.getPopulation(), 8, f);
		assertEquals(data.getPopulationStandardGrades(), 3, f);
		
		assertEquals(data.getNumGradeType(GradeType.I), 2, f);
		assertEquals(data.getNumGradeType(GradeType.NP), 1, f);
		
		assertEquals(data.getGpa(), avg1, f);
		
		System.out.println(SUCCESS_STR + t);
	}
	
	/// unit test that determines if calculations are being made precisely
	@Test
	void testDecimalPrecision() {
		String t = "DECIMAL PRECISION";
		System.out.println(START_STR + t);
		String f = FAIL_STR + t;
		
		String[] temp1 = {
			"A", "B+", "C+", "D", "NP", "A-", "B+", "C+"
		};
		BigDecimal avg1 = new BigDecimal("2.843");
		GradeType[] test1 = convertToGrades(temp1);
		SectionData data1 = new SectionData("TEST", test1);
		assertEquals(data1.getGpa(), avg1, f);
		
		String[] temp2 = {
			"W", "W", "D+", "F", "B-", "F", "C-", "B+", "B-", 
			"A", "B-", "NP", "D+", "F", "B", "A", "D", "C", 
			"C", "W", "B-", "B+", "F", "B+", "C-", "A-", "B-", 
			"W", "C", "F"
		};
		GradeType[] test2 = convertToGrades(temp2);
		BigDecimal avg2 = new BigDecimal("2.044");
		SectionData data2 = new SectionData("TEST", test2);
		assertEquals(data2.getGpa(), avg2, f);
		
		System.out.println(SUCCESS_STR + t);
	}
	
	/// Unit test that sees if SectionData is throwing errors correctly
	@Test
	void testSectionErrors() {
		String t = "SECTION DATA ERRORS";
		System.out.println(START_STR + t);
		String f = FAIL_STR + t;
		
		GradeType[] test1 = {};
		try {
			SectionData data1 = new SectionData("TEST", test1); //cannot take empty set
			fail(f);
		} catch (IllegalArgumentException e) {};
		String[] temp2 = {"NP", "I", "W"};
		GradeType[] test2 = convertToGrades(temp2);
		try {
			SectionData data1 = new SectionData("TEST", test2); //need at least one standard grade
			fail(f);
		} catch (IllegalArgumentException e) {};
		
		System.out.println(SUCCESS_STR + t);
	}
	
	/// Integration test that determines if GroupData can initialize and
	/// Perform calculations correctly
	@Test
	void testGroupCalculations() {
		String t = "GROUP CALCULATIONS";
		System.out.println(START_STR + t);
		String f = FAIL_STR + t;
		
		String[] temp1 = {
			"B+", "D", "C+", "D", "D", "C-", "C+", "F", "B", "B", 
			"B", "D+", "C", "P", "F", "C+", "A", "A", "C+", "A-", 
			"C-", "C+", "C", "I", "F", "P", "A", "NP", "NP", "C+"
		};
		BigDecimal avg1 = new BigDecimal(2.14, Globals.CONTEXT);
		BigDecimal z1 = new BigDecimal(-0.1354, Globals.CONTEXT);
		
		String[] temp2 = {
			"D+", "C", "W", "D+", "B", "W", "I", "A-", "NP", "B", 
			"P", "NP", "B-", "F", "D", "C+", "F", "I", "W", "A-", 
			"A-", "P", "A-", "B+", "B", "W", "I", "C", "B", "B+"
		};
		BigDecimal avg2 = new BigDecimal(2.4211, Globals.CONTEXT);
		BigDecimal z2 = new BigDecimal(0.09801, Globals.CONTEXT);
		
		String[] temp3 = {
			"C", "A-", "D", "NP", "A-", "NP", "A", "P", "P", "NP", 
			"NP", "B", "A", "C", "F", "W", "W", "D+", "W", "D+", "B-", 
			"W", "D", "B", "P", "B", "W", "D+", "NP", "A"
		};
		BigDecimal avg3 = new BigDecimal(2.4118, Globals.CONTEXT);
		BigDecimal z3 = new BigDecimal(0.09053, Globals.CONTEXT);
		
		String[][] gradeArray = {temp1, temp2, temp3};
		BigDecimal[] avgArray = {avg1, avg2, avg3};
		BigDecimal[] zArray = {z1, z2, z3};
		
		// make section data objects from above 3 sets of data
		SectionData[] secData = new SectionData[gradeArray.length];
		for (int i = 0; i < gradeArray.length; i++) {
			GradeType[] test = convertToGrades(gradeArray[i]);
			String name = String.format("Section %d", i+1);
			secData[i] = new SectionData(name, test);
		}
		BigDecimal stdDev = new BigDecimal(1.204, Globals.CONTEXT); //based on outside calculations
		BigDecimal groupAvg = new BigDecimal(2.303, Globals.CONTEXT); //based on oustide calculations
		
		GroupData groupdata = new GroupData("TEMP", secData);
		
		assertEquals(groupdata.getGroupGpa(), groupAvg, f);
		assertEquals(groupdata.getGroupStdDev(), stdDev, f);
		
		//check that the z-tests are consistent with outside calculations
		SectionTuple[] ztests = groupdata.getSectionData();
		for (int i = 0; i < ztests.length; i++) {
			assertEquals(zArray[i], ztests[i].getZTestVal(), f);
		}
		
		System.out.println(SUCCESS_STR + t);
	}
}
