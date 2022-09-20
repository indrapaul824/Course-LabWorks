public class Varargs {
    public int sum(double ... args) {
        System.out.println("No. of args entered: " + args.length);
        int sum = 0;
        for(double i: args) {
            sum += i;
        }
        return sum;
    }

    public static void main (String[] args) {
        Varargs v = new Varargs();
        double v1 = v.sum(12, 23);
        System.out.println("Sum = " + v1);
        double v2 = v.sum(12, 15, 19, 15, 89);
        System.out.println("Sum = " + v2);
    }
}
