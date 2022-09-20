import java.util.*;
import java.util.stream.Collectors;

class Employee1
{
    private final String id;
    private final double sal;

    Employee1(String id, double sal)
    {
        this.id = id;
        this.sal = sal;
    }

    public double getSal() {
        return sal;
    }

    @Override
    public String toString() {
        return "Employee1{" +
                "id='" + id + '\'' +
                ", sal=" + sal +
                '}';
    }
}



public class CompanyEmployee
{
    public static void main (String[] args)
    {
        Employee1[] a1 = new Employee1[4];
        a1[0] = new Employee1("M10046", 20000);
        a1[1] = new Employee1("A10090", 38000);
        a1[2] = new Employee1("B30066", 56000);
        a1[3] = new Employee1("D11004", 90000);

        List<Employee1> empList = Arrays.asList(a1);
        empList.forEach(System.out::println);

        empList
                .forEach(employee1 ->
                {
                    if (employee1.getSal() > 50000)
                    {
                        System.out.println("Senior Employees");
                    }
                    else
                    {
                        System.out.println("Junior Employees");
                    }
                });

        empList.stream().filter(x -> x.getSal()<50000).forEach(System.out::println);
        
        List<Employee1> newEmpList = empList.stream().filter(x -> x.getSal() < 50000)
                .collect(Collectors.toList());
        
        System.out.println(newEmpList);
    }
}
