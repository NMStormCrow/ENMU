// Assignment: Homework #3 Question #1
// Creator: Thomas Crow
// Class:  CS123
// Date: 10/23/2021
// Requirements:  Suppose the cost of airmail letters is 30 cents for the first ounce and 25 cents for each additional ounce. 
//                Write a complete Java program to compute the cost of a letter for a given weight of the letter in ounce. (hint: use Math.ceil(???)) 
//                Some sample runs:
//                input  output
//                0.5     30 cents
//                1       30 cents
//                1.1     55 cents
//                2       55 cents
//                2.5     80 cents

import java.lang.Math;
import java.util.Scanner;

class CurrencyPrettyPrint {
    public static void main(String args[]) {
        
        // Open Scanner
        Scanner scan = new Scanner(System.in);

        // Print out banner for user
        for (int j=0; j<100; j++) 
            System.out.print("*");
        System.out.println();

        System.out.print("***");
        for (int j=0; j<94; j++) 
            System.out.print(" ");
        System.out.print("***");
        System.out.println();
        
        System.out.print("***");
        for (int j=0; j<30; j++) 
            System.out.print(" ");
        System.out.print("Shipping rates are as follows: ");    
        for (int j=0; j<33; j++) 
            System.out.print(" ");
        System.out.print("***");
        System.out.println();

        System.out.print("***");
        for (int j=0; j<30; j++) 
            System.out.print(" ");
        System.out.print("Airmail: First ounce is 30 cents: ");    
        for (int j=0; j<30; j++) 
            System.out.print(" ");
        System.out.print("***");
        System.out.println();

        System.out.print("***");
        for (int j=0; j<30; j++) 
            System.out.print(" ");
        System.out.print("Airmail: Additional ounces are 25 cents per ounce");    
        for (int j=0; j<15; j++) 
            System.out.print(" ");
        System.out.print("***");
        System.out.println();

        System.out.print("***");
        for (int j=0; j<94; j++) 
            System.out.print(" ");
        System.out.print("***");
        System.out.println();
        
        for (int i=0; i<100; i++) 
            System.out.print("*");
        System.out.println();
        System.out.println();
        
        // User Input
        System.out.print("How many ounces is your letter? ");
      
        double letterWeight = scan.nextDouble();
        int roundedLetterWeight = (int)Math.ceil(letterWeight);
        double shippingCost = 0.3 + (0.25 * (roundedLetterWeight - 1));
        System.out.println("The shipping cost is $" + String.format("%.2f",shippingCost));

        // Close Scanner
        scan.close();

    }
}