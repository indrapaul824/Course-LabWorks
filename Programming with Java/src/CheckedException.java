import java.io.*;

public class CheckedException {
    public static void main(String[] args) throws IOException
    {
        FileInputStream f = null;

        f = new FileInputStream("C:\\Users\\indra\\Programming In Java\\src\\java.txt");
        int k;

        while ((k = f.read ()) != -1)
        {
            System.out.print((char)k);
        }

        f.close ();
    }
}
