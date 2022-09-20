/*
1. When we have several classes that are closely related to
each other and we want to share the same code among them
2. When we want to declare objects whose state can be
accessed or modified (non-final)
*/

abstract class GraphicObject {
    abstract void dim();
    abstract void shape();
    void Graphic() {
        System.out.println("I am a Graphic Object!");
    }
}

class Circle extends GraphicObject {
    void dim() {
        System.out.println("Radius");
    }
    void shape() {
        System.out.println("I am a Circle");
    }
}
class Rectangle extends GraphicObject {
    void dim() {
        System.out.println("Length and Breadth");
    }
    void shape() {
        System.out.println("I am a Rectangle");
    }
}
class Line extends GraphicObject {
    void dim() {
        System.out.println("Length");
    }
    void shape() {
        System.out.println("I am a Line");
    }
}
class Bezier extends GraphicObject {
    void dim() {
        System.out.println("X and Y coordinates");
    }
    void shape() {
        System.out.println("I am a Bezier Curve");
    }
}


public class submit {
    public static void main (String[] args) {
        GraphicObject g = new Circle();
        g.Graphic();
        g.dim();
        g.shape();

        System.out.println("\n");

        g = new Rectangle();
        g.Graphic();
        g.dim();
        g.shape();

        System.out.println("\n");

        g = new Line();
        g.Graphic();
        g.dim();
        g.shape();

        System.out.println("\n");

        g = new Bezier();
        g.Graphic();
        g.dim();
        g.shape();

    }
}
