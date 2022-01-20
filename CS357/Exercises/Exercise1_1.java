public class Exercise1_1 {
    public static void main(String args []) {

        for (int i=0; i<=10; i=i+2)
        {
            System.out.print(i);
            if (i<10)
                System.out.print(", ");
            else
                System.out.println();
        }
    }
}