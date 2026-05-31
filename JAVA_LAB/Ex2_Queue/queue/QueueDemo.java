package queue;

import java.util.Scanner;

public class QueueDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("==================================================");
        System.out.println("     CUSTOM JAVA QUEUE INTERACTION (IS48 EX-2)    ");
        System.out.println("==================================================");
        System.out.print("Enter Queue Capacity: ");
        int capacity = scanner.nextInt();
        
        Queue queue = new Queue(capacity);
        boolean running = true;

        while (running) {
            System.out.println("\n--- Queue Operations Menu ---");
            System.out.println("1. Enqueue (Insert)");
            System.out.println("2. Dequeue (Delete)");
            System.out.println("3. Display Queue");
            System.out.println("4. Exit");
            System.out.print("Select an option (1-4): ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter integer value to enqueue: ");
                    int val = scanner.nextInt();
                    try {
                        queue.enqueue(val);
                    } catch (QueueOverflowException e) {
                        System.err.println("❌ ERROR: " + e.getMessage());
                    }
                    break;
                case 2:
                    try {
                        int popped = queue.dequeue();
                    } catch (QueueUnderflowException e) {
                        System.err.println("❌ ERROR: " + e.getMessage());
                    }
                    break;
                case 3:
                    queue.display();
                    break;
                case 4:
                    running = false;
                    System.out.println("Exiting Queue Demonstration. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid option! Please enter a number between 1 and 4.");
            }
        }
        scanner.close();
    }
}
