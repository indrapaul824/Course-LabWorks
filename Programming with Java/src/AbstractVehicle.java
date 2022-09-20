abstract class Vehicle {
    abstract void engine();

    double computeCost (double c) {
        return (c + 10000);
    }

    void showCost(double c) {
        System.out.println("Cost is: " + c);
    }
}

class V1 extends Vehicle {
    void engine() {
        System.out.println("Engine used is V1");
    }
}

class V2 extends Vehicle {
    void engine() {
        System.out.println("Engine used is V2");
    }
    double computeCost(double c) { return (c + 50000); }
}

public class AbstractVehicle {
    public static void main (String[] args) {
        double c = 100000.0;

        Vehicle v1 = new V1();

        v1.engine();
        v1.showCost(v1.computeCost (c));

        v1 = new V2();
        v1.engine();
        v1.showCost(v1.computeCost (c));

    }
}
