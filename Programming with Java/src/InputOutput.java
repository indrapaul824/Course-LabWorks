import java.util.Scanner;
import java.io.*;

// Reg. No.: 19MIM10046
// First Java program
public class InputOutput {
	public static void main(String[] args) throws IOException {
		System.out.print("Hello World!\n");

		// Input through Scanner class
		Scanner in = new Scanner(System.in);
		System.out.println("Enter the First Number: ");
		int a = in.nextInt();

		System.out.println("Enter the Second Number: ");
		int b = in.nextInt();

		System.out.println("Addition of two numbers: " + (a + b));

		// Input using BufferedReader class
		BufferedReader obj = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter 3rd Number: ");
		int c = Integer.parseInt(obj.readLine());

		System.out.println("Enter 4th Number: ");
		int d = Integer.parseInt(obj.readLine());

		System.out.println("The addition of these two numbers are: " + (c + d));
	}

}