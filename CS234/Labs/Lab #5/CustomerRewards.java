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

    /*
    Get the input for the prices and names and add them to the Array Lists
    @param an ArrayList for the sales
    @param an ArrayList for the names
    */

    public static void getValues(ArrayList<Double> sales, ArrayList<String> customers) {



    }

    /*
    Finds the best customer based on the sales.
    @param an ArrayList for the sales
    @param an ArrayList for the customers
    @return a String with the name of the customer
    */

    public static String nameOfBestCustomer(ArrayList<Double> sales, ArrayList<String> customers) {
        
        String BestCustomer = new String("");

        for (int i = 0; i < sales.size(); i++) {


        }

        return BestCustomer;
    }

    public static void main(String args []) {
    //  Open Scanner
        Scanner scan = new Scanner(System.in);         
        
        ArrayList<Double> sales = new ArrayList<Double>();
        ArrayList<String> customers = new ArrayList<String>();
        String BestCustomer;

        getValues(sales, customers);
        BestCustomer = nameOfBestCustomer(sales, customers);
        System.out.printf("The best customer for today is %s", BestCustomer);

    //  Close Scanner
        scan.close();    
    }

}
