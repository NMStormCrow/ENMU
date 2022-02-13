// CS234
// Lab #3 - 1D
// Thomas Crow
// Requirement: Write Java programs (5) with loops that compute the following:
//              The sum of all odd numbers between a and b (inclusive), where a and b are inputs.

import java.util.Scanner;

public class d_SumOfOddNumbers {

    public static void main(String args []) {

//      Open Scanner        
        Scanner scan = new Scanner(System.in);

        int Sum = 0;
        int firstNum = 0;
        int secondNum = 0;
        int smallNum = 0;
        int bigNum = 0;

//      Obtain user input
        System.out.printf("This program gives the sum of odd numbers between two inputted whole numbers.\n");
        System.out.printf("Please enter the first number: ");
        firstNum = scan.nextInt();
        System.out.printf("Please enter the second number: ");
        secondNum = scan.nextInt();

//      Determine the smaller and larger number from the user inputs         
        if (firstNum > secondNum) {
            bigNum = firstNum;
            smallNum = secondNum;
        }
        else {
            bigNum = secondNum;
            smallNum = firstNum;
        }

//      Compute the sum of odd numbers between smallNum and bigNum
        for (int i = smallNum; i <= bigNum; i++) {
            if (i % 2 != 0) {
                Sum = Sum + i;
            }
        }
                        
//      Print out value to user
        System.out.printf("The sum of odd numbers between %d and %d is %d\n", smallNum, bigNum, Sum);

//      Close Scanner        
        scan.close();        
        
    }
}

// End of program