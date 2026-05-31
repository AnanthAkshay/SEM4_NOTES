package PayrollManagement;

public class PartTime extends Employee implements Payable {
    private double hourlyRate;
    private int hoursWorked;

    public PartTime(String name, int age, String designation, double hourlyRate, int hoursWorked) {
        super(name, age, 0, designation); // base salary set to 0, dynamically calculated
        this.hourlyRate = hourlyRate;
        this.hoursWorked = hoursWorked;
    }

    @Override
    public double calculate() {
        return hourlyRate * hoursWorked;
    }
}
