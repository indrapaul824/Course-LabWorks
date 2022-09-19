import java.util.Scanner;

public class StringConcat
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        String a;
        String b;
        a = in.nextLine();
        b = in.nextLine();
        System.out.println("Result: " + (a+b));
    }
}
