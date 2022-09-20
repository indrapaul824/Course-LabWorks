interface Animal {
    public static final String tname = " Hello";
    void name(String tname);
    void speed();
    
    default void show() {
        System.out.println("Hello! I am default method");
    }
}
interface FastAnimal {
    void run();
}

class Tiger implements Animal, FastAnimal {

    @Override
    public void name(String tname) {

    }

    public void speed() {
        System.out.println("Tiger's speed is 30-50 Km/h");
    }
    
    public void run() {
        System.out.println("I am a fast Animal");
    }
}

public class InterfaceSample {
    public static void main (String[] args) {
        Tiger t1 = new Tiger();
        t1.speed();
        t1.run();

        Animal a1 = new Tiger();

        a1.speed();
    }
}
