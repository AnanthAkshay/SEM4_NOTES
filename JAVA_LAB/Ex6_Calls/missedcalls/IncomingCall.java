package missedcalls;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class IncomingCall {
    private String number;
    private String name;
    private LocalDateTime time;

    public IncomingCall(String number, String name) {
        this.number = number;
        this.name = (name == null || name.trim().isEmpty()) ? "private caller" : name;
        this.time = LocalDateTime.now();
    }

    public String getNumber() {
        return number;
    }

    public String getName() {
        return name;
    }

    public String getTimeString() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        return time.format(formatter);
    }

    @Override
    public String toString() {
        return "Caller: " + name + " | Number: " + number + " | Time: " + getTimeString();
    }
}
