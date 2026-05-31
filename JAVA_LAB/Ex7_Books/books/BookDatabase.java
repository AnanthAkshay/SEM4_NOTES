package books;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class BookDatabase {
    private List<Book> mainList;

    public BookDatabase() {
        mainList = new ArrayList<>();
    }

    public void addBook(Book book) {
        mainList.add(book);
    }

    // Sort books in ascending order of price and store in a new List
    public List<Book> getSortedByPrice() {
        List<Book> sortedList = new ArrayList<>(mainList);
        sortedList.sort(Comparator.comparingDouble(Book::getPrice));
        return sortedList;
    }

    // List all books matching a given author name
    public List<Book> getBooksByAuthor(String authorName) {
        List<Book> matching = new ArrayList<>();
        for (Book b : mainList) {
            if (b.getAuthor().equalsIgnoreCase(authorName)) {
                matching.add(b);
            }
        }
        return matching;
    }

    // Create a new list holding all books with price greater than a specified value
    public List<Book> getBooksPriceGreaterThan(double threshold) {
        List<Book> filtered = new ArrayList<>();
        for (Book b : mainList) {
            if (b.getPrice() > threshold) {
                filtered.add(b);
            }
        }
        return filtered;
    }

    public void displayList(List<Book> list, String title) {
        System.out.println("\n--- " + title + " ---");
        if (list.isEmpty()) {
            System.out.println("No books found.");
            return;
        }
        for (Book b : list) {
            System.out.println(b);
        }
    }

    public static void main(String[] args) {
        BookDatabase db = new BookDatabase();
        
        // Add sample books
        db.addBook(new Book(101, "Java Complete Reference", "Herbert Schildt", "McGrawHill", 850.00));
        db.addBook(new Book(102, "JavaEE 7 for Beginners", "Sharanam Shah", "Shroff", 450.00));
        db.addBook(new Book(103, "Clean Code", "Robert C. Martin", "Pearson", 950.00));
        db.addBook(new Book(104, "Design Patterns", "Erich Gamma", "Addison-Wesley", 1200.00));
        db.addBook(new Book(105, "Java Comprehensive Guide", "Christian Ullenboom", "Shroff", 620.00));
        db.addBook(new Book(106, "Java Concurrency in Practice", "Brian Goetz", "Addison-Wesley", 780.00));

        Scanner scanner = new Scanner(System.in);
        System.out.println("==================================================");
        System.out.println("     COLLECTION BOOK DATABASE SYSTEM (IS48 EX-7)  ");
        System.out.println("==================================================");

        boolean running = true;
        while (running) {
            System.out.println("\n--- Book Database Menu ---");
            System.out.println("1. Display All Books");
            System.out.println("2. Sort and Display Books (Ascending by Price)");
            System.out.println("3. Search Books by Author");
            System.out.println("4. Filter Books by Minimum Price");
            System.out.println("5. Exit");
            System.out.print("Select choice (1-5): ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // consume newline

            switch (choice) {
                case 1:
                    db.displayList(db.mainList, "All Books in Database");
                    break;
                case 2:
                    List<Book> sorted = db.getSortedByPrice();
                    db.displayList(sorted, "Sorted Book Catalog (Ascending Price)");
                    break;
                case 3:
                    System.out.print("Enter Author Name to search: ");
                    String author = scanner.nextLine();
                    List<Book> authorBooks = db.getBooksByAuthor(author);
                    db.displayList(authorBooks, "Books written by: " + author);
                    break;
                case 4:
                    System.out.print("Enter minimum price threshold: ");
                    double threshold = scanner.nextDouble();
                    List<Book> filtered = db.getBooksPriceGreaterThan(threshold);
                    db.displayList(filtered, "Books Priced Above INR " + threshold);
                    break;
                case 5:
                    running = false;
                    System.out.println("Exiting Book Database. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid option! Please enter a choice between 1 and 5.");
            }
        }
        scanner.close();
    }
}
