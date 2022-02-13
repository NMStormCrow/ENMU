// CS234
// Lab #3 - 1A
// Thomas Crow
// Requirement: Write Java programs (5) with loops that compute the following:
//              The sum of all even numbers between 2 and 100 (inclusive). 

public class a_SumEvenNumbers {

    public static void main(String args []) {

        int sum = 0;

//      Compute the sum of even numbers between 2 and 100
        for (int i = 2; i <= 100; i = i + 2) {
            sum = sum + i;
        }

//      Print out sum to user
        System.out.println("The sum of all even numbers between 2 and 100 is: " + sum);
    
    }
    
}

// End of program