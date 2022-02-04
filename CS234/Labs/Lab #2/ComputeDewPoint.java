// Thomas Crow
// CS234
// Lab 2 Question 2

import java.util.Scanner;

public class ComputeDewPoint {
    public static void main(String args []) {

        Scanner in = new Scanner(System.in);

        final double a = 17.27;
        final double b = 237.7;

        System.out.print("Relative humidity (between 0 and 1): ");
        double RelativeHumidity = in.nextDouble();
        System.out.print("Temperature (in degrees C): ");
        double Temperature = in.nextDouble();
        double FunctionT_RH = (a * Temperature) / (b + Temperature) + Math.log(RelativeHumidity);
        double DewPoint = (b * FunctionT_RH) / (a - FunctionT_RH);
        System.out.printf("DewPoint: %.2f \n", DewPoint);
        in.close();
    }
}