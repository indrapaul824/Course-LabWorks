package Package1;

public class TempJ
{
    protected static int temp = 5;

    protected static void printHello() {
        System.out.println("Hello, I am the protected method of the Base class!");
    }

    public static class TempH {
        private static final int temp = 6;

        public static void printTemp() {
            System.out.println(temp);
        }
    }
}
