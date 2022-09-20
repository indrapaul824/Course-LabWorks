import java.util.*;

public class VectorsDemo
{
    public static void main (String[] args)
    {
        int size = 2;
        int incr = 1;

        String[] st = {"Hello", "Dear", "Students"};

        Vector<String> v1 = new Vector<>();   // default size=10
        Vector<Integer> v2 = new Vector<>(size);     //constructor
        Vector<Double> v3 = new Vector<>(size, incr);     // constructor

        v1.add("Hello");
        v1.add("My");
        v1.add("Dear");

        System.out.println("V1");
        System.out.println(v1);
        System.out.println(v1.contains("hello"));
        System.out.println(v1.contains("Hello"));
        System.out.println(v1.firstElement());
        System.out.println(v1.lastElement());

        System.out.println("\nV2");
        System.out.println(v2.capacity());
        v2.add(8);
        v2.add(10);
        v2.add(30);

        System.out.println(v2);
        System.out.println(v2.capacity());
        System.out.println(Collections.max(v2) + Collections.min(v2));
        System.out.println(v2.remove(2));
        System.out.println(v2.capacity());


        System.out.println("\nV3");
        System.out.println(v3.capacity());
        v3.add(90.0);
        v3.add(10.50);
        v3.add(20.67);
        System.out.println(v3);
        System.out.println(v3.capacity() + "\n");

        List<String> l1 = new Vector<>(Arrays.asList(st));
        System.out.println(l1);

        System.out.println("\nDefault vector");
        Vector vd = new Vector();
        vd.add(23);
        vd.add("Any String");
        System.out.println(vd);


        System.out.println("\nNum List");
        Integer[] n = {10, 5, 100, 48, 39, 54, 27, 1};
        List<Integer> n1 = new Vector<>(Arrays.asList(n));
        System.out.println(n1);
        List<Integer> n2 = new Vector<>(n1);
        Collections.sort(n2);
        for (Integer a: n1)
        {System.out.print(n2.indexOf(a) + ", ");}
        System.out.println();

    }
}
