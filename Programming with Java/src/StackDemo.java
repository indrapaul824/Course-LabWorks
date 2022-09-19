import java.util.*;
public class StackDemo
{
    public static void main(String[] args)
    {
        Stack obj = new Stack();
        obj.push('a');
        obj.push('b');
        obj.push('c');

        System.out.println(""+obj);

        obj.pop();
        System.out.println(""+obj);
    }
}
