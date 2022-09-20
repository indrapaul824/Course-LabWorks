import java.util.Arrays;

public class Array1
{
    public static void main (String[] args)
    {
        // Initializing arrays
        int size = 9;
        int[] ar1 = {1, 2, 3, 4, 5, 10};
        int []ar2 = {7, 8, 9, 12, 16};
        double ar3[] = {12.5, 2.6, 3.7, 9.3, 45.2, 36.5};

        double[] ar4 = new double[size];
        char []ar5 = {'I', 'N', 'D', 'R', 'A'};

        // Usage of array.length method
        int l = ar1.length;
        System.out.println("Length of array1: " + l);

        // Standard For loop method
        int i;
        System.out.print("The elements of array3 are: ");
        for(i=0; i <= ar3.length - 1; i++)
        {
            System.out.print(ar3[i] + ", ");
        }

        // For-each method
        System.out.print("\nThe elements of array5 are: ");
        for(char k : ar5)
        {
            System.out.print(k + ", ");
        }

        int[] A = new int[] {12, 24, 48, 60};
        int[] B = new int[] {12, 24, 48, 65};

        boolean result = Arrays.equals(A, B);
        System.out.println("\nAre the arrays equal? " + result);
    }
}
