import java.awt.*;
import java.awt.event.*;


public class CheckboxDemo extends Frame implements ActionListener
{
    Checkbox c1, c2, c3;
    Button b2;
    CheckboxDemo()
    {
        setVisible(true);
        setSize(500, 500);
        setBackground(Color.GRAY);
        c1 = new Checkbox("C++");
        c2 = new Checkbox("Java", true);
        c3 = new Checkbox("Python");
        b2 = new Button("Close");
        setLayout(new FlowLayout());
        add(c1);add(c2);add(c3);
        b2.addActionListener(this);
        add(b2);
    }

    public void actionPerformed(ActionEvent ae)
    {
        if(ae.getSource() == b2)
        {
            dispose();
            System.out.println("The GUI has stopped!");
        }
    }

    public static void main(String[] args)
    {
        System.out.println("The GUI is running!");
        CheckboxDemo obj = new CheckboxDemo();
    }
}
