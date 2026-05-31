package application;

import stringoperations.*;
import java.util.Scanner;

public class StringApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StringProcessor processor = new StringProcessor();

        System.out.println("==================================================");
        System.out.println("     MODULAR STRING PROCESSOR SUITE (IS48 EX-3)   ");
        System.out.println("==================================================");

        System.out.print("Enter a main string to process: ");
        String userInput = scanner.nextLine();

        System.out.print("Enter an additional string for concatenation: ");
        String concatInput = scanner.nextLine();

        System.out.print("Enter a character to replace in the main string: ");
        char oldChar = scanner.next().charAt(0);

        System.out.print("Enter the replacement character: ");
        char newChar = scanner.next().charAt(0);

        System.out.println("\n----------------- TEST RESULTS -----------------");
        System.out.println("1. Original String  : \"" + userInput + "\"");
        System.out.println("2. Reversed String  : \"" + processor.reverse(userInput) + "\"");
        System.out.println("3. Uppercase conversion: \"" + processor.toUpperCase(userInput) + "\"");
        System.out.println("4. Lowercase conversion: \"" + processor.toLowerCase(userInput) + "\"");
        System.out.println("5. Concatenated result : \"" + processor.concatenate(userInput, concatInput) + "\"");
        System.out.println("6. Vowel Count      : " + processor.countVowels(userInput));
        System.out.println("7. Word Count       : " + processor.wordCount(userInput));
        System.out.println("8. Is Palindrome?   : " + processor.isPalindrome(userInput));
        System.out.println("9. Char Replacement : \"" + processor.replaceChar(userInput, oldChar, newChar) + "\"");
        System.out.println("--------------------------------------------------");

        scanner.close();
    }
}
