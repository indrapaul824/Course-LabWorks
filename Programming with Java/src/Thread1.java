import java.util.concurrent.TimeUnit;

public class Thread1 {
    public static void main(String[] args) {
        // Runnable Functional Interface
        Runnable task = () -> {String threadName = Thread.currentThread().getName();
                System.out.println("Hello " + threadName);
        };
        task.run();  // called from Runnable Functional Interface

        Thread thread0 = new Thread(task);
        Thread thread1 = new Thread(task);
        Thread thread2 = new Thread(task);

        //Thread.sleep(3000);
        thread0.start();
        thread1.start();
        thread2.start();

        System.out.println("Done!");


        Runnable task1 = () -> {
            try {
                String name = Thread.currentThread().getName();
                System.out.println("Foo " + name);
                TimeUnit.SECONDS.sleep(3);
                System.out.println("Bar " + name);
            }
            catch (InterruptedException e) {
                e.printStackTrace();
            }
        };

        Thread thread3 = new Thread(task1);
        Thread thread4 = new Thread(task1);
        Thread thread5 = new Thread(task1);

        //Thread.sleep(3000);
        thread3.start();
        thread4.start();
        thread5.start();

        System.out.println("Done 2!");
    }
}
