// Thomas Crow
// CS234
// Lab 2 Question 1

import java.util.Scanner;

public class ComputeCostOfOrder {
    public static void main(String args []) {

        Scanner in = new Scanner(System.in);
        System.out.print("Enter the price of a book: ");
        float PriceOfBook = in.nextFloat();
        System.out.print("Enter the number of books: ");
        long NumberOfBooks = in.nextLong();
        float CostOfBooks = PriceOfBook * NumberOfBooks;
        final double TaxRate = 0.075;
        double CostOfTax = CostOfBooks * TaxRate;
        final int ShippingCharge = 2;
        float CostOfShipping = NumberOfBooks * ShippingCharge;
        double CostOfOrder = CostOfBooks + CostOfTax + CostOfShipping;
        System.out.printf("Total price of order: $%.2f \n", CostOfOrder); 
        in.close();
    }
}