// Indrashis Paul
// Reg no.: 19MIM10046

public class cmdOps {
    public static void main(String[] args) {
        System.out.println("The no. of args: " + args.length);

        int i;
        for (i = 0; i < args.length; i++) {
            System.out.println(args[i]);
        }

        if (args.length == 3) {
            int a = Integer.parseInt(args[0]);
            int b = Integer.parseInt(args[1]);

            String c = args[2];

            if(c.equals("+")) {
                System.out.println(a+b);
            }
            else if(c.equals("-")) {
                if(a>b)
                    System.out.println(a-b);
                else
                    System.out.println(b-a);
            }
            else if(c.equals("X")) {
                System.out.println(a*b);
            }
            else if(c.equals("/")) {
                if(a==0 || b==0) {
                    System.out.println("Please input values other than 0");
                }
                else
                    System.out.println(a/b);

            }

        } else
            System.out.println("Enter only two arguments for operation!");
    }
}