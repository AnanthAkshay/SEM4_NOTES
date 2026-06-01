package palindrome;

import java.util.Scanner;

public class PalindromeChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("==================================================");
        System.out.println("     ROBUST JAVA PALINDROME CHECKER (IS48 EX-4)   ");
        System.out.println("==================================================");
        System.out.print("Enter string to verify: ");
        String input = scanner.nextLine();

        try {
            checkPalindrome(input);
        } catch (ShortStringException e) {
            System.err.println("❌ ShortStringException: " + e.getMessage());
        } catch (InvalidInputException e) {
            System.err.println("❌ InvalidInputException: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }

    public static void checkPalindrome(String str) throws ShortStringException, InvalidInputException {
        if (str == null) {
            throw new InvalidInputException("Input string cannot be null.");
        }

        // 1. Validate String Length (must be >= 3 characters)
        if (str.length() < 3) {
            throw new ShortStringException("String length is " + str.length() + ". It must be at least 3 characters long.");
        }

        // 2. Validate Character Content (alphabetical letters only, spaces allowed)
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (!Character.isLetter(ch) && !Character.isWhitespace(ch)) {
                throw new InvalidInputException("Input contains invalid character '" + ch + "'. Alphabetical letters only!");
            }
        }

        // 3. Process Palindrome Case-Insensitively using StringBuffer
        String cleanStr = str.replaceAll("\\s+", "").toLowerCase();
        StringBuffer buffer = new StringBuffer(cleanStr);
        String reversedStr = buffer.reverse().toString();

        System.out.println("\n---------------- PROCESS DETAILS ----------------");
        System.out.println("Sanitized Text: \"" + cleanStr + "\"");
        System.out.println("Reversed Text : \"" + reversedStr + "\"");

        if (cleanStr.equals(reversedStr)) {
            System.out.println("✅ Result: The string \"" + str + "\" IS a Palindrome!");
        } else {
            System.out.println("❌ Result: The string \"" + str + "\" IS NOT a Palindrome.");
        }
        System.out.println("-------------------------------------------------");
    }
}
