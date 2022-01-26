public class Exercise0_2 {
    public static void main(String args[]) {

        for (int i=0; i<=12; i=i+3)
        {
            System.out.print(i);
            if (i<12)
                System.out.print(", ");
            else
                System.out.println();
        }
    }
}