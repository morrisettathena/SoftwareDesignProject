package calculation;

/****************************************************
 * Util.java
 * 
 * Various utility functions used in calculations
*****************************************************/

import java.math.BigDecimal;
import java.util.HashMap;

public class Util {
	
	public static BigDecimal[] convertArray(double[] arr) {
		BigDecimal[] BDarr = new BigDecimal[arr.length];
		for (int i = 0; i < arr.length; i++) {
			BDarr[i] = new BigDecimal(arr[i], Globals.CONTEXT);
		}
		
		return BDarr;
	}
	
	public static BigDecimal[] convertArray(int[] arr) {
		BigDecimal[] BDarr = new BigDecimal[arr.length];
		for (int i = 0; i < arr.length; i++) {
			BDarr[i] = new BigDecimal(arr[i], Globals.CONTEXT);
		}
		return BDarr;
	}
	
	/// Returns a hashmap where the count of every grade is initialized to 0
	public static HashMap<GradeType, Integer> getNewGradeMap() {
		HashMap<GradeType, Integer> map = new HashMap<GradeType, Integer>();
		for (GradeType gradeType: GradeType.values()) {
				map.put(gradeType, 0);
		}
		return map;
	}
}
