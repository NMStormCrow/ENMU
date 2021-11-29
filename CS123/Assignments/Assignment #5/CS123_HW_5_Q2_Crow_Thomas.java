// Assignment: Homework #5 Question #2 
// Creator: Thomas Crow
// Class:  CS123
// Date: 11/28/2021
// Requirements: Write a Java method “largestOfFour” to find the largest number among four 
//               numbers. The method must accept four integer inputs and return one integer. 



import java.util.Scanner;

class LargestOfFour {

    static int getLargestNumber(int num1, int num2, int num3, int num4) {
        int largestNum = num1;
        if (num2 > largestNum) {
            largestNum = num2;
        }
        if (num3 > largestNum) {
            largestNum = num3;
        }
        if (num4 > largestNum) {
            largestNum = num4;
        }
        return largestNum;
    }
    public static void main(String args[]) {
        System.out.println("This program determines the largest of four numbers entered.");
        Scanner scan = new Scanner(System.in);
        System.out.print("Please enter the first number: ");
        int userNum1 = scan.nextInt();
        System.out.print("Please enter the second number: ");
        int userNum2 = scan.nextInt();
        System.out.print("Please enter the third number: ");
        int userNum3 = scan.nextInt();
        System.out.print("Please enter the fourth number: ");
        int userNum4 = scan.nextInt();
        int largestNumber = getLargestNumber(userNum1, userNum2, userNum3, userNum4);
        System.out.println("The largest number is " + largestNumber);
        scan.close();
    }   
}