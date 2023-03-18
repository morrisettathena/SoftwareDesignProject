package calculation;

/******************************************
 * File:  GradeType.java
 * 
 * Enum that represents various grade types
 * and their associated GPA value.
 * 
*******************************************/

import java.math.BigDecimal;

/// Enum representing grades, their associated GPA value, and string representation.
public enum GradeType {
	
	A		(4.0, "A"),
	AMinus	(3.7, "A-"),	
	BPLUS	(3.3, "B+"),
	B		(3.0, "B"),
	BMINUS	(2.7, "B-"),
	CPLUS	(2.3, "C+"),
	C		(2.0, "C"),
	CMINUS	(1.7, "C-"),
	DPLUS	(1.3, "D+"),
	D		(1.0, "D"),
	F		(0.0, "F"),
	I		(null, "I"),
	W		(null, "W"),
	P		(null, "P"),
	NP		(null, "NP");
	
	private final BigDecimal gpaValue;
	private final String stringRep;
	private final boolean isStandard; //A-F are standards, I, W, P etc are not
	
	GradeType(Double gpaValue, String stringRep) {
		//determine if standard or not
		if (gpaValue == null) {
			this.gpaValue = null;
			this.isStandard = false;
		} else {
			this.gpaValue = new BigDecimal(gpaValue, Globals.CONTEXT);
			this.isStandard = true;
		}
		this.stringRep = stringRep;
	}
	
	/// Returns a gradetype from a string representation.  Throws
	/// IllegalArgumentException if string is not recognized.
	public static GradeType fromRep(String rep) throws IllegalArgumentException{
		for (GradeType gradetype: GradeType.values()) { //loop through all values in Enum
			if (rep.equals(gradetype.getRep())) {
				return gradetype;
			}
		}
		throw new IllegalArgumentException(String.format("%s is not a valid grade type", rep));
	}
	
	public BigDecimal getValue() {
		return gpaValue;
	}
	
	public String getRep() {
		return stringRep;
	}
	
	public boolean isStandard() {
		return isStandard;
	}
	
	@Override
	public String toString() {
		return stringRep;
	}
}
