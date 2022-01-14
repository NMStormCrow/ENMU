// Assignment: Homework #3 Question #2
// Creator: Thomas Crow
// Class:  CS123
// Date: 10/23/2021
// Requirements:  Write a complete Java program that asks the user to input the number of 
//                month and then print the month in English. For example, the user input is 5, 
//                the output should be May

import java.util.Scanner;


class PrintMonth{
    public static void main(String args[]) {

        // Declare and initialize array containing the 12 months
        
        String[] userMonth = new String[12];
        userMonth[0] = "January";
        userMonth[1] = "February";
        userMonth[2] = "March";
        userMonth[3] = "April";
        userMonth[4] = "May";
        userMonth[5] = "June";
        userMonth[6] = "July";
        userMonth[7] = "August";
        userMonth[8] = "September";
        userMonth[9] = "October";
        userMonth[10] = "November";
        userMonth[11] = "December";

        Scanner scan = new Scanner(System.in);

        // User Input
        System.out.print("Please enter the number of the month: 1-12: ");
        int userInput = (scan.nextInt() - 1);

        System.out.println("The month entered is: " + userMonth[userInput]);

        // Close Scanner
        scan.close();
    }
} 
