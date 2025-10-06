//Concept: Wrapping data and methods into a single unit (class) and restricting direct access using private fields and getters/setters.

class BankAccount {
    private double balance;

    // Getter method
    public double getBalance() {
        return balance;
    }

    // Setter method
    public void deposit(double amount) {
        if (amount > 0)
            balance += amount;
    }

    // A getter is just a method that gets some value (usually from a variable), while a setter is just a method that sets the value of a variable
}

public class EncapsulationExample {
    public static void main(String[] args) {
        BankAccount account = new BankAccount();
        account.deposit(5000);
        System.out.println("Current balance: ₹" + account.getBalance());
    }
}
