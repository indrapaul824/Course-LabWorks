import java.nio.file.*;
import java.io.*;

public class PathUsage {
    public static void main (String[] args) throws IOException {
        char[] arr = new char[200];
        File f1 = Paths.get("Files.txt").toFile ();
        Path p1 = Paths.get ("C:\\Users\\indra\\Programming In Java\\src");
        System.out.println (p1);
        System.out.println (f1);

        final String HOME = System.getProperty("user.home");
        System.out.println(HOME);

        File f2 = new File("PathUsageFile1.txt");
        boolean status = f2.createNewFile();
        if (status)
            System.out.println("The new file is created: " + f2.getName());
        else
            System.out.println("The file already exists: " + f2.getName());

        FileReader content = new FileReader(f2);
        content.read(arr);
        System.out.println(arr);
        content.close();
    }
}
