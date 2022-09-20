class PurchaseItem
{
    private final String name;
    private double unitPrice;

    PurchaseItem()
    {
        name = "no item";
        unitPrice = 0.0;
    }

    PurchaseItem(String name, double unitPrice)
    {
        this.name = name;
        this.unitPrice = unitPrice;
    }

    public double getPrice()
    {
        return unitPrice;
    }

    public String getName()
    {
        return name;
    }

    public void setUnitPrice(double unitPrice)
    {
        this.unitPrice = unitPrice;
    }

    @Override
    public String toString()
    {
        return "PurchaseItem{" +
                "name='" + name + '\'' +
                ", unitPrice=" + unitPrice +
                '}';
    }
}

class WeighedItem extends PurchaseItem
{
    private final double weight;

    WeighedItem(String name, double unitPrice, double weight)
    {
        super(name, unitPrice);
        this.weight = weight;
    }

    public double getUnitPrice()
    {
        return (super.getPrice() * weight);
    }

    @Override
    public String toString() {
        return "WeighedItem{" +
                "name='" + super.getName() + '\'' +
                ", unitPrice=" + super.getPrice() +
                ", weight=" + weight +
                ", weighted price=" + getUnitPrice() +
                '}';
    }
}

class CountedItem extends PurchaseItem
{
    private final int quantity;
    CountedItem(String name, double unitPrice, int quantity)
    {
        super(name, unitPrice);
        this.quantity = quantity;
    }

    public double getUnitPrice()
    {
        return (super.getPrice() * quantity);
    }

    @Override
    public String toString() {
        return "CountedItem{" +
                "name='" + super.getName() + '\'' +
                ", unitPrice=" + super.getPrice() +
                ", count=" + quantity +
                ", counted price=" + getUnitPrice() +
                '}';
    }
}


public class submit2_2
{
    public static void main (String[] args)
    {
        WeighedItem b1 = new WeighedItem("Banana", 3.00, 1.37);
        System.out.println(b1);

        CountedItem p1 = new CountedItem("Pens", 4.5, 10);
        System.out.println(p1);
    }
}


