package password;

import java.util.Scanner;

public class PasswordSecurityApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("==================================================");
        System.out.println("     PASSWORD SECURITY SUITE ENGINE (IS48 EX-5)   ");
        System.out.println("==================================================");
        System.out.print("Enter your password: ");
        String password = scanner.nextLine();

        System.out.println("\n---------------- SECURITY REPORT ----------------");

        // 1. Check for Uppercase, Lowercase, and Digits
        boolean hasUpper = false;
        boolean hasLower = false;
        boolean hasDigit = false;
        for (char c : password.toCharArray()) {
            if (Character.isUpperCase(c)) hasUpper = true;
            else if (Character.isLowerCase(c)) hasLower = true;
            else if (Character.isDigit(c)) hasDigit = true;
        }
        System.out.println("• Complexity Validation:");
        System.out.println("  - Contains Uppercase? : " + (hasUpper ? "YES (Pass)" : "NO (Fail)"));
        System.out.println("  - Contains Lowercase? : " + (hasLower ? "YES (Pass)" : "NO (Fail)"));
        System.out.println("  - Contains Digit?      : " + (hasDigit ? "YES (Pass)" : "NO (Fail)"));
        System.out.println("  - Overall Strength   : " + (hasUpper && hasLower && hasDigit ? "STRONG" : "WEAK"));

        // 2. Count Special Characters (excluding alphanumeric)
        int specialCount = 0;
        for (char c : password.toCharArray()) {
            if (!Character.isLetterOrDigit(c) && !Character.isWhitespace(c)) {
                specialCount++;
            }
        }
        System.out.println("• Count of Special Characters: " + specialCount);

        // 3. Mask the Password (replace with *, keeping first and last characters)
        String masked = maskPassword(password);
        System.out.println("• Masked Security Preview   : " + masked);

        // 4. Reverse the Password (Encryption Demonstration)
        String reversed = new StringBuilder(password).reverse().toString();
        System.out.println("• Reversed Password Trace   : " + reversed);

        // 5. Append random security token (e.g. "@123!")
        String tokened = password + "@123!";
        System.out.println("• Appended Security Token   : " + tokened);

        // 6. Replace Vowels with '#'
        String scrambled = password.replaceAll("(?i)[aeiou]", "#");
        System.out.println("• Scrambled Vowel Variant    : " + scrambled);
        System.out.println("-------------------------------------------------");

        scanner.close();
    }

    private static String maskPassword(String pass) {
        if (pass == null || pass.length() <= 2) {
            return pass; // Cannot mask middle of 0, 1, or 2 length string
        }
        StringBuilder builder = new StringBuilder();
        builder.append(pass.charAt(0));
        for (int i = 1; i < pass.length() - 1; i++) {
            builder.append('*');
        }
        builder.append(pass.charAt(pass.length() - 1));
        return builder.toString();
    }
}
