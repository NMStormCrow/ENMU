public class Exercise1_4 {
    public static void main(String args[]) 
    {
        for (int i=0; i<5; i++)
        {
            for (int j=0; j<=4; j++)
            {
                if (j<4)
                    System.out.print("*");
                else
                    System.out.println();
            }
        }
    }
}