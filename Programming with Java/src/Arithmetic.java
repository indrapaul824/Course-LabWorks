package Miscellaneous;

import java.util.*;

public class Arithmetic
{
  public static void main(String[] args)
  {
    Scanner in = new Scanner(System.in);
    int a, b;
    System.out.println("Input the numbers:");
    a = in.nextInt();
    b = in.nextInt();
    System.out.println("The sum is:" + (a+b));
    System.out.println("The difference is:" + (a-b));
    System.out.println("The product is:" + (a*b));
    System.out.println("The quotient is:" + (a/b));
    System.out.println("The remainder is:" + (a%b));
  }
  
}
