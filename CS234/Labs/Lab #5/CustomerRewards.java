/*
* CS234
* Thomas Crow
* Lab #5
*
* Requirements: A  supermarket  wants  to  reward  its  best  customer  of  each  day,  showing  the 
                customer’s name on a screen in the supermarket.
*/

import java.util.Scanner;
import java.util.ArrayList;


public class CustomerRewards {

    //  Open Scanner
    static Scanner scan = new Scanner(System.in); 

    /*
    Get the input for the prices and names and add them to the Array Lists
    @param an ArrayList for the sales
    @param an ArrayList for the names
    */

    public static void getValues(ArrayList<Double> sales, ArrayList<String> customers) {

        double PriceofItem = 1;
        String CurrentCustomer = new String("");
        do
         {
            try {
                System.out.printf("Enter the price of the item: ");
                PriceofItem = Double.parseDouble(scan.nextLine());
                if (PriceofItem > 0) {
                    System.out.printf("Enter the last name of the customer: ");
                    CurrentCustomer = scan.nextLine();
//                      Check for existing customer record with same last name, add price of item if found to exisiting record
                    if (customers.contains(CurrentCustomer)) {                    
                        sales.set(customers.indexOf(CurrentCustomer), sales.get(customers.indexOf(CurrentCustomer)) + PriceofItem);
                    }
//                      Add new records if last name not found
                    else {            
                        sales.add(PriceofItem);
                        customers.add(CurrentCustomer);
                    }
                }
            }
            catch (Exception e) {
                scan.reset();
                System.out.printf("Invalid option\n");
            }
        }
        while (PriceofItem > 0);
    }

    /*
    Finds the best customer based on the sales.
    @param an ArrayList for the sales
    @param an ArrayList for the customers
    @return a String with the name of the customer
    */

    public static String nameOfBestCustomer(ArrayList<Double> sales, ArrayList<String> customers) {
        
        String BestCustomer = new String("");
        double HighestSales = 0;

        for (int i = 0; i < sales.size(); i++) {
//          If One Customer has the highest value
            if (sales.get(i) > HighestSales) {
                HighestSales = sales.get(i);
                BestCustomer = customers.get(i);
            }
//          If there is a tie
            else if (sales.get(i) == HighestSales) {
                BestCustomer = BestCustomer + " and " + customers.get(i);
            }
        }
        return BestCustomer;
    }

    public static void main(String args []) {
        
        ArrayList<Double> sales = new ArrayList<Double>();
        ArrayList<String> customers = new ArrayList<String>();
        String BestCustomer;

        getValues(sales, customers);
        BestCustomer = nameOfBestCustomer(sales, customers);
        System.out.printf("List of total sales by customer:\n");
        for (int i = 0; i < sales.size(); i++)
        {
            System.out.printf("%s $%.2f\n", customers.get(i), sales.get(i));
        }
        if (sales.size() > 0) {   
//          Check if multiple best customers
            if (BestCustomer.contains("and"))         
                System.out.printf("The best customers for today are %s\n", BestCustomer);
//          Perform if only one best customer
            else
                System.out.printf("The best customer for today is %s\n", BestCustomer);
        }
//      Perform if there are no best customers
        else {
            System.out.printf("Sorry, no customers on the list.\n");
        }
    //  Close Scanner
        scan.close();    
    }

}
