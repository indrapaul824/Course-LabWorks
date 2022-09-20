abstract class Shape1
{
    abstract void draw();
    abstract void erase();
}

class Circle1 extends Shape1
{
    @Override
    void draw () {
        System.out.println("Draw a Circle");
    }

    @Override
    void erase () {
        System.out.println("Erase a drawn Circle");
    }
}

class Triangle extends Shape1
{
    @Override
    void draw () {
        System.out.println("Draw a Triangle");
    }

    @Override
    void erase () {
        System.out.println("Erase a drawn Triangle");
    }
}

class Square extends Shape1
{
    @Override
    void draw () {
        System.out.println("Draw a Square");
    }

    @Override
    void erase () {
        System.out.println("Erase a drawn Square");
    }
}

public class submit3 {
    public static void main (String[] args)
    {
        Shape1 s1 = new Circle1 ();
        s1.draw ();
        s1.erase ();

        Square s2 = new Square ();
        s2.draw ();
        s2.erase ();

        Triangle s3 = new Triangle ();
        s3.draw ();
        s3.erase ();
    }
}
