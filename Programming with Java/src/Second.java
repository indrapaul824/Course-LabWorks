import java.io.*;

public class Second
{
    public static void main(String[] args) throws IOException
    {
        InputStreamReader istream = new InputStreamReader(System.in);
        BufferedReader bufRead = new BufferedReader(istream);

        System.out.println("Welcome to my Second Java Program!");
        System.out.println("Please enter your first name: ");

        String firstName = bufRead.readLine();

        System.out.println("Please enter the year you were born in: ");

        String bornYear = bufRead.readLine();

        System.out.println("Hello "+firstName+"\nD.O.B.:"+bornYear);
    }

}
