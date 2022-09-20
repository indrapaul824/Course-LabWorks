import java.util.*;
import java.util.stream.*;

public class StreamDemo
{
    public static void main (String[] args)
    {
        // Method 1
        Stream<Integer> stream = Stream.of(1, 2, 3, 4, 5, 6, 7, 8, 9);
        stream.forEach(p -> System.out.print(p*2 + " "));

        System.out.println();

        // Method 2
        List<Integer> l1 = new ArrayList<>();
        for (int i =0; i<10; i++)
        {
            l1.add(i);
        }

        Stream<Integer> stream2 = l1.stream();
        stream2.forEach(p -> System.out.print(p*3 + " "));
        System.out.println();
        System.out.println(l1);

        List<String> students = new ArrayList<>();
        students.add("India");
        students.add("America");
        students.add("Denmark");
        students.add("Russia");
        students.add("Australia");

        Stream<String> stream3 = students.stream();

        students.stream().filter(s -> s.startsWith("A")).forEach(System.out::println);
        students.stream().sorted().filter(s -> s.startsWith("A")).forEach(System.out::println);

    }
}
