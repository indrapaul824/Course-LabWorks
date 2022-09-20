import java.util.Arrays;

public class ArrayNum
{
    public static void main (String[] args)
    {
        int[] A = new int[] {100, 200, 150, 240, 30, 60};
        Arrays.sort(A);
        System.out.println("The largest element is: " + A[A.length-1]);

        int sum = Arrays.stream(A).sum();
        System.out.println("The sum of the elements is: " + sum);
    }
}
