// Assignment: Homework #5 Question #1 
// Creator: Thomas Crow
// Class:  CS123
// Date: 11/28/2021
// Requirements: Write a Java method “printNTimes” to print a given string for a given times. 
//               Your method should accept two inputs, one is String s and another is an integer n. 
//               The input string s will be printed n times. What is the return type? 



import java.util.Scanner;

class Main {

    // Open Scanner
    static Scanner scan = new Scanner(System.in);
    
    
    static void printProgramInstructions() {
        System.out.print("This program prints a user inputed value a user defined number of times.\n");
    }
    
    static String getString_Value() {
        System.out.print("Please enter the value you would like to be printed: ");        
        String userString = scan.nextLine();     
        return userString;
    }

    static int getN_Value() {
        System.out.print("Please enter the number of times you would like to print the inputed value: ");        
        int userInt = scan.nextInt();
        return userInt;
    }

    static void printNTimes(String s, int n) { 
        for (int i = 0; i < n; i++) {
            System.out.println(s);
        }
    }
    
    public static void main(String args[]) {
        printProgramInstructions();
        String userInput = getString_Value();
        int userN = getN_Value();
        printNTimes(userInput, userN);
        scan.close();
    }
}