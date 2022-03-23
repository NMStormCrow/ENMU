public class paymentTester {
    
    public static void main(String[] args) {
        //Payment
        Payment pay1 = new Payment(13.95);

        //Two cash payments
        Payment cash1 = new CashPayment(99.99, "Emma");
        Payment cash2 = new CashPayment(15.60, "John");

        //Two credit card payments
        CreditCardPayment credit1 = new CreditCardPayment(56.50, "********678", "06/22");
        CreditCardPayment credit2 = new CreditCardPayment(19.65, "********123", "07/25");

        //Show details for each payment
        pay1.paymentDetails();
        cash1.paymentDetails();
        cash2.paymentDetails();
        credit1.paymentDetails();
        credit2.paymentDetails();
    }
}
