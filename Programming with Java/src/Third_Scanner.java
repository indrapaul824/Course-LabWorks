import java.io.*;
import java.util.*;

public class Third_Scanner
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter your name:");
        String name = sc.nextLine();
        System.out.println("Enter no.:");
        int num = sc.nextInt();

        System.out.println("The first character of your name is: " + name.charAt(0));
        System.out.println("The square of number = " + (num*num));
    }
}
