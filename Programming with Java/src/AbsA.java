abstract class A {
    abstract void hello();
    abstract void callme();
    void showme() {
        System.out.println("I am non-abstract method of Base class");
    }
}

class B extends A {
    @Override
    void hello() {
        System.out.println("Hello, this is B");
    }
    void callme() {
        System.out.println("Calling B");
    }
}

class C extends A {
    @Override
    void hello() {
        System.out.println("Hello, this is C");
    }
    void callme() {
        System.out.println("Calling C");
    }
}

public class AbsA {
    public static void main (String[] args) {
        // For class B
        B b = new B();
        b.callme();
        b.showme();
        b.hello();

        // For class C
        C c = new C();
        c.callme();
        c.showme();
        c.hello();

        // Object of sub-class into reference variable
        A a1 = new B();
        a1.callme();

        a1 = new C();
        a1.callme();
    }
}
