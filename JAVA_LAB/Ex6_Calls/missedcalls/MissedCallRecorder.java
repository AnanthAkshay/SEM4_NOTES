package missedcalls;

import java.util.LinkedList;
import java.util.Scanner;

public class MissedCallRecorder {
    private LinkedList<IncomingCall> callList;
    private static final int MAX_CALLS = 3;

    public MissedCallRecorder() {
        callList = new LinkedList<>();
    }

    public void addCall(String number, String name) {
        IncomingCall call = new IncomingCall(number, name);
        if (callList.size() >= MAX_CALLS) {
            // Expel the oldest call (which is at the head of the list)
            IncomingCall oldest = callList.removeFirst();
            System.out.println("⚠️ Storage full! Removing oldest record: [" + oldest.getName() + "]");
        }
        callList.addLast(call);
        System.out.println("📞 Missed call logged from: " + call.getName());
    }

    public void displayCalls() {
        if (callList.isEmpty()) {
            System.out.println("No missed calls logged.");
            return;
        }
        System.out.println("\n--- Missed Calls (Oldest to Newest) ---");
        for (int i = 0; i < callList.size(); i++) {
            System.out.println((i + 1) + ". " + callList.get(i).getName());
        }
    }

    public void interactiveMenu() {
        Scanner scanner = new Scanner(System.in);
        boolean active = true;

        while (active) {
            displayCalls();
            if (callList.isEmpty()) {
                break;
            }
            System.out.println("\nOptions: ");
            System.out.println("1. View call details");
            System.out.println("2. Delete a call");
            System.out.println("3. Exit Missed Calls Hub");
            System.out.print("Select choice (1-3): ");
            int choice = scanner.nextInt();

            if (choice == 3) {
                active = false;
                System.out.println("Exiting Phone Simulator.");
                break;
            }

            System.out.print("Enter item number (1-" + callList.size() + "): ");
            int index = scanner.nextInt() - 1;

            if (index < 0 || index >= callList.size()) {
                System.out.println("Invalid selection!");
                continue;
            }

            if (choice == 1) {
                IncomingCall call = callList.get(index);
                System.out.println("\n--- CALL DETAILS ---");
                System.out.println("Origin Number: " + call.getNumber());
                System.out.println("Caller Name  : " + call.getName());
                System.out.println("Timestamp    : " + call.getTimeString());
                System.out.println("--------------------");
            } else if (choice == 2) {
                IncomingCall deleted = callList.remove(index);
                System.out.println("🗑️ Call record from [" + deleted.getName() + "] deleted successfully.");
            }
        }
    }

    public static void main(String[] args) {
        MissedCallRecorder recorder = new MissedCallRecorder();

        System.out.println("==================================================");
        System.out.println("     TELEPHONE CALL RECORDER ENGINE (IS48 EX-6)   ");
        System.out.println("==================================================");

        // Simulate 4 calls to verify older record expulsion
        System.out.println("Simulating incoming calls...");
        recorder.addCall("9876543210", "Evangeline D");
        recorder.addCall("9988776655", "Ananth Akshay");
        recorder.addCall("8877665544", null); // Unlisted number
        recorder.addCall("7766554433", "John Watson"); // 4th call should trigger oldest expulsion

        // Open the user menu
        recorder.interactiveMenu();
    }
}
