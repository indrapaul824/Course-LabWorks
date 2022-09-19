import java.util.*;

public class ArrayListDemo
{

    public static void main(String[] args)
    {
        ArrayList obj = new ArrayList();
        for(int i=0;i<10;i++)
        {
            obj.add(i);
        }
        System.out.println(obj);
        System.out.println(""+obj.size());
        obj.remove(3);
        System.out.println(""+obj.size());
        for(int i=0;i< obj.size();i++)
        {
            System.out.println(""+obj.get(i));
        }
        System.out.println("Hello World");
    }
}
