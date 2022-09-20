import java.io.*;
import java.util.*;

public class ReadConsole
{
    public static void main (String[] args) throws IOException
    {
        // 1
        InputStreamReader in = null;
        in = new InputStreamReader (System.in);
        System.out.println ("Enter your characters: ");
        char c = (char) in.read();
        System.out.println (c);

        // 2a
        InputStreamReader in1 = null;
        in1 = new InputStreamReader (System.in);
        BufferedReader br1 = new BufferedReader (in1);
        System.out.println ("Enter more characters: ");
        char c1 = (char) br1.read();
        System.out.println (c1+"es");

        // 2b
        InputStreamReader input = new InputStreamReader (System.in);
        BufferedReader br2 = new BufferedReader (input);
        String s = br2.readLine ();
        int n = Integer.parseInt (s);
        System.out.println (n);


    }
}
