//Inheritance sub-classing implementation
//Subclass Constructor creation
// Overriding example
class Employee
{
    private String eName;
    private String eID;
    private double salary;

    // Employee class constructor
    Employee(String eName, String eID, double salary) {
        this.eName = eName;
        this.eID = eID;
        this.salary = salary;
    }

    public void seteName(String eName) {
        this.eName = eName;
    }

    public String geteName() {
        return eName;
    }

    public void seteID(String eID) {
        this.eID = eID;
    }

    public String geteID() {
        return eID;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    public double getSalary() {
        return salary;
    }
}

class Manager extends Employee{
    private double bonus;

    Manager(String eName, String eID, double salary, double bonus) {
        super(eName, eID, salary);
        this.bonus = bonus;
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }

    public double getBonus() {
        return bonus;
    }

    @Override
    public double getSalary() {
        return super.getSalary()+bonus;
    }
}

class Project extends Manager {
    private String project;

    Project(String eName, String eID, double salary, double bonus, String project) {
        super(eName, eID, salary, bonus);
        this.project = project;
    }

    public void setProject(String project) {
        this.project = project;
    }

    public String getProject() {
        return project;
    }

    @Override
    public double getSalary() {
        return super.getSalary() + super.getBonus() + 10000;
    }
}

// Driver class
public class CompanyOverriding
{
    public static void main (String[] args)
    {
        Employee e = new Employee("IP", "19MIM", 40000);
        System.out.println(e.getSalary());
        Manager m = new Manager("SS", "10012", 120000, 20000);
        System.out.println(m.getSalary());
        Project p = new Project("AR", "18BCA", 50000, 10000, "Finance Analyzer");
        System.out.println(p.getProject());

        System.out.println(m.getSalary());
        m.seteName("RCh");
        m.setBonus(40000);
        System.out.println("Bonus to boss:"+m.getBonus());

        System.out.println();

        Employee[] staff = new Employee[3];            //Array of Employee objects
        staff[0] = new Employee("DR", "20FTE", 58000);
        staff[1] = new Employee("IP", "19MAI", 80000);
        staff[2] = new Employee("AS", "20BCS", 75000);
        for (Employee employee : staff)
            System.out.println(employee.geteName() + "\t" + employee.getSalary() + "\t" + employee.geteID());

        System.out.println();

        Project[] staff1 = new Project[3];            //Array of Project objects
        staff1[0] = new Project("DR", "20FTE", 58000, 7500, "AR Ad");
        staff1[1] = new Project("IP", "19MAI", 80000, 10000, "Finance Analyzer");
        staff1[2] = new Project("AS", "20BCS", 75000, 15000, "AR Ad System");
        for (Project project : staff1)
            System.out.println(project.geteName() + "\t" + project.getProject() + "\t" + project.getBonus() + "\t" + project.getSalary());
    }
}
