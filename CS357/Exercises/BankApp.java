class BankAccount {

    private double balance;  //account balance

    public BankAccount(double openingBalance)  {    //constructor
        balance = openingBalance;
    }
    
    public void deposit(double amount) {    //makes depsoit
        balance = balance + amount;
    }

    public void withdraw(double amount) {   //makes withdrawl
        balance = balance - amount;
    }

    public void display() {  //displays balance
        System.out.println("balance = $" + String.format("%.2f",balance));
    }
}   // end class BankAccount
/////////////////////////////////////////////////////////////////////////////

class BankApp {
    public static void main(String[] args) {
    
        BankAccount ba1 = new BankAccount(100.00);  // create account

        System.out.print("Before transactions, ");
        ba1.display();                              //display balance

        ba1.deposit(74.35);                         //make deposit
        ba1.withdraw(20.00);                        //make withdrawl

        System.out.print("After transactions, ");
        ba1.display();                               //display balance
    }   //end main
}   //end class BankApp