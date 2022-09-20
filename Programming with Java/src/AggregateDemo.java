class Engine
{
    public void work()
    {
        System.out.println("Engine Works");
    }
}

final class Car
{
    private Engine engine; //--> Aggregation
    // private final Engine1 engine; //--> Composition. Engine is a must attribute in car.
    Car(Engine engine)
    {
        this.engine = engine;
    }

    public void move()
    {
        engine.work();
        System.out.println("Car is moving");
    }
}


public class AggregateDemo
{
    public static void main (String[] args)
    {
        Engine e1 = new Engine();
        Car c1 = new Car(e1);

        c1.move();
    }
}
