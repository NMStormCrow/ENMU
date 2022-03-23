/*
* CS234
* Thomas Crow
* Lab #8 
*/

public class CashPayment extends Payment {
    
//  Declaration of instance variables
    private String clientName = new String();

//  Default constructor
    public CashPayment(double value, String name) {
        super(value);
        this.clientName = name;
    }

//  Method: getClientName 
//  Purpose: Get the name of the client
//  Arguments: None
//  Returns: The name of the client as a String value

    public String getClientName() {
        return this.clientName;
    }

//  Method: paymentDetails
//  Purpose: Print the details of the payment
//  Arguments: None
//  Returns:  None

    public void paymentDetails() {
        System.out.println("Payment of $" + this.getPaymentAmount());
        System.out.println("        Client " + this.getClientName() + " paid in cash");
        System.out.println("------------------------------------------------");
    }

}
