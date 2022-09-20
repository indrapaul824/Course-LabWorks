class TimeSpan {
    private int hours;
    private int minutes;

    TimeSpan(int hours, int minutes) {
        this.hours = hours;
        if (minutes > -1 && minutes < 60)
            this.minutes = minutes;
    }

    public int getHours () {
        return hours;
    }

    public int getMinutes () {
        return minutes;
    }

    public void add (int addHours, int addMinutes) {
        hours += addHours;
        minutes += addMinutes;

        if (minutes >= 60) {
            minutes -= 60;
            hours++;
        }
    }

    public void add (TimeSpan span) {
        add (span.hours, span.minutes);
    }

    public double getTotalHours () {
        return hours + minutes / 60.0;
    }

    @Override
    public String toString () {
        return "TimeSpan{" +
                hours + "h" +
                minutes + "m" +
                '}';
    }
}


public class submit4 {
    public static void main (String[] args) {
        TimeSpan t1 = new TimeSpan(13, 37);
        System.out.println(t1 + " is " + t1.getTotalHours() + " hours");

        t1.add(11, 30);
        System.out.println(t1 + " is " + t1.getTotalHours() + " hours");

        TimeSpan t2 = new TimeSpan(2, 49);
        t1.add(t2);
        System.out.println(t1 + " is " + t1.getTotalHours() + " hours");
    }
}
