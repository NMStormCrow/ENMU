// Assignment: Homework #4 Question #2
// Creator: Thomas Crow
// Class:  CS123
// Date: 11/09/2021
// Requirements:  Write a Java program to determine if an input positive integer n is prime or not. 
//                A prime number is a whole number greater than 1 that cannot be made by multiplying other whole numbers.


import java.util.Scanner;

class calculateIfPrimeNumber {
    public static void main(String args[]) {

        boolean isPrime = true;

        System.out.print("This program determines if a number is prime.\n");
        System.out.print("Please enter a postitive whole number greater than 1: ");        
        // Open Scanner
        Scanner scan = new Scanner(System.in);
        int userNumber = scan.nextInt();
        if (userNumber < 2) {
            isPrime = false;
        }
        else {
            for (int i = 2; i < userNumber; i++) {
                if ((userNumber % i) == 0) {
                    isPrime = false;
                }        
            }
        }    

        if (isPrime) {
            System.out.print("The number " + userNumber + " is a prime number.\n");
        }
        else 
            System.out.print("The number " + userNumber + " is not a prime number.\n");

        // Close Scanner
        scan.close();   
    }
}