import java.util.Scanner;

public class IllegalArgumentExceptionSample {
    static void setPercentage (int p) {
        try {
            if (p < 0 || p > 100) {
                throw new IllegalArgumentException ("Given input is invalid!");
            }
            else {
                System.out.println("Value of Percentage is validated!");
            }
        } catch (IllegalArgumentException e) {
            e.printStackTrace ();
        }
    }

    public static void main (String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Enter the value of the Percentage: ");
        int percent = in.nextInt();
        setPercentage(percent);

    }
}
