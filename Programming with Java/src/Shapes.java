public class Shapes
{
    static void print_rectangle(int n, int m)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= m; j++)
            {
                if (i == 1 || i == n ||
                        j == 1 || j == m)
                    System.out.print("*");
                else
                    System.out.print(" ");
            }
            System.out.println();
        }

    }

    static void print_shapes()
    {
        System.out.println ("      ***        *          * ");
        System.out.println ("    *     *     ***        * * ");
        System.out.println ("   *       *   *****      *   * ");
        System.out.println ("   *       *     *       *     * ");
        System.out.println ("   *       *     *      *       * ");
        System.out.println ("   *       *     *       *     * ");
        System.out.println ("   *       *     *        *   * ");
        System.out.println ("    *     *      *         * * ");
        System.out.println ("      ***        *          * ");
    }


    public static void main(String[] args)
    {
        int rows = 6, columns = 20;
        System.out.println ("This Application Displays A Box, An Oval, An Arrow"
                + " And A Diamond Using Asterisks (*)");
        print_rectangle(rows, columns);
        print_shapes();
    }
}