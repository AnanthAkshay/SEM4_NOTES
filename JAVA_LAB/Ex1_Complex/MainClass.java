class Complex {
    private double real;
    private double imaginary;

    // Default constructor
    public Complex() {
        this.real = 0.0;
        this.imaginary = 0.0;
    }

    // Parameterized constructor
    public Complex(double real, double imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    // Display complex number in proper format (e.g. 3.0 + 4.0i)
    public void display() {
        if (imaginary >= 0) {
            System.out.println(real + " + " + imaginary + "i");
        } else {
            System.out.println(real + " - " + Math.abs(imaginary) + "i");
        }
    }

    // Multiply two Complex Numbers and return resultant Complex Number
    public Complex multiply(Complex c) {
        double r = (this.real * c.real) - (this.imaginary * c.imaginary);
        double i = (this.real * c.imaginary) + (this.imaginary * c.real);
        return new Complex(r, i);
    }
}

public class MainClass {
    public static void main(String[] args) {
        System.out.println("==================================================");
        System.out.println("      COMPLEX NUMBER MULTIPLICATION (EX-1)        ");
        System.out.println("==================================================");

        // Using default constructor
        Complex c1 = new Complex();
        System.out.print("Complex Number 1 (Default): ");
        c1.display();

        // Using parameterized constructor
        Complex c2 = new Complex(3.0, 4.0);
        System.out.print("Complex Number 2 (Parameterized): ");
        c2.display();

        Complex c3 = new Complex(1.5, -2.5);
        System.out.print("Complex Number 3 (Parameterized): ");
        c3.display();

        // Multiplying c2 and c3
        Complex result = c2.multiply(c3);
        System.out.print("Result of Multiplication: ");
        result.display();
        System.out.println("==================================================");
    }
}
