public class ConstructorDemo
{
    ConstructorDemo()
    {
        System.out.println("Default Constructor");
    }

    ConstructorDemo(int a, int y)
    {
        System.out.println("Parametric Constructor");
        System.out.println(""+(a+y));
    }

    ConstructorDemo(int x, int y, int z)
    {
        System.out.println("Parametric Constructor");
        System.out.println(""+(x+y+z));
    }

    public static void main(String[] args)
    {
        new ConstructorDemo();
        new ConstructorDemo(2, 3);
        new ConstructorDemo(10, 20, 30);
    }
}
