package PayrollManagement;

public class FullTime extends Employee implements Payable {
    public FullTime(String name, int age, double salary, String designation) {
        super(name, age, salary, designation);
    }

    @Override
    public double calculate() {
        return this.salary; // Receives basic monthly salary directly
    }
}
