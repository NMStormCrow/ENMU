// CS234
// Lab #3 - 1B
// Thomas Crow
// Requirement: Write Java programs (5) with loops that compute the following:
//              The sum of all squares between 1 and 100 (inclusive). 

import java.lang.Math;

public class b_SumSquares {

    public static void main(String args []) {

        int sum = 0;

//      Compute the sum of all numbers squared between 1 and 100
        for (int i = 1; i <= 100; i++) {
            sum = sum + (int)Math.pow((double)i, 2);
        }

//      Print out sum to user
        System.out.printf("The sum of all numbers between 1 and 100 squared is: %d\n", sum);    
    }    
}

// End of program