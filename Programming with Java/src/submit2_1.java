class Student
{
    private String name;
    private final int id;
    private final double gpa;


    Student(String name, int id, double gpa)
    {
        this.name = name;
        this.id = id;
        this.gpa = gpa;
    }

    public String getName() {
        return name;
    }

    public double getGpa() {
        return gpa;
    }

    public int getId() {
        return id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", id=" + id +
                ", gpa=" + gpa +
                '}';
    }
}

class Undergrad extends Student
{
    private int year;

    Undergrad(String name, int id, double gpa, int year)
    {
        super(name, id, gpa);
        this.year = year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public int getYear() {
        return year;
    }

    @Override
    public String toString() {
        return "Undergrad{" +
                "name='" + super.getName() + '\'' +
                ", id=" + super.getId() +
                ", gpa=" + super.getGpa() +
                ", year=" + year +
                '}';
    }
}

class Graduate extends Student
{
    private String thesisTitle;


    Graduate(String name, int id, double gpa, String thesisTitle)
    {
        super(name, id, gpa);
        this.thesisTitle = thesisTitle;
    }

    public void setThesisTitle(String thesisTitle)
    {
        this.thesisTitle = thesisTitle;
    }

    public String getThesisTitle()
    {
        return thesisTitle;
    }

    @Override
    public String toString() {
        return "Graduate{" +
                "name='" + super.getName() + '\'' +
                ", id=" + super.getId() +
                ", gpa=" + super.getGpa() +
                ", thesisTitle='" + thesisTitle + '\'' +
                '}';
    }
}



public class submit2_1
{
    public static void main (String[] args)
    {
        Student s1 = new Student("Student 1",10046, 8.56);
        System.out.println(s1);

        s1 = new Undergrad("Student 1",10046, 8.56, 2018);
        System.out.println(s1);

        s1 = new Graduate("Student 1",10046, 8.56, "NovelMLAlgo");
        System.out.println(s1);

        System.out.println();

        Student s2 = new Student("Student 2", 10200, 7.8);
        System.out.println(s2);
        s2.setName("Student IP");
        System.out.println(s2);

        System.out.println();

        Undergrad ug1 = new Undergrad("Student 3", 10046, 9.0, 2019);
        System.out.println(ug1);
        System.out.println(ug1.getName() + " " + ug1.getId() + " " + ug1.getGpa());
        ug1.setYear(2020);
        ug1.setName("Undergrad 1");
        System.out.println(ug1);
        System.out.println(ug1.getName() + " " + ug1.getId() + " " + ug1.getGpa());

        System.out.println();

        Graduate gr1 = new Graduate("Student 4", 10000, 10.0, "NLP Novel Algo");
        System.out.println(gr1);
        System.out.println(gr1.getName() + " " + gr1.getId() + " " + gr1.getGpa());
        gr1.setThesisTitle("Novel NLP Algo");
        gr1.setName("Graduate 1");
        System.out.println(gr1);
        System.out.println(gr1.getName() + " " + gr1.getId() + " " + gr1.getGpa());
    }
}
