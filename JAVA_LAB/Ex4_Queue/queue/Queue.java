package queue;

public class Queue {
    private int[] arr;
    private int front;
    private int rear;
    private int capacity;
    private int count;

    public Queue(int size) {
        arr = new int[size];
        capacity = size;
        front = 0;
        rear = -1;
        count = 0;
    }

    public void enqueue(int item) throws QueueOverflowException {
        if (count == capacity) {
            throw new QueueOverflowException("Queue Overflow! Cannot enqueue " + item + ". Maximum capacity is " + capacity + ".");
        }
        rear = (rear + 1) % capacity;
        arr[rear] = item;
        count++;
        System.out.println("Enqueued: " + item);
    }

    public int dequeue() throws QueueUnderflowException {
        if (count == 0) {
            throw new QueueUnderflowException("Queue Underflow! Cannot dequeue from an empty queue.");
        }
        int item = arr[front];
        front = (front + 1) % capacity;
        count--;
        System.out.println("Dequeued: " + item);
        return item;
    }

    public void display() {
        if (count == 0) {
            System.out.println("Queue is empty.");
            return;
        }
        System.out.print("Queue contents (Front to Rear): ");
        for (int i = 0; i < count; i++) {
            int index = (front + i) % capacity;
            System.out.print(arr[index] + " ");
        }
        System.out.println();
    }
}
