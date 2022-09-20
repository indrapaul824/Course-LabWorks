import java.awt.*;

public class Lambda1
{
    public static void main (String[] args)
    {
        Frame frame = new Frame("ActionListener java8");
        Button b = new Button("Click Here");
        Button b1 = new Button("Say Hi!");
        Button b2 = new Button("Close");
        b.setBounds(50, 130, 80, 50);
        b1.setBounds(20, 40, 50, 80);
        b2.setBounds(80, 40, 40, 40);

        // Lambda expression passed as an argument
        b.addActionListener(e -> System.out.println("Hello World!"));
        b1.addActionListener(e -> System.out.println("Hi All!"));
        b2.addActionListener(e -> frame.dispose());

        frame.add(b);   // Add button to frame
        frame.add(b1);
        frame.add(b2);
        frame.setSize(200, 200);
        frame.setLayout(null);
        frame.setVisible(true);
    }
}
