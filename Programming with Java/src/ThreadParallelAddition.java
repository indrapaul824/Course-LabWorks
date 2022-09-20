import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.Executors;
/*
public class ThreadParallelAddition {


    public Integer parallelSum()
    {
        long t1 = System.currentTimeMillis();
        ExecutorService executor = Executors.newFixedThreadPool(10);
        List<Future<Integer>> list = new ArrayList<>();
        int count=1;
        int prev=0;
        for(int i=0 ;i<101;i++)
        {
            if(count%2 == 0)//grouping
            {
                System.out.println("Prev :" + prev + " current: " + i);
                Future<Integer> future = executor.submit(new CallableAdder(prev,i));
                list.add(future);
                count=1;
                continue;
            }
            prev=i ;
            count++;
        }
        int totsum=0;
        for(Future<Integer> fut : list)
        {
            try {
                totsum = totsum+ fut.get();
            } catch (InterruptedException | ExecutionException e) {
                e.printStackTrace();
            }
        }
        System.out.println("Total Sum is " + totsum);
        long t2 = System.currentTimeMillis();
        System.out.println("Time taken by parallelSum " + (t2-t1));
        return totsum;
    }
    public int sequentialSum()
    {
        long t1 = System.currentTimeMillis();
        Integer totsum=0;
        for(int i=0; i<101; i++)
        {
            totsum = totsum + i;
        }
        long t2 = System.currentTimeMillis();
        System.out.println("sequentialSum Total Sum is " + totsum);
        System.out.println("Time taken by sequentialSum " + (t2-t1));
        return totsum;
    }


    public static void main(String[] args) {
        ThreadParallelAddition adder = new ThreadParallelAddition();
        int pSum= adder.parallelSum(); //using threads
        int sSum= adder.sequentialSum(); //for loop
        System.out.println("parallel Sum equals to Sequential Sum ? " );
        System.out.println("Answer is :: " + (pSum==sSum));
    }

}*/
