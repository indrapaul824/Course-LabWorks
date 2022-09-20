import java.util.*;

public class NumAsterisk
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);

        int[] num = new int[5];
        System.out.println("Enter 5 numbers between 1 and 30:");
        for(int i=0;i<5;i++)
        {
            int n = in.nextInt();
            if(n>0 && n<31)
            {
                num[i] = n;
            }
        }

        for (int k : num)
        {
            if (k != 0)
            {
                System.out.print(k + " --> ");
                for (int j = 0; j < k; j++)
                {
                    System.out.print("*");
                }
                System.out.println();
            }
        }
    }
}
