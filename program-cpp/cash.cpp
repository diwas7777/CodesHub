#include <iostream>
#include <vector>
#include <iomanip>
#include <string>
#include <limits>
#include <algorithm>
#include <cctype>


#ifdef _WIN32
#include <windows.h>
#endif

using namespace std;


#define RESET   "\033[0m"
#define RED     "\033[31m"
#define GREEN   "\033[32m"
#define YELLOW  "\033[33m"
#define BLUE    "\033[34m"
#define MAGENTA "\033[35m"
#define CYAN    "\033[36m"
#define BOLD    "\033[1m"


string toLower(string str) {
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    return str;
}

class Item {
public:
    string name;
    double price;
    int quantity;
    double total;

    Item(string n, double p, int q) {
        name = n;
        price = p;
        quantity = q;
        total = price * quantity;
    }
};

class FruitShop {
private:
    vector<Item> items;
    double grandTotal;
    double cashGiven;
    double change;

    struct FruitOption {
        string name;
        double price;
        string color;
    };

    vector<FruitOption> availableFruits = {
        {"Apple", 80, RED},
        {"Mango", 60, YELLOW},
        {"Banana", 40, YELLOW},
        {"Orange", 50, "\033[38;5;208m"},
        {"Grapes", 70, "\033[38;5;93m"},
        {"Strawberry", 90, RED},
        {"Watermelon", 30, GREEN},
        {"Pineapple", 65, YELLOW},
        {"Pomegranate", 85, RED},
        {"Kiwi", 75, GREEN}
    };

public:
    FruitShop() {
        grandTotal = 0;
        cashGiven = 0;
        change = 0;
    }

    void showAvailableFruits() {
        cout << "\n" << GREEN << BOLD << "==========================================" << RESET << endl;
        cout << GREEN << BOLD << "       🍎 AVAILABLE FRUITS & PRICES 🍍       " << RESET << endl;
        cout << GREEN << BOLD << "==========================================" << RESET << endl;
        cout << left << setw(20) << "Fruit" << setw(15) << "Price (per kg)" << endl;
        cout << "------------------------------------------" << endl;
        
        for (const auto& fruit : availableFruits) {
            cout << fruit.color << left << setw(20) << fruit.name << RESET;
            cout << "Rs. " << fixed << setprecision(2) << fruit.price << " /kg" << endl;
        }
        cout << GREEN << "==========================================" << RESET << endl;
    }

    void addItem() {
        string itemName;
        double price;
        int quantity;

        cout << CYAN << "\n📝 Enter item details:" << RESET << endl;
        

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        
        bool validFruit = false;
        do {
            cout << "Fruit name: ";
            getline(cin, itemName);
            
            // Convert input to lowercase for case-insensitive comparison
            string itemNameLower = toLower(itemName);
            
            for (const auto& fruit : availableFruits) {
                string fruitNameLower = toLower(fruit.name);
                
                if (fruitNameLower == itemNameLower) {
                    price = fruit.price;
                    validFruit = true;
                    cout << fruit.color << "✅ " << fruit.name << " found! Price: Rs. " << price << "/kg" << RESET << endl;
                    itemName = fruit.name;
                    break;
                }
            }
            
            if (!validFruit) {
                cout << RED << "❌ Fruit not available! Please choose from the list." << RESET << endl;
                showAvailableFruits();
            }
        } while (!validFruit);


        cout << "Quantity (in kg): ";
        cin >> quantity;
        
        while (cin.fail() || quantity <= 0) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << RED << "❌ Invalid quantity! Please enter a positive number: " << RESET;
            cin >> quantity;
        }

        Item newItem(itemName, price, quantity);
        items.push_back(newItem);
        
