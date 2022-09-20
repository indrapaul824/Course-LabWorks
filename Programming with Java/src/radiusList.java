// Name: Indrashis Paul
// Reg: 19MIM10046

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class radiusList
{
    public static void main (String[] args)
    {
        double pi = 3.14;
        Stream<Integer> stream = Stream.of(1, 2, 3, 4, 5, 6, 7, 8, 9);
        List<Double> area = stream.map(r -> pi * r * r).collect(Collectors.toList());

        System.out.println(area);
    }
}
