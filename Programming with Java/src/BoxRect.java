class Box
{
    public double volume(double l, double b, double h)
    {
        return l*b*h;
    }
}

class BoxRect
{
    public static void main(String[] args)
    {
        Box b1 = new Box();

        double rectVolume = b1.volume(5, 6, 7);
        System.out.println("The volume of the box is: " + rectVolume);
    }
}
