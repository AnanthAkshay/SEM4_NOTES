package queue;

public class QueueUnderflowException extends Exception {
    public QueueUnderflowException(String message) {
        super(message);
    }
}
