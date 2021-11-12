// Assignment: Homework #4 Question #1 Part #1
// Creator: Thomas Crow
// Class:  CS123
// Date: 11/09/2021
// Requirements:  Write TWO complete Java programs that accept a small positive integer n fromuser, then print the “hello world” I times. Each program either use “for” loop or “while” loop. 



import java.util.Scanner;

class PrintWorldViaForLoop {
    public static void main(String args[]) {
        
        int userInput = -1;  

        while ((userInput < 1) || (userInput > 100)) {
            System.out.print("How many times would you like to print \"hello world\", Between 1 to 100 times: ");
            Scanner scan = new Scanner(System.in);
            userInput = scan.nextInt();
            if (userInput < 1) {
                System.out.print("Please enter a postive number.\n");
            }
            else if (userInput > 100) {
                System.out.print("Please enter a postive number equal to 100 or less.\n");
            }
            else {
                scan.close();
            }
        } 

        for (int i = 0; i < userInput; i++) {
            System.out.print("hello world\n");
        }
    }
}