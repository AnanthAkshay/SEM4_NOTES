package stringoperations;

public class StringProcessor implements StringManipulator {

    @Override
    public String reverse(String input) {
        if (input == null) return null;
        return new StringBuilder(input).reverse().toString();
    }

    @Override
    public String toUpperCase(String input) {
        if (input == null) return null;
        return input.toUpperCase();
    }

    @Override
    public String toLowerCase(String input) {
        if (input == null) return null;
        return input.toLowerCase();
    }

    @Override
    public String concatenate(String str1, String str2) {
        if (str1 == null) str1 = "";
        if (str2 == null) str2 = "";
        return str1.concat(str2);
    }

    @Override
    public int countVowels(String input) {
        if (input == null) return 0;
        int count = 0;
        String temp = input.toLowerCase();
        for (int i = 0; i < temp.length(); i++) {
            char c = temp.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            }
        }
        return count;
    }

    @Override
    public int wordCount(String input) {
        if (input == null || input.trim().isEmpty()) return 0;
        String[] words = input.trim().split("\\s+");
        return words.length;
    }

    @Override
    public boolean isPalindrome(String input) {
        if (input == null) return false;
        String clean = input.replaceAll("\\s+", "").toLowerCase();
        String reversed = reverse(clean);
        return clean.equals(reversed);
    }

    @Override
    public String replaceChar(String input, char oldChar, char newChar) {
        if (input == null) return null;
        return input.replace(oldChar, newChar);
    }
}
