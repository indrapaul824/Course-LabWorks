public class Welcome {
    public static void main (String[] args) {
        if(args.length == 2) {
            if(args[0].equals("Indrashis") && args[1].equals("Paul")) {
                System.out.println("Welcome, " + args[0] + " " + args[1] + "!");
            }
            else
                System.out.println("Please enter correct name!");
        }
        else
            System.out.println("Please enter the full name!");
    }
}
