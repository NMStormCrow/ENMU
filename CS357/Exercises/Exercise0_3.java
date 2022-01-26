public class Exercise0_3 {
    public static void main(String args[]) {

        for (int i=11; i>=1; i=i-2)
        {
            System.out.print(i);
            if (i>1)
                System.out.print(", ");
            else
                System.out.println();
        }
    }
}