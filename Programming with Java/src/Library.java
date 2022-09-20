import java.sql.Ref;

class Book {
    protected void issues() {
        System.out.println("Print Book");
    }
}

class RefBook extends Book {
    protected void issues() {
        System.out.println("Print Reference Book");
    }
}



public class Library
{
    public static void main (String[] args) {
        Book b = new Book();
        b.issues();
        RefBook rb = new RefBook();
        rb.issues();
    }
}
