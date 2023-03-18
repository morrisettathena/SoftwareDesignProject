package calculation;

/****************************************************
 * Globals.java
 * 
 * Various global values that are used in the calculation
 * package
*****************************************************/

import java.math.MathContext;
import java.math.BigDecimal;

public class Globals {
	static int SCALE = 4; //Scale which decimals should be rounded to
	static MathContext CONTEXT = new MathContext(SCALE);
	static double LOW_Z_BOUND = -2.0;
	static double HIGH_Z_BOUND = 2.0;
}
