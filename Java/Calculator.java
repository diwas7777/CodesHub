import java.util.Scanner;

public class Calc {
public static void main(String[] args){
    System.out.println("Enter your problem");
    Scanner input = new Scanner(System.in);
    int num1 =input.nextInt();
    String opt = input.next();
    int num2 = input.nextInt();
    switch (opt) {
        case "+" -> {
            int sum = num1 + num2;
            System.out.println("Sum of two numbers is :" + sum);
        }
        case "-" -> {
            int dif = num1 - num2;
            System.out.println("Difference is :" + dif);
        }
        case "*" -> {
            int prod = num1 * num2;
            System.out.println("The product is : " + prod);
        }
        case "/" -> {
            int div = num1 / num2;
            System.out.println("The division is :" + div);
        }
        default -> System.out.println("Cannot do anything use + - / or *");
    }


}
}
