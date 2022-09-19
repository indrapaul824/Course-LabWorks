class Root
{
	public void Print() 
	{
		System.out.println("Hello World");
	}
}

class Add extends Root
{
    public void addition(int a, int b)
    {
        System.out.println(a+b);
    }
}

class ClassInheritence extends Add
{
    public void subtraction(int x, int y)
    {
        System.out.println(x-y);
    }
    public static void main(String[] args)
    {
        ClassInheritence in = new ClassInheritence();
        in.addition(20, 10);
        in.subtraction(20, 10);
        in.Print();
    }
}
