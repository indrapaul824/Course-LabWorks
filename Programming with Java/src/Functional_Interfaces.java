import org.jetbrains.annotations.NotNull;

import java.util.function.*;
import java.util.*;

public class Functional_Interfaces
{
    public static void main (String[] args)
    {
        // Predicate --> Boolean
        Predicate<String> p1 = (p) -> p.length() > 7;

        System.out.println(p1.test("Successfully"));
        System.out.println(p1.test("Success"));

        List<String> l = new ArrayList<>();
        l.add("successfully");
        l.add("easy");
        l.add("grateful");
        l.stream().filter(p1).forEach (System.out::println);

        // Supplier --> Provides values
        int n = 3;
        display(() -> n + 10);
        display(() -> n + 100);
    }
    static void display(@NotNull Supplier<Integer> supplier) {
        System.out.println(supplier.get());
    }
}
