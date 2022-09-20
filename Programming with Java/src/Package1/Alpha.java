package Package1;

public class Alpha {
    public int a;
    private String n;

    public Alpha(int a, String n) {
        this.a = a;
        this.n = n;
    }

    public void setA(int a) {
        this.a = a;
    }

    public int getA() {
        return a;
    }

    private void setN(String n) {
        this.n = n;
    }

    private String getN() {
        return n;
    }

    public static void main (String[] args) {
        Alpha alpha = new Alpha(12, "IPaul");
        System.out.println(alpha.getN() + "-->" + alpha.getA());
    }
}
