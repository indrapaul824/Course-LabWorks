import java.util.Scanner;
public class Scanner_Intro
{
	public static void main(String[] args) 
	{
	    Scanner in = new Scanner(System.in);
		System.out.println("Hello World");
		
		// Integer Variable
		int a;
		a = in.nextInt();
		System.out.println("The value of a is: " + a);
		
		// Integer Array
		int[] A = new int[12];
		
		for(int i=0;i<12;i++)
		{
		    A[i] = in.nextInt();
		}
		
		System.out.println("The values in the array are: \n");
		for(int i=0;i<12;i++)
		{
		    System.out.println(A[i]);
		}
	}
}
