package Company;

import PayrollManagement.*;

public class PayrollSystem {
    public static void main(String[] args) {
        System.out.println("==================================================");
        System.out.println("     MSRIT COMPANY PAYROLL SYSTEM (IS48 EX-1)      ");
        System.out.println("==================================================");

        // Create an array of Employee objects containing mixed roles
        Employee[] employees = new Employee[3];
        
        employees[0] = new FullTime("Evangeline D", 35, 95000.0, "Senior Developer");
        employees[1] = new PartTime("Ananth Akshay", 21, "Technical Writer", 450.0, 40); // 450/hr for 40 hours
        employees[2] = new Intern("Jane Doe", 22, "Java Intern", 25000.0); // 25000 fixed stipend

        // Process and display payroll for each employee
        for (Employee emp : employees) {
            emp.displayDetails();
            
            double finalSalary = 0;
            if (emp instanceof Payable) {
                finalSalary = ((Payable) emp).calculate();
            }
            
            System.out.println("Calculated Payable Salary: INR " + finalSalary);
            System.out.println("--------------------------------------------------");
        }
    }
}
