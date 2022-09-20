import java.time.*;
import java.time.format.DateTimeFormatter;

public class TimeDuration {
    public static void main (String[] args) {
        Period p1 = Period.ofWeeks (3);
        System.out.println (p1);

        // adding duration to local time
        Duration d1 = Duration.ofDays (7);
        LocalDateTime localDateTime = LocalDateTime.now ();
        LocalDateTime finalDateTime = localDateTime.plus (d1); // adding

        System.out.println (finalDateTime);

        // To print the date and time in a particular format
        DateTimeFormatter df = DateTimeFormatter.ofPattern ("HH");
        String pattern = finalDateTime.format (df);
        System.out.println ("Formatted date: " + pattern);
    }
}
