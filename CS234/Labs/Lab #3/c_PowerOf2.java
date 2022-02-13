// CS234
// Lab #3 - 1C
// Thomas Crow
// Requirement: Write Java programs (5) with loops that compute the following:
//              All powers of 2 from 0 up to 20.

import java.lang.Math;

public class c_PowerOf2 {

    public static void main(String args []) {

        double value = 0;

//      Compute the value of 2 to the power i from 0 to 20
        for (int i = 0; i <= 20; i++) {
            
            value = Math.pow(2, i);

//          Print out value to user
            System.out.printf("The value of 2 to the power %d is %d\n", i, (int)value);
        }
    }
}

// End of program