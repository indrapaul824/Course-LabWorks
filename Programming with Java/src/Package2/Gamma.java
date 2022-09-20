package Package2;

public class Gamma extends AlphaSub {
    int g;

    Gamma(int a, String n, int as, int g) {
        super(a, n, as);
        this.g = g;
    }

    public void setG(int g) {
        this.g = g;
    }

    public int getG() {
        return g;
    }
}
