package calculation;
import java.math.BigDecimal;
import java.util.HashMap;
import java.util.concurrent.atomic.AtomicReference;
import java.util.ArrayList;

/// Tuple Object that stores section data along with associated z-test value
class SectionTuple {
	private SectionData data;
	private BigDecimal zTestVal;
	
	SectionTuple(SectionData data, BigDecimal zTestVal) {
		this.data = data;
		this.zTestVal = zTestVal;
	}
	
	SectionTuple(SectionData data) {
		this.data = data;
		this.zTestVal = null;
	}
	
	SectionData getData() {
		return data;
	}
	
	BigDecimal getZTestVal() {
		return zTestVal;
	}
}

/// Object that stores an array of section data, and produces statistics about them.
public class GroupData {
	private String name;
	private SectionTuple[] sectionData;
	private BigDecimal groupGpa;
	private BigDecimal groupStdDev;
	private HashMap<GradeType, Integer> gradeCounts;
	private int numStudents;

	public GroupData(String name, SectionData[] sections) {
		this.name = name;
		gradeCounts = Util.getNewGradeMap();
		groupGpa = new BigDecimal(0, Globals.CONTEXT);
		ArrayList<String> studentList = new ArrayList<String>();
		int meanCount = 0; //number of standard grades to be counted
		
		for (int i = 0; i < sections.length; i++) {
			SectionData sec = sections[i];
			BigDecimal popBD = new BigDecimal(sec.getPopulationStandardGrades()); 
			meanCount += sec.getPopulationStandardGrades();//increment by this sections number of standard grades
			
			//for a given section, multiply its average by the number of standard
			//grades it has.  When these values are summed for every section, 
			//the resulting value is equal to the sum of every individual grade across
			//all sections.  Then, the sum can be divided by the number of standard
			//grades, producing the average in a more computationally efficient way.
			groupGpa = groupGpa.add(sec.getGpa().multiply(popBD, Globals.CONTEXT));
			gradeCounts.forEach((gradetype, count) -> { //Increment the count of each grade
				gradeCounts.put(gradetype, count + sec.getNumGradeType(gradetype));
			});
			
			//add to the student list if they do not exist
			for (String s: sec.getStudentList()) {
				if (!studentList.contains(s)) {
					studentList.add(s);
				}
			}
		}
		numStudents = studentList.size();
		BigDecimal meanCountBd = new BigDecimal(meanCount, Globals.CONTEXT);
		groupGpa = groupGpa.divide(meanCountBd, Globals.CONTEXT);//average calculation
		groupGpa = groupGpa.stripTrailingZeros();
		
		calculateStdDev(meanCountBd);
		calculateZVals(sections);
	}
	
	/// Procedure that calculates the standard deviation of grades.
	public void calculateStdDev(BigDecimal meanCountBd) {
		groupStdDev = new BigDecimal(0, Globals.CONTEXT);
		
		//AtomicReference needed because a forEach loop can only use final variables.
		//This gets around the problem by having the contents of sumPointer change, but
		//sumPointer itself stays static.
		AtomicReference<BigDecimal> stdDevPointer = new AtomicReference<BigDecimal>(groupStdDev);
		gradeCounts.forEach((gradetype, count) -> {
			if (gradetype.isStandard()) {
				BigDecimal stdDevSum = stdDevPointer.get();
				BigDecimal countBD = new BigDecimal(count);
				
				///Perform standard deviation calculation.  Because grades are fixed values,
				///The standard deviation can be performed for one grade and then multiplied
				///By how many times the grade occurs.
				BigDecimal temp = gradetype.getValue().subtract(groupGpa).pow(2, Globals.CONTEXT);
				temp = stdDevSum.add(temp.multiply(countBD, Globals.CONTEXT));
				stdDevPointer.set(temp);
			}
		});
		groupStdDev = stdDevPointer.get();
		
		//Divide by n and take the square root to produce final standard deviation
		groupStdDev = groupStdDev.divide(meanCountBd, Globals.CONTEXT).sqrt(Globals.CONTEXT);
		groupStdDev = groupStdDev.stripTrailingZeros();
	}
	
	/// Procedure that performs a z test on every section
	public void calculateZVals(SectionData[] sections) {
		sectionData = new SectionTuple[sections.length];
		
		for (int i = 0; i < sections.length; i++) {
			SectionData sec = sections[i];
			BigDecimal z = sec.getGpa().subtract(groupGpa);
			z = z.divide(groupStdDev, Globals.CONTEXT);
			sectionData[i] = new SectionTuple(sec, z); //make new tuple for this section
		}
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public SectionTuple[] getSectionData() {
		return sectionData;
	}
	
	public int getNumStudents() {
		return numStudents;
	}
	
	public BigDecimal getGroupGpa() {
		return groupGpa;
	}
	
	public BigDecimal getGroupStdDev() {
		return groupStdDev;
	}
}
