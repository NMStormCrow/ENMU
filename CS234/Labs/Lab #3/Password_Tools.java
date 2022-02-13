// CS234
// Lab #3 - 2
// Thomas Crow
// Requirement: Write a program that validates a new password, following these rules:
//              • The password must be at least 8 characters long.
//              • The password must have at least one uppercase and one lowercase letter
//              • The password must have at least one digit.
//
//              Write a Java program that asks for a password, then asks again to confirm it.
//              If the passwords don’t match or the rules are not fulfilled, prompt again.
//              Your program should include a method that checks whether a password is valid.
//

import java.util.Objects;
import java.util.Scanner;

public class Password_Tools {

/*
Checks if both passwords are the same
@param password and confirmation password
@return true or false
*/

    public static boolean samePassword(String password, String confPassword) {

        return Objects.equals(password, confPassword);

    }

/*
Checks if the password is valid.
It uses isDigit(), isLowerCase(), and isUpperCase() helper methods
@param the password
@return true or false
*/

    public static boolean validate(String password) {

        boolean hasUpper = false;
        boolean hasLower = false;
        boolean hasDigit = false;
        boolean longEnough = false;
        boolean passwordValid = false;

        for (int i = 0; i < password.length(); i++) {
            
            char loopChar = password.charAt(i);

            if (hasUpper == false) {
                hasUpper = isUpperCase(loopChar);
            }

            if (hasLower == false) {
                hasLower = isLowerCase(loopChar);
            }

            if (hasDigit == false) {
                hasDigit = isDigit(loopChar);
            }

            if (longEnough == false) {
                longEnough = isLongEnough(password);
            }

            if (hasUpper && hasLower && hasDigit && longEnough) {
                passwordValid = true;
            }             
        }

        return passwordValid;
    }

/*
Checks if the character is a digit (0 to 9)
@param a character
@return true or false
*/

    public static boolean isDigit(char ch) {

        return Character.isDigit(ch);

    }

/*
Checks if the character is lower case(a to z)
@param a character
@return true or false
*/

    public static boolean isLowerCase(char ch) {

        return Character.isLowerCase(ch);

    }

/*
Checks if the character is upper case (A to Z)
@param a character
@return true or false
*/

    public static boolean isUpperCase(char ch) {

        return Character.isUpperCase(ch);

    }

/*
Checks if the password is long enough
@param the password
@return true or false
*/

    public static boolean isLongEnough(String password) {

        return (password.length() >= 8);
 
    }


    public static void main(String args []) {

//      Open Scanner        
        Scanner scan = new Scanner(System.in);

        boolean passwordValid;
        boolean passwordSame = false;
        String firstPassword = "";
        String secondPassword = "";

//      Loop until user enters valid password and can confirm it         
        while (passwordSame == false) {

            passwordValid = false;

//          Prompt user to create a password and validate it meets required complexity
            while (passwordValid == false) {
                System.out.printf("Please enter a password: ");
                firstPassword = scan.nextLine();
                passwordValid = validate(firstPassword);
                if (passwordValid == false) {
                    System.out.printf("The password did not meet complexity requirements. Please try again.\n");
                }
            }

//          Have user confirm password.
            System.out.printf("Please reenter the password: ");
            secondPassword = scan.nextLine();
            passwordSame = samePassword(firstPassword, secondPassword); 
            if (passwordSame == false) {
                System.out.printf("The passwords did not match. Please try again.\n");
            }
        }

//      Print confirmation to user
        System.out.printf("The password has been confirmed.\n");

        // Close Scanner
        scan.close();        
    }
}

// End of program