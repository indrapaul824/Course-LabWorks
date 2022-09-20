import java.lang.ArithmeticException;
import java.util.*;

public class PasswordException
{
    static void checkPwd(int pwd)
    {
        if (pwd!=12345) {
            System.out.println ("Invalid Password!");
            throw new ArithmeticException("......Access Denied......");
        }
        else
            System.out.println("Password Validated! You may proceed.");
    }

    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("************* Sign In *************\nEnter your password: ");

        try {
            int x = in.nextInt();
            checkPwd (x);   // static method called without object
        }
        finally {
            System.out.println("End of process!");
        }
    }
}
