import java.util.function.Function;

public class Function3
{
    public static void main (String[] args)
    {
        int n=20;
        modify(n, (s) -> s + 100);
    }

    public static void modify(int x, Function<Integer, Integer> fun)
    {
        System.out.println(fun.apply(x));
    }
}
