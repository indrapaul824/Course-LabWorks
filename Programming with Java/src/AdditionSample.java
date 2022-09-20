import java.util.Scanner;

public class AdditionSample {
    static int add (int a, int b)
    {
        return a+b;
    }

    static double add (double x, double y)
    {
        return x+y;
    }

    static int[][] add (int[][] A, int[][] B, int n)
    {
        int i, j;
        int[][] C = new int[n][n];

        for (i = 0; i < n; i++)
            for (j = 0; j < n; j++)
                C[i][j] = A[i][j] + B[i][j];

        return C;
    }

    public static void main (String[] args) {
        Scanner in = new Scanner (System.in);

        System.out.println (add(23, 15));
        System.out.println (add(40.74, 76.201));

        System.out.println ("Enter the size: ");
        int n = in.nextInt ();

        int[][] A = new int[n][n];
        int[][] B = new int[n][n];


        System.out.println("Enter the elements of matrix A");
        for (int i= 0 ; i < n ; i++ )
        {
            for (int j= 0 ; j < n ;j++ )
                A[i][j] = in.nextInt();
        }

        System.out.println("Enter the elements of matrix B");
        for (int i= 0 ; i < n ; i++ )
        {
            for (int j= 0 ; j < n ;j++ )
                B[i][j] = in.nextInt();
        }

        int[][] C;
        C = add(A, B, n);

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
                System.out.print(C[i][j] + " ");
            System.out.println();
        }
    }

}
