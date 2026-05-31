package PayrollManagement;

public class Intern extends Employee implements Payable {
    private double stipend;

    public Intern(String name, int age, String designation, double stipend) {
        super(name, age, 0, designation); // base salary set to 0, dynamically calculated
        this.stipend = stipend;
    }

    @Override
    public double calculate() {
        return stipend; // Receives a fixed stipend
    }
}
