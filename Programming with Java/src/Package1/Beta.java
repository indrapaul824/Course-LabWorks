package Package1;

public class Beta {
    protected int b;

    Beta() {
        b = 0;
    }

    public void setB(int b) {
        this.b = b;
    }

    public int getB() {
        return b;
    }

    public static void main (String[] args) {
        Beta beta = new Beta();
    }
}
