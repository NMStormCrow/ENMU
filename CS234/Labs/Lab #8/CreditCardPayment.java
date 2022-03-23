/*
* Thomas Crow
* Lab #8 
* CS234
*/

public class CreditCardPayment extends Payment {

//  Declaration of instance variables
    private String cardNumber = new String();
    private String expirationDate = new String();

//  Default constructor
    public CreditCardPayment(double value, String cardNumber, String cardExpiration) {
        super(value);
        this.cardNumber = cardNumber;
        this.expirationDate = cardExpiration;
    }
    
//  Method:  getCardNumber
//  Purpose: Get the number of the credit card
//  Arguments: None
//  Returns: The number of the credit card as a string

    public String getCardNumber() {
        return this.cardNumber;
    }

//  Method:  getCardExpriation
//  Purpose: Get the expiration date of the credit card
//  Arguments: None
//  Returns: The expiration date in a String value

    public String getCardExpiration() {
        return this.expirationDate;
    }

//  Method:  paymentDetails
//  Purpose: Print the details of the payment
//  Arguments: None
//  Returns: None

    public void paymentDetails() {
        super.paymentDetails();
        System.out.println("        Using the card " + this.getCardNumber() + ", with expiration date " + getCardExpiration());
        System.out.println("------------------------------------------------");
    }
}
