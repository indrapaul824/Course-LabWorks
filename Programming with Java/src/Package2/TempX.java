package Package2;
import Package1.*;

public class TempX extends TempJ{
    public static void main (String[] args) {
        System.out.println(temp);
        TempX.printHello();
        TempH.printTemp();
    }
}
