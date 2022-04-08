/*
* Thomas Crow
* Lab #10
* CS234
*/

public class Product {

//  Declare instance variables
    
    private int amount;
    private double price;

//  Default constructor
    
    public Product (int amount, double price) {
        this.amount = amount;
        this.price = price;
    }

//  Method: getAmount()
//  Purpose: Provide the amount of the product
//  Arguments: None
//  Returns: The amount of product as an int 

    public int getAmount() {
        return this.amount;
    }

//  Method: getPrice()
//  Purpose: Provide the price of the product
//  Arguments: None
//  Returns: The price of the product as a double 

    public double getPrice() {
        return Double.parseDouble(String.format("%.2f", this.price));
    }

//  Method: productSale()
//  Purpose: Return the product of amount * sale, with at most two decimal points
//  Arguments: None
//  Returns: The value of amount * sale as a double

    public double productSale() {
        return Double.parseDouble(String.format("%.2f", (this.amount * this.price)));
    }
    
}