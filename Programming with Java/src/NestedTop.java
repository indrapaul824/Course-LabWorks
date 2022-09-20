/*
abstract class ShapeX {
    public abstract void area();
    private double pi = 3.141;

    public class Circle1 extends ShapeX {   //non-static or inner class begins here
        double radius;

        Circle1(double radius) {
            this.radius = radius;
        }
        @Override
        public void area () {
            System.out.println("Circle Area = " + (pi * radius * radius));
        }
    }  // Circle1 ends here

    public static class Rectangle1 extends ShapeX {   //static nested class (nested-top level class)
        int length, breadth;

        Rectangle1(int length, int breadth) {
            this.length = length;
            this.breadth = breadth;
        }

        @Override
        public void area () {
            System.out.println("Rectangle Area = " + length * breadth);
        }
    }  // Rectangle1 ends here

}   // Top-level class ends here
*/

//Nested Top classes
abstract class ShapeX {										//Top level class is ShapeX
    public abstract void area();							//abstract method should be there
    private double pi = 3.141;
    public class Circle1 extends ShapeX {                  //non-static or inner class begins here
        double r;
        Circle1(double r){									//Constructor
            this.r = r ;
        }
        public void area() {                                         // method.
            System.out.println("Circle area ="+(pi*r*r));
        }
    }	//Circle1 ends here
    public static class Rectangle1 extends ShapeX { 			//static nested class (nested-top level class)
        int length;
        int breadth;
        Rectangle1(int length, int breadth){
            this.breadth = breadth;
            this.length = length;
        }
        public void area() {										//overridden method
            System.out.println("Rectangle area ="+length*breadth);
        }
    } //static nested class end here.
} // Top-level class ends here

public class NestedTop {
    public static void main(String[] args) {
        ShapeX aShape = new ShapeX.Rectangle1 (12, 13);  // Reference object of abstract class
        aShape.area ();


        ShapeX.Circle1 c1 = aShape.new Circle1(2.0);
        c1.area ();

        // Object of nested top class and inner class can exist individually.
        /*
        Rectangle1 r1 = new Rectangle1 (4, 6);
        r1.area();
        Circle1 c2 = new Circle1 (3.0);
        c2.area();*/
    }
}
