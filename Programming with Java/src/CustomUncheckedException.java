import java.util.Scanner;

class MultipleOptionFoundException extends UnsupportedOperationException
{
    public MultipleOptionFoundException(String message)
    {
        super(message);
    }
}

class OptionChoiceService
{
    public void validateNumOptions(int opNum) {
        try {
            if (opNum > 1) {
                throw new MultipleOptionFoundException ("Multiple Options are not supported! Please choose a single option.");
            }
            else {
                System.out.println("Options validated!");
            }
        } catch (MultipleOptionFoundException e) {
            e.printStackTrace ();
        }
    }
}


public class CustomUncheckedException
{
    public static void main (String[] args) {
        Scanner in = new Scanner(System.in);
        OptionChoiceService service = new OptionChoiceService();
        System.out.println("Available Options: \n1\n2\n3\n4\nEnter your choice:");
        String s = in.nextLine ();
        String[] S = s.split(",");
        service.validateNumOptions (S.length);
    }
}
