package Package2;

import Package1.Alpha;

public class AlphaSub extends Alpha {
    int as;

    AlphaSub(int a, String n, int as) {
        super(a, n);
        this.as = as;
    }

    public void setAs(int as) {
        this.as = as;
    }

    public int getAs() {
        return as;
    }

    public static void main (String[] args) {
        AlphaSub alphaSub = new AlphaSub(12, "CPaul", 21);
        System.out.println(alphaSub.getAs() + alphaSub.getA());
    }
}
