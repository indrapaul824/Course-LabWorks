import java.lang.Exception;

class MyException extends Exception {
    public MyException(String message) {
        super(message);
    }
}


public class UncheckedException {
    public static void main (String[] args) {
        try {
            String customerId = null;

            if (customerId == null) {
                throw new MyException("Customer ID cannot be null");
            }
        }

        catch (MyException e) {
            System.err.println(e);
        }
    }
}