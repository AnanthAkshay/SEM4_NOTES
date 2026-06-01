package generics;

public class GenericStackDemo {
    public static void main(String[] args) {
        System.out.println("==================================================");
        System.out.println("     TYPE-SAFE GENERIC JAVA STACK (IS48 EX-8)     ");
        System.out.println("==================================================");

        // 1. Demonstrate Stack of Strings
        System.out.println("\n--- Instantiating Stack of Strings ---");
        Stack<String> stringStack = new Stack<>();

        stringStack.display();
        stringStack.push("Evangeline D");
        stringStack.push("Ananth Akshay");
        stringStack.push("MSRIT Bangalore");
        stringStack.display();

        stringStack.pop();
        stringStack.display();

        System.out.println("Is string stack empty? " + stringStack.isEmpty());
        stringStack.clear();
        stringStack.display();

        // 2. Demonstrate Stack of Integers
        System.out.println("\n--- Instantiating Stack of Integers ---");
        Stack<Integer> intStack = new Stack<>();

        intStack.display();
        intStack.push(100);
        intStack.push(200);
        intStack.push(300);
        intStack.display();

        intStack.pop();
        intStack.pop();
        intStack.display();

        System.out.println("Is integer stack empty? " + intStack.isEmpty());
        intStack.pop(); // Pop last element
        intStack.pop(); // Try to trigger underflow
    }
}
