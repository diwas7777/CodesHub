import java.util.Scanner;

public class WordCount {

    public static void main(String[] args) {
        System.out.print("Please enter a word:\n>>>");
        Scanner scanner = new Scanner(System.in);
        String word = scanner.nextLine();
        System.out.println(String.format("The word has %s characters.", word.length()));
    }
}