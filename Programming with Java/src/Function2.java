import java.util.function.DoubleToIntFunction;
import java.util.function.Supplier;

public class Function2
{
    public static void main (String[] args)
    {
        DoubleToIntFunction d1 = s -> (int) s;

        System.out.println(d1.applyAsInt(100.056));
    }
}