        cout << GREEN << "✅ Added: " << quantity << "kg of " << itemName << " (Rs. " << price << "/kg)" << RESET << endl;
    }

    void calculateGrandTotal() {
        grandTotal = 0;
        for (const auto& item : items) {
            grandTotal += item.total;
        }
    }

    bool processPayment() {
        calculateGrandTotal();
        
        cout << "\n" << YELLOW << BOLD << "💰 PAYMENT SECTION 💰" << RESET << endl;
        cout << "Grand Total: Rs. " << fixed << setprecision(2) << grandTotal << endl;
        
        do {
            cout << "\n💵 Enter cash given (Rs.): ";
            cin >> cashGiven;
            
            if (cin.fail()) {
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                cout << RED << "❌ Invalid input! Please enter a number." << RESET << endl;
                continue;
            }
            
            if (cashGiven < grandTotal) {
                cout << RED << "❌ Insufficient cash! Need Rs. " << grandTotal << RESET << endl;
            } else {
                break;
            }
        } while (true);
        
        change = cashGiven - grandTotal;
        return true;
    }

    void printReceipt() {
        cout << "\n" << GREEN << BOLD;
        cout << "╔══════════════════════════════════════════════╗" << endl;
        cout << "║           🧾 FRUIT SHOP RECEIPT 🧾           ║" << endl;
        cout << "╠══════════════════════════════════════════════╣" << endl;
        cout << "║  Item          Price   Qty    Total          ║" << endl;
        cout << "╠══════════════════════════════════════════════╣" << RESET << endl;
        
        for (const auto& item : items) {
            string fruitColor = RESET;
            for (const auto& fruit : availableFruits) {
                if (fruit.name == item.name) {
                    fruitColor = fruit.color;
                    break;
                }
            }
            
            cout << fruitColor << "║  " << left;
            cout << setw(12) << item.name;
            cout << "Rs." << setw(6) << fixed << setprecision(2) << item.price;
            cout << setw(6) << item.quantity;
            cout << "Rs." << setw(8) << item.total;
            cout << "║" << RESET << endl;
        }
        
        cout << GREEN << "╠══════════════════════════════════════════════╣" << RESET << endl;
        cout << YELLOW << BOLD << "║  GRAND TOTAL:                 Rs. " << setw(8) << fixed << setprecision(2) << grandTotal << " ║" << RESET << endl;
        cout << CYAN << "║  CASH GIVEN:                  Rs. " << setw(8) << cashGiven << " ║" << RESET << endl;
        cout << GREEN << BOLD << "║  CHANGE:                     Rs. " << setw(8) << change << " ║" << RESET << endl;
        cout << GREEN << "╚══════════════════════════════════════════════╝" << RESET << endl;
        
        cout << "\n" << GREEN << "🍎 Thank you for shopping! Visit again! 🍍" << RESET << endl;
    }

    void startOrder() {
        char choice;
        
        cout << "\n" << MAGENTA << BOLD;
        cout << "╔════════════════════════════════════╗" << endl;
        cout << "║     🛒 WELCOME TO FRUIT SHOP 🛒     ║" << endl;
        cout << "╚════════════════════════════════════╝" << RESET << endl;
        
        do {
            showAvailableFruits();
            addItem();
            calculateGrandTotal();
            
            cout << "\n📊 Current Total: Rs. " << fixed << setprecision(2) << grandTotal << endl;
            
            if (grandTotal >= 100) {
                cout << RED << "⚠️ Warning: You've reached the maximum limit (Rs. 100)!" << RESET << endl;
                break;
            }
            
            cout << "\n❓ Do you want to add more items? (y/n): ";
            cin >> choice;
            
            while (choice != 'y' && choice != 'Y' && choice != 'n' && choice != 'N') {
                cout << RED << "Invalid choice! Enter y or n: " << RESET;
                cin >> choice;
            }
            
        } while ((choice == 'y' || choice == 'Y') && grandTotal < 100);
        
        if (grandTotal > 100) {
            cout << RED << "\n❌ Total exceeds Rs. 100! Please remove some items." << RESET << endl;
            return;
        }
        
        if (processPayment()) {
            printReceipt();
        } else {
            cout << RED << "\n❌ Order cancelled." << RESET << endl;
        }
    }
};

int main() {
    #ifdef _WIN32
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD consoleMode;
    GetConsoleMode(hConsole, &consoleMode);
    consoleMode |= ENABLE_VIRTUAL_TERMINAL_PROCESSING;
    SetConsoleMode(hConsole, consoleMode);
    #endif
    
    FruitShop shop;
    shop.startOrder();
    
    cout << "\n" << BOLD << "Press Enter to exit..." << RESET;
    cin.ignore();
    cin.get();
    
    return 0;
}