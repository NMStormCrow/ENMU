/*
* Thomas Crow
* Lab #10
* CS234
*/

import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Random;

public class Sales {

//  Declare instance variables
    private LinkedList<Product> products = new LinkedList<>();

    private Random rand = new Random();

//  Default constructor
    public Sales () {
        generateProducts();
    }

//  Method: generateProducts()
//  Purpose: The method randomly generates between 1 and 5 clients.
//           For each client, randomly generate an amount of product between 1 to 10
//           For each client, randomly generate a price for the product between 0.5 and 50
//           Adds a product to the end of the list of products
//  Arguments: None
//  Returns:  None

    public void generateProducts() {
        
//      Declare class variables
        int    numClients = generateRandomNumber(1,5);
        int    productAmount = 0; 
        double productPrice = 0;
        Product loopProduct;
        
        for (int i = 0; i <= numClients; i++) {
            productAmount = generateRandomNumber(1,10);
            productPrice = generateRandomDoubleNumber(0.5,50);
            loopProduct = new Product(productAmount, productPrice);
            products.addLast(loopProduct);
        }

    }

//  Method: generateRandomNumber()
//  Purpose: Generates a random int between min and max
//  Arguments:The ints value min and max
//  Returns: The random integer

    public int generateRandomNumber(int min, int max) {
        
        int randomInt = this.rand.nextInt(min, max);
        return randomInt;

    }

//  Method: generateRandomDoubleNumber()
//  Purpose: Generates a random double between min and max
//  Arguments:The double values min and max
//  Returns: The random double

    public double generateRandomDoubleNumber(double min, double max) {

        double randomDouble = this.rand.nextDouble(min, max);
        return randomDouble;

    }

//  Method: getSales()
//  Purpose: Generate all information about sales
//  Arguments: None
//  Returns: All information about the sales as a string

    public String getSales() {

//      Declare class variables
        String salesReport = "";
        ListIterator<Product> iterator = products.listIterator();
        int count = 0;
        double totalSales = 0;

        while (iterator.hasNext()) {
            count++;
            iterator.next();
        }

        salesReport = "number of people: " + count + "\n";
        salesReport = salesReport + "************* Amount ********** Price *********** Total\n\n"; 

        iterator = products.listIterator();
        count = 0;

        while (iterator.hasNext()) {
            count++;
            Product loopProduct = iterator.next();
            salesReport = salesReport + "Product" + count + "\t"  + loopProduct.getAmount() + "\t\t" + loopProduct.getPrice() + "\t\t" + loopProduct.productSale() + "\n";
            totalSales = totalSales + loopProduct.productSale();
        }
        
        salesReport = salesReport + "Total sales:\t\t\t\t\t" + String.format("%.2f",totalSales) + "\n";

        return salesReport;

    }

}