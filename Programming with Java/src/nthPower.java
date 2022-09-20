import java.util.*;

public class nthPower
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number and exponent:");
        int n = sc.nextInt();
        int e = sc.nextInt();
        int res = 1;

        for(int i=0; i<e; i++)
        {
            res *= n;
        }

        System.out.println("The result from for loop is: " + res);
        System.out.println("The result from Math.pow is: " + Math.pow(n, e));
    }
}
