import java.util.*;

public class TreeSetDemo
{
    public static void main (String[] args)
    {
        TreeSet<String> t1 = new TreeSet<>();

        t1.add("1st Data");
        t1.add("2nd Data");
        t1.add("3rd Data");
        t1.add("4th Data");

        System.out.println(t1 + "\n");

        t1.remove("2nd Data");
        System.out.println(t1 + "\n");

        System.out.println("Size = " + t1.size() + "\n");

        System.out.println(t1.ceiling("3rd Data"));
    }
}
