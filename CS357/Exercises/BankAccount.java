import java.util.Scanner;

class BankAccount {

    private double balance;  //account balance

    public BankAccount(double openingBalance)  { //constructor
        balance = openingBalance;
    }
    
    public void deposit(double amount) { //makes depsoit
        balance = balance + amount;
    }

    
    public static void main(String args[]) {
        
        Scanner scan = new Scanner(System.in);
       
        scan.close();
    }
}