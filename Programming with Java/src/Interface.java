interface Sara
{
    void printing();
}

interface Ibrahim
{
    void print1();
}

public class Interface implements Sara, Ibrahim
{
    public void printing()
    {
        System.out.println("My name is Sara!");
    }
    public void print1()
    {
        System.out.println("My name is Ibrahim!");
    }
	public static void main(String[] args)
	{
		System.out.println("Hello World");
		Sara obj = new Interface();
		Ibrahim obj1 = new Interface();
		obj.printing();
		obj1.print1();
	}
}
