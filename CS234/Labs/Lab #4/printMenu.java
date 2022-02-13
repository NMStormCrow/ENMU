/*
* CS234
* Thomas Crow
* Lab #4 Q1
*/

import java.util.Scanner;

public class printMenu {

    static Scanner scan = new Scanner(System.in);

    /*
    * Prints a sequence of numbers starting at start, no larger than bound,
    * incrementing by skip. The numbers are printed on a single line.
    * @param start the starting number (integer)
    * @param bound the ending number (integer)
    * @param skip the incrementing number (integer)
    * @return nothing
    */

    public static void printNumbers(int start, int bound, int skip) {
        for (int i = start; i <= bound; i += skip) {
            System.out.printf("%d ", i);    
        }
        System.out.printf("\n");
    }

/*
    * The method takes a String and returns the number of lower-case letters
    'a'
    * in the string. Do not use the count() built-in method.
    * @param s, the string
    * @return the count
*/

    public static int countA(String s) {
        int numberOfLowerCase = 0;
        char loopChar = 0; 
        for (int i = 0; i < s.length(); i++) {
            loopChar = s.charAt(i);
            if (Character.isLowerCase(loopChar)) {
                numberOfLowerCase++;
            }        
        }
        return numberOfLowerCase;
    }

    /* The method takes a character and a string and return a string that has
    * the character interleaved after each character in the given string.
    * @param c, the character
    * @param s, the string
    * @return the new string
    */
    
    public static String interleave(char c, String s) {

        String newString = new String("");

        return newString;

    }
    
    /*
    * The method takes a string and two characters and returns a string in
    * which every occurrence of the first character is replaced by the
    *second one.
    * Do not use the .replace() built-in method.
    * @param s, the string
    * @param a, the first character
    * @param b, the second character
    * @return a new string
    */

    public static String replace(String s, char a, char b) {

        String newString = new String("");

        return newString;
    }
    
    
    /*
    * This method gets the values for printNumbers() and calls it
    */

    public static void option1() {

        int userStart;
        int userBound;
        int userSkip;
        boolean keepRunningLoop = true;


        while (keepRunningLoop) {
            try {
                System.out.printf("Write the starting number:\n");
                userStart = scan.nextInt();
                System.out.printf("Write the ending number:\n");
                userBound = scan.nextInt();
                System.out.printf("Write the skip:\n");
                userSkip = scan.nextInt();
                printNumbers(userStart, userBound, userSkip);
                keepRunningLoop = false;
             }
            catch (Exception e) {
                scan.reset();
                scan.next();
                System.out.printf("Invalid option\n");
            } 
        } 
    }

    /*
    * This method gets the values for countA() and calls it
    */

    public static void option2() {

    }

    /*
    * This method gets the values for interleave()and calls it
    */

    public static void option3() {

    }

    /*
    * This method gets the values for replace() and calls it
    */

    public static void option4() {

    }

    /*
    * This method builds the menu, gets the user selection, and uses a switch
    statement
    * to call the respective options. The selection should use a switch()
    statement.
    */
    
    public static void menu() {
        
        boolean keepRunning = true;
        Scanner scan = new Scanner(System.in);
        int userChoice;


        while (keepRunning) {
            System.out.printf("Select an option:\n");
            System.out.printf("1. Print Numbers\n");
            System.out.printf("2. Count As\n");
            System.out.printf("3. Interleave\n");
            System.out.printf("4. Replace\n");
            System.out.printf("5. Quit\n");
            try {
                userChoice = scan.nextInt();
                System.out.printf("You selected %d\n", userChoice);           
                switch (userChoice) {
                    case 1:   option1();
                              break;
                    case 2:   option2();
                              break;
                    case 3:   option3();
                              break;
                    case 4:   option4();
                              break;
                    case 5:   System.out.printf("Bye\n");
                              keepRunning = false;
                              break;
                    default:  System.out.printf("Invalid option\n");
                              break; 
                }              
            }  
            catch (Exception illegal) {
                scan.reset();
                scan.next();
                System.out.printf("Invalid option\n");
            }
            System.out.printf("~~~~~~~~~~~~~~~~~~~\n");
        }
//      Close Scanner
        scan.close();
    }

    public static void main(String args []) {
        menu();
    }

}