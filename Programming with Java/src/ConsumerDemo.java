import java.util.function.Consumer;
import java.util.*;


class Product
{
    private double price = 0.0;

    public void setPrice(double price) {
        this.price = price;
    }

    public double getPrice() {
        return price;
    }

    public void print() {
        System.out.println("Product{" +
                "price=" + price +
                '}');
    }
}

public class ConsumerDemo
{
    public static void main (String[] args)
    {
        Consumer<Product> xyz = p -> p.setPrice(5.9); //lambda expression

        Product p1 = new Product();

        List<Product> p2 = new ArrayList<>();
        p2.add(new Product());

        xyz.accept(p1);
        p1.print();
    }
}
