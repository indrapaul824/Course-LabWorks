import java.util.*;

// Functional interface
interface MyInterface1
{
    String sayHello(); // Method with no parameter
}

// Functional Interface
interface AreaC
{
    double areaCircle(int i); // Method with a single parameter
}

// Functional Interface
interface AreaR
{
    double areaRect(int l, int b); // Method with a double parameter
}

// Driver class
public class Lambda2
{
    public static void main (String[] args)
    {
        MyInterface1 msg = () -> "Hello Everyone!";

        double pi = 3.14;
        AreaC a1 = (r) -> pi * r * r;

        AreaR a2 = (l, b) -> l*b;

        System.out.println("The message is: " + msg.sayHello());
        System.out.println("Area of circle is: " + a1.areaCircle(6));
        System.out.println("Area of rectangle is: " + a2.areaRect(2, 3));

        List<String> list = new ArrayList<> ();
        list.add("ankit");
        list.add("manky");
        list.add("irfan");
        list.add("jai");

        list.forEach (System.out::println);
        // list.forEach ((n) -> System.out.println (n));
    }
}
