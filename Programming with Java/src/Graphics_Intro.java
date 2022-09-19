import java.awt.*;
import java.awt.event.*;

public class Graphics_Intro extends Frame implements ActionListener
{
    Button b1, b2, b3, b4;
    TextField t1;
    Graphics_Intro()
    {
        setVisible(true);
        setSize(200, 200);
        b1 = new Button("RED");
        b2 = new Button("GREEN");
        b3 = new Button("BLUE");
        b4 = new Button("Close");
        t1 = new TextField(20);
        
        setBackground(Color.BLUE);
        setLayout(new FlowLayout());
        add(b1);add(b2);add(b3);add(b4);add(t1);
        
        b1.addActionListener(this);
        b2.addActionListener(this);
        b3.addActionListener(this);
        b4.addActionListener(this);
    }
    
    public void actionPerformed(ActionEvent ae)
    {
        if(ae.getSource()==b1){setBackground(Color.RED);}
        if(ae.getSource()==b2){setBackground(Color.GREEN);}
        if(ae.getSource()==b3){setBackground(Color.BLUE);}
        if(ae.getSource()==b4){dispose();}
    }
    
	public static void main(String[] args) 
	{
        new Graphics_Intro();
        System.out.println("System is closed!");
	}
}
