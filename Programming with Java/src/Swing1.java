import javax.swing.*;

public class Swing1
{
    public static void main(String[] args)
    {
        String s1, s2;
        int a, b, n;

        s1 = JOptionPane.showInputDialog("Enter First Number: ");
        a = Integer.parseInt(s1);

        s2 = JOptionPane.showInputDialog("Enter Second Number: ");
        b = Integer.parseInt(s2);

        n = a + b;
        JOptionPane.showMessageDialog(null, "The sum is: "+n, "Results", JOptionPane.PLAIN_MESSAGE);
        System.exit(0);
    }
}
