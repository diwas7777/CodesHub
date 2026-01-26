// Simple Shopping List CLI App in Java

import java.util.ArrayList;
import java.util.Scanner;

public class ShoppingList {

    static ArrayList<String> itemNames = new ArrayList<>();       // stores item names
    static ArrayList<String> itemQuantities = new ArrayList<>();  // stores corresponding quantities

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int menu;

        while (true) {
            // Display menu
            System.out.println("\n--Shopping List--");
            System.out.println("1. Add Item");
            System.out.println("2. Delete Item");
            System.out.println("3. Show List");
            System.out.println("0. Close");
            System.out.print("Choice: ");

            // Read menu choice safely
            try {
                menu = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("\nInvalid option.");
                continue;
            }

            switch (menu) {
                case 1 -> { // Add item
                    System.out.print("Item name: ");
                    String name = scanner.nextLine();
                    if (!name.isEmpty()) {
                        System.out.print("Item quantity: ");
                        String quantity = scanner.nextLine();
                        if (!quantity.isEmpty()) {
                            itemNames.add(name);
                            itemQuantities.add(quantity);
                        }
                    }
                }

                case 2 -> { // Delete item
                    while (true) { 
                        if (!itemNames.isEmpty()) {
                            System.out.println("\nChoose item to remove:");
                            for (int i = 0; i < itemNames.size(); i++) {
                                System.out.println((i + 1) + ". " + itemNames.get(i));
                            }
                            System.out.println("0.(Back)");
                            System.out.print("Choice: ");
                            try {
                                int choice = Integer.parseInt(scanner.nextLine());
                                if (choice > 0 && choice <= itemNames.size()) {
                                    itemNames.remove(choice - 1);
                                    itemQuantities.remove(choice - 1);
                                } else if(choice == 0) {
                                    break;
                                } else {
                                    System.out.println("\nInvalid Input!");
                                }
                            } catch (NumberFormatException e) {
                                System.out.println("\nInvalid Input!");
                            }
                        } else {
                            System.out.println("\nYou don't have any items in the list...");
                            scanner.nextLine();
                            break;
                        }
                    }
                }

                case 3 -> { // Show list
                    if (!itemNames.isEmpty()) {
                        System.out.println("\nYour shopping list:");
                        for (int i = 0; i < itemNames.size(); i++) {
                            System.out.println((i + 1) + ". " + itemNames.get(i) + " - " + itemQuantities.get(i));
                        }
                        System.out.println("\n(Back)");
                        scanner.nextLine();
                    } else {
                        System.out.println("\nYou don't have any items in the list...");
                        scanner.nextLine();
                    }
                }

                case 0 -> { // Exit program
                    System.out.println("Exiting...");
                    scanner.close();
                    return;
                }

                default -> System.out.println("Invalid option."); // Invalid menu choice
            }
        }
    }
}
