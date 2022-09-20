import java.io.*;

public class Third
{
    public static void main(String[] args) throws IOException
    {
        InputStreamReader istream = new InputStreamReader(System.in);
        BufferedReader bufRead = new BufferedReader(istream);

        System.out.println("Welcome to my Third Java Program!");

        System.out.println("Please enter your first name: ");
        String firstName = bufRead.readLine();

        System.out.println("Please enter the year you were born in: ");
        String bornYear = bufRead.readLine();

        System.out.println("Please enter the Current Year: ");
        String currYear = bufRead.readLine();

        System.out.println("Hello "+firstName+"\nD.O.B.:"+bornYear);

        int born = Integer.parseInt(bornYear);
        int curr = Integer.parseInt(currYear);
        int age = curr - born;

        System.out.println("Your age is: " + age);
    }

}