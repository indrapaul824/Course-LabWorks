import java.util.*;

class BankAccount
{
    private final int acno;
    private double bal;
    Scanner in = new Scanner(System.in);
    BankAccount()
    {
        System.out.println("Enter account number: ");
        acno = in.nextInt();
        System.out.println("Enter Initial balance: ");
        bal = in.nextDouble();
    }
    BankAccount(int x, double y)
    {
        acno = x;
        bal = y;
    }

    void deposit()
    {
        float amount;
        System.out.println("Enter Amount to be deposited: ");
        amount = in.nextFloat();
        bal = bal + amount;
        System.out.println("Deposited balance is: " + bal);
    }

    void withdraw()
    {
        float amount;
        System.out.println("Enter the Amount to be withdrawn: ");
        amount = in.nextFloat();
        if(amount<bal)
        {
            bal = bal - amount;
            System.out.println("Amount withdrawn!! Available balance: " + bal);
        }
        else
        {
            System.out.println("Insufficient funds!!");
        }
    }
}


// Driver class
public class Bank
{
    public static void main (String[] args)
    {
        BankAccount myObj = new BankAccount();
        myObj.deposit();
        myObj.withdraw();

        new BankAccount(89000, 15000);
    }
}
