class Bank {
    private String accountNumber;
    private String customerName;
    private String customerAddress;
    private double balance;
    private String email;
    private String phoneNumber;

    // Default constructor
    public Bank() {
        this.accountNumber = "N/A";
        this.customerName = "N/A";
        this.customerAddress = "N/A";
        this.balance = 0.0;
        this.email = "N/A";
        this.phoneNumber = "N/A";
    }

    // Parameterized constructor
    public Bank(String accountNumber, String customerName, String customerAddress, double balance, String email, String phoneNumber) {
        this.accountNumber = accountNumber;
        this.customerName = customerName;
        this.customerAddress = customerAddress;
        this.balance = balance;
        this.email = email;
        this.phoneNumber = phoneNumber;
    }

    // Display customer details
    public void display() {
        System.out.println("--------------------------------------------------");
        System.out.println("Account Number   : " + accountNumber);
        System.out.println("Customer Name    : " + customerName);
        System.out.println("Address          : " + customerAddress);
        System.out.println("Email            : " + email);
        System.out.println("Phone Number     : " + phoneNumber);
        System.out.println("Current Balance  : Rs. " + balance);
        System.out.println("--------------------------------------------------");
    }

    // Deposit amount
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Successfully deposited Rs. " + amount);
        } else {
            System.out.println("Invalid deposit amount.");
        }
    }

    // Withdraw amount with a minimum balance limit check of Rs. 500
    public void withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("Invalid withdrawal amount.");
            return;
        }
        if (balance - amount < 500.0) {
            System.out.println("Transaction Denied! Withdrawal of Rs. " + amount + " violates minimum balance limit of Rs. 500.");
            System.out.println("Available Balance: Rs. " + balance + " | Max allowed withdrawal: Rs. " + (balance - 500.0));
        } else {
            balance -= amount;
            System.out.println("Successfully withdrew Rs. " + amount);
        }
    }

    // Return the balance
    public double getBalance() {
        return balance;
    }
}

public class BankDemo {
    public static void main(String[] args) {
        System.out.println("==================================================");
        System.out.println("            BANK ACCOUNT OPERATIONS (EX-2)         ");
        System.out.println("==================================================");

        // 1. Using default constructor
        System.out.println("Creating account using default constructor:");
        Bank emptyAccount = new Bank();
        emptyAccount.display();

        // 2. Using parameterized constructor
        System.out.println("Creating account with initial deposit of Rs. 2000:");
        Bank myAccount = new Bank("1029384756", "Ananth Akshay", "R.T. Nagar, Bengaluru", 2000.0, "ananth.akshay@gmail.com", "+91 98765 43210");
        myAccount.display();

        // 3. Deposit operation
        System.out.println("Depositing Rs. 1500:");
        myAccount.deposit(1500.0);
        System.out.println("Current Balance via getBalance(): Rs. " + myAccount.getBalance());
        System.out.println();

        // 4. Withdrawal operation (Successful)
        System.out.println("Withdrawing Rs. 2000:");
        myAccount.withdraw(2000.0);
        System.out.println("Current Balance via getBalance(): Rs. " + myAccount.getBalance());
        System.out.println();

        // 5. Withdrawal operation (Failing minimum balance check)
        System.out.println("Attempting to withdraw Rs. 1100 (which leaves Rs. 400, below Rs. 500 minimum):");
        myAccount.withdraw(1100.0);
        System.out.println("Current Balance via getBalance(): Rs. " + myAccount.getBalance());
        System.out.println();

        // 6. Withdrawal operation (Successful boundary check)
        System.out.println("Withdrawing Rs. 1000 (leaves exactly Rs. 500):");
        myAccount.withdraw(1000.0);
        System.out.println("Final Account Details:");
        myAccount.display();
        System.out.println("==================================================");
    }
}
