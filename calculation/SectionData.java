package calculation;

/****************************************************
 * SectionData.java
 * 
 * Object representing statistics about a given class
 * section.  Takes in an array of BigDecimals and 
 * populates various fields according to contents
 * of the array.
*****************************************************/

import java.math.BigDecimal;
import java.util.concurrent.atomic.AtomicReference;
import java.util.HashMap;
import java.util.ArrayList;

/// Object representing statistics about a given class section.
public class SectionData {
	private String name;
	private int population;
	private int populationStandardGrades;
	private BigDecimal sectionGpa;
	private HashMap<GradeType, Integer> gradeCounts;
	private ArrayList<String> studentList;
	
	public SectionData(String name, GradeType[] grades, String[] studentArr) {
		setData(name, grades, studentArr);
	}
	
	public SectionData(String name, GradeType[] grades) {
		String[] emptyset = {};
		setData(name, grades, emptyset);
	}
	
	/// Procedure that is used to initialize the section data.
	private void setData(String name, GradeType[] grades, String[] studentArr) {
		this.name = name;
		population = grades.length; //population should match number of grades
		populationStandardGrades = 0;
		gradeCounts = Util.getNewGradeMap(); //set all counts of each grade to 0
		studentList = new ArrayList<String>(studentArr.length);
		
		//loop through every grade in the array
		for (int i = 0; i < grades.length; i++) {
			//in the gradeCounts hashmap, anytime a value is found
			//increment that value.
			gradeCounts.compute(grades[i], (grade, count) ->
				++count
			);
			
			//only increment the standard population if it is a standard grade
			if (grades[i].isStandard()) {
				populationStandardGrades++;
			}
		}
		
		//record the name of every student in the student list
		for (int i = 0; i < studentArr.length; i++) {
			studentList.add(studentArr[i]);
		}
		
		//set sectionGpa based on gradeCounts
		calculateAverage();
	}

	///Populates the sectionGpa field with the correct GPA based on gradeCounts
	private void calculateAverage() throws IllegalArgumentException {
		if (populationStandardGrades < 1)
			throw new IllegalArgumentException("cannot calculate average of set with no standard grades");
		
		//AtomicReference needed because a forEach loop can only use final variables.
		//This gets around the problem by having the contents of sumPointer change, but
		//sumPointer itself stays static.
		BigDecimal initSum = new BigDecimal(0, Globals.CONTEXT);
		AtomicReference<BigDecimal> sumPointer = new AtomicReference<BigDecimal>(initSum);
		gradeCounts.forEach((grade, count) -> {
			if (grade.isStandard()) {
				BigDecimal countBD = new BigDecimal(count, Globals.CONTEXT);
				BigDecimal sum = sumPointer.get();
				//add to the sum the value of the grade, multiplied by the number of occurences
				//of said grade.
				sum = sum.add(grade.getValue().multiply(countBD, Globals.CONTEXT), Globals.CONTEXT);
				sumPointer.set(sum);
			}
		});
		
		BigDecimal popStandardBD = new BigDecimal(populationStandardGrades, Globals.CONTEXT);
		sectionGpa = sumPointer.get().divide(popStandardBD, Globals.CONTEXT).stripTrailingZeros();
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public int getPopulation() {
		return population;
	}
	
	public int getPopulationStandardGrades() {
		return populationStandardGrades;
	}
	
	public BigDecimal getGpa() {
		return sectionGpa;
	}
	

	public HashMap<GradeType, Integer> getCounts() {
		return gradeCounts;
	}
	
	/// Returns an integer that represents the number of times
	/// a certain grade type appears in the section data
	public int getNumGradeType(GradeType type) {
		return gradeCounts.get(type);
	}
	
	@Override
	public String toString() {
		return name;
	}
	
	public ArrayList<String> getStudentList() {
		return studentList;
	}
	
	public int getNumStudents() {
		return population;
	}
}
