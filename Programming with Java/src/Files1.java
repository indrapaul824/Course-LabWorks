import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.*;
import java.util.List;

public class Files1 {
    public static void main (String[] args) throws IOException {
        char[] arr = new char[200];

        //Using NIO package
        Path p1 = Paths.get ("D:\\Projects\\Programming In Java\\src\\Files.txt");
        System.out.println (p1);

        Files.createFile (p1);

        List<String> l1 = Files.readAllLines (p1);
        System.out.println (l1);

        //Using IO package
        File file1 = new File("File.txt"); // in workspace folder
        boolean x = file1.createNewFile ();

        if(x) {
            System.out.println ("The file is created!");
        }
        else {
            System.out.println ("The file already exists!");
        }

        //III
        FileReader content = new FileReader (file1);
        content.read (arr);
        System.out.println (arr);
        content.close ();

        Files.delete(p1);
    }
}
