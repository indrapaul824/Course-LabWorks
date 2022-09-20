import java.nio.file.*;
import java.io.*;
import java.util.List;
import java.util.stream.*;

public class FileWrite {
    public static void main(String[] args) {
        Stream<String> stream;
        
        try
        {
            File f1 = new File("D:\\myFile.txt");
            boolean status = f1.createNewFile();
            if (status) {
                System.out.println("File created successfully: " + f1.getPath());
                String str = "Write this string to my file";
                FileWriter fw = new FileWriter(f1);
                fw.write(str);
                fw.close();
            }
            else
                System.out.println("The file already exists: " + f1.getPath());

            Path p1 = Paths.get("D:\\myFile.txt");
            List<String> l1 = Files.readAllLines(p1);
            System.out.println(l1);

            stream = Files.lines(p1);
            stream.forEach(System.out::println);
            stream.close();
        } catch (IOException e) 
        {
            e.printStackTrace();
        }
    }
}
