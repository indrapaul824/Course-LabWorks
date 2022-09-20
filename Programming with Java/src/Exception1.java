import java.lang.ArithmeticException;
import java.util.*;

public class Exception1
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);

        int z = 0;

        System.out.println("Enter two values for division: ");
        int x = in.nextInt();
        try {
            int y = in.nextInt ();
            z = x / y;
        }

        catch (ArithmeticException e) {
            System.out.println("/ by zero is not allowed. Please change y.");
        }

        finally
        {
            System.out.println("This will be executed besides exception!");
        }

        System.out.println("Result = " + z);
    }
}
