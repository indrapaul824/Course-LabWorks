import java.util.*;

public class DequeDemo
{
    public static void main (String[] args)
    {
        ArrayDeque<String> d1 = new ArrayDeque<>();

        d1.add("1st Data");
        d1.addFirst("2nd Data");
        d1.addLast("3rd Data");
        d1.add("4th Data");

        System.out.println(d1 + "\n");

        d1.remove();
        System.out.println(d1 + "\n");

        d1.removeFirst();
        System.out.println(d1 + "\n");

        d1.removeLast();
        System.out.println(d1 + "\n");
    }
}
