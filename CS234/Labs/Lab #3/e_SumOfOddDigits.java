// CS234
// Lab #3 - 1E
// Thomas Crow
// Requirement: Write Java programs (5) with loops that compute the following:
//              The sum of all odd digits of an input. (For example, if the input is
//              32677, the sum would be 3 + 7 + 7 = 17.)

import java.util.Scanner;

public class e_SumOfOddDigits {

    public static void main(String args []) {

//      Open scanner
        Scanner scan = new Scanner(System.in);

        int sum = 0;
        int loopNumber = 0;

//      Obtain user input
        System.out.printf("This program determines the sum of odd numbers contained in an inputted number.\n");
        System.out.printf("Please enter a number: ");
        String userNum = scan.nextLine();

//      Add odd numbers contained in userNum        
        for (int i = 0; i < userNum.length(); i++) {
            
            loopNumber = Character.getNumericValue(userNum.charAt(i));
            
            if (loopNumber % 2 != 0) {
                sum = sum + loopNumber;
            }
        }
        
//      Print out value to user
        System.out.printf("The sum of odd numbers contained in %s is %d\n", userNum, sum);
        
//      Close Scanner        
        scan.close();        
    }
}

// End of program