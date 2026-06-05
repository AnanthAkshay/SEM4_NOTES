package generics;

import java.util.ArrayList;

public class Stack<T> {
    private ArrayList<T> elements;

    public Stack() {
        elements = new ArrayList<>();
    }

    public void push(T item) {
        elements.add(item);
        System.out.println("Pushed: " + item);
    }

    public T pop() {
        if (isEmpty()) {
            System.err.println("❌ Stack Underflow! Cannot pop from empty stack.");
            return null;
        }
        T item = elements.remove(elements.size() - 1);
        System.out.println("Popped: " + item);
        return item;
    }

    public void clear() {
        elements.clear();
        System.out.println("Stack cleared.");
    }

    public boolean isEmpty() {
        return elements.isEmpty();
    }

    public void display() {
        if (isEmpty()) {
            System.out.println("Stack is empty.");
            return;
        }
        System.out.print("Stack elements (Bottom to Top): ");
        for (T item : elements) {
            System.out.print(item + " -> ");
        }
        System.out.println("[TOP]");
    }
}
