package stringoperations;

public interface StringManipulator {
    String reverse(String input);
    String toUpperCase(String input);
    String toLowerCase(String input);
    String concatenate(String str1, String str2);
    int countVowels(String input);
    int wordCount(String input);
    boolean isPalindrome(String input);
    String replaceChar(String input, char oldChar, char newChar);
}
