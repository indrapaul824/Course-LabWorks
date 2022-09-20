
public class ParallelAddition {

    //Sequential Sum
    public void sequentialSum()
    {
        long t1 = System.currentTimeMillis();
        int totsum = 0;
        for(int i=0; i<100000001; i++)
        {
            totsum = totsum + i;
        }
        long t2 = System.currentTimeMillis();
        System.out.println("sequentialSum Total Sum is " + totsum);
        System.out.println("Time taken by sequentialSum " + (t2-t1));
    }

    public static void main(String[] args) {
        ParallelAddition p = new ParallelAddition();
        p.sequentialSum();

        // Parallel Sum using 2 threads
        long t1 = System.currentTimeMillis();
        final int[] totsum1 = {0};
        final int[] totsum2 = {0};
        Runnable r1 = () -> {
            for(int i=0; i<100000001/2; i++)
            {
                totsum1[0] = totsum1[0] + i;
            }
        };

        Runnable r2 = () -> {
            for(int i=100000001/2; i<100000001; i++)
            {
                totsum2[0] = totsum2[0] + i;
            }
        };

        Thread th1 = new Thread(r1);
        Thread th2 = new Thread(r2);

        th1.start();
        th2.start();

        while(true) {
            if (!th1.isAlive() && !th2.isAlive()) {
                int sum = totsum1[0] + totsum2[0];
                long t2 = System.currentTimeMillis();
                System.out.println("parallelSum Total Sum is " + sum);
                System.out.println("Time taken by parallelSum " + (t2 - t1));
                break;
            }
        }
    }
}
