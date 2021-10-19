// Assignment: HW2
// Creator: Thomas Crow
// Class:  CS123
// Date: 10/03/2021
// Requirements:  Write a Java program to convert an amount to (dollar, cent) format. If amount 12.45 is input from user,
//                for example, must print “12 dollars and 45 cents”. (The user will only input the normal dollar amount.)
//

import java.util.Scanner;

class CurrencyPrettyPrint {
    public static void main(String args[]) {

//    Open Scanner
      Scanner scan = new Scanner(System.in);

//    User Input
      System.out.println("Please enter a dollar amount using number format: ");

//    Variable initialization
      double userAmount = scan.nextDouble();
      int userDollarAmount = (int)userAmount;
      int userCentsAmount =  (int)((userAmount * 100) - (userDollarAmount * 100));

//    User Output
//    Note: I have used an if statement to do basic validation to handle the singular dollar grammar and negative entries

      if (userDollarAmount == 1) {
          System.out.println("The dollar amount written out in English is " + userDollarAmount + " dollar and " + userCentsAmount + " cents.");
          }
      else if (userDollarAmount < 0) {
          System.out.println("Please enter a postive amount");
          }
      else  {
        System.out.println("The dollar amount written out in English is " + userDollarAmount + " dollars and " + userCentsAmount + " cents.");
          }

//    Close Scanner
      scan.close();
    }
}
