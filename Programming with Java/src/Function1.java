import java.util.*;
import java.util.function.Function;

public class Function1
{
    public static void main (String[] args)
    {
        List<Integer> l1 = new ArrayList<>();
        l1.add(16);
        l1.add(14);

        Function<Integer, Integer> fun = val -> val + 100;

        for (Integer i : l1)
        {
            System.out.println(fun.apply(i));
        }
    }
}
