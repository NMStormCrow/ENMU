import java.util.Scanner;

public class Exercise1_1 {
    public static void main(String args[]) {
        
        Scanner scan = new Scanner(System.in);
        System.out.print("How many hours did you work? ");
        double HoursWorked = scan.nextDouble();
        System.out.print("How much do you get paid per hour? ");
        double HourlyWage = scan.nextDouble();
        double MoneyEarned = HoursWorked * HourlyWage;
        System.out.println("You have earned $" + String.format("%.2f",MoneyEarned));
        scan.close();
    }
}