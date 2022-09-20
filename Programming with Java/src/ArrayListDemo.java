import java.util.*;

public class ArrayListDemo
{
    public static void main (String[] args)
    {
        ArrayList<String> a1 = new ArrayList<> ();

        a1.add("Mumbai");
        a1.add("California");
        a1.add("Sydney");
        a1.add("London");


        System.out.println("Size of a1: " + a1.size());
        System.out.println(a1);

        System.out.println("Does a1 contain 'Mumbai'? -->" + a1.contains("Mumbai"));
        System.out.println("Does a1 contain 'mumbai'? -->" + a1.contains("mumbai"));

        for (String a: a1)
        {System.out.print(a1.indexOf(a) + ", ");}
        System.out.println();

        ArrayList<String> a2 = new ArrayList<> (a1);
        Collections.sort(a2);
        System.out.println(a2);
        for (String a: a1)
        {System.out.print(a2.indexOf(a) + ", ");}
        System.out.println();

        a1.add("Singapore");
        System.out.println(a1);

        String[] balls = {"football", "baseball", "basketball", "volleyball"};

        // ArrayList<String> a3 = new ArrayList<>(Arrays.asList(balls));
        List<String> a3 = Arrays.asList(balls);
        System.out.println(a3);

    }
}
