public class cmdLine {
    public static void main (String[] args) {
        System.out.println("The no. of args: " + args.length);

        int i;
        for(i= 0; i< args.length; i++) {
            System.out.println(args[i]);
        }

        if(args.length == 2) {
            int a = Integer.parseInt(args[0]);
            int b = Integer.parseInt(args[1]);

            int c = a + b;
            System.out.println("Sum = " + c);
        }
        else
            System.out.println("Enter only two arguments for summation!");


    }
}
