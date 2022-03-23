/*
* Thomas Crow
* Lab #8 
* CS234
*/

public class Payment {

//  Declaration of instance variables
    private double paymentAmount;

//  Default constructor
    public Payment(Double amount) {
         setPaymentAmount(amount); 
    }

//  Method: getPaymentAmount
//  Purpose: Get the amount of the payment
//  Arguments: None
//  Returns: The amount of the payment as a double

    public double getPaymentAmount() {
        return this.paymentAmount;
    }

//  Method: setPaymentAmount
//  Purpose: Modify payment amount
//  Arguments: Payment amount as a double
//  Returns: None

    public void setPaymentAmount(double payment) {
        this.paymentAmount = payment;
    }

//  Method: paymentDetails()
//  Purpose: Prints to user the details of the payment
//  Arguments: None
//  Returns: None

    public void paymentDetails() {
        System.out.println("Payment of $" + this.getPaymentAmount());
    }
}
