final class Person
{
    private final int pan;
    public Person(int p)
    {
        this.pan = p;
    }
    int getPan()
    {
        return pan;
    }
}

public class Immutable1
{
    public static void main (String[] args)
    {
        Person p = new Person(123456);
        System.out.println(p.getPan());
    }
}
