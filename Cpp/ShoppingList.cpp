// Simple Shopping List CLI App in CPP

#include <iostream>
#include <vector>
#include <string>
#include <limits>

using namespace std;

vector<string> item_names;
vector<string> item_quantities;

// Read a single-digit integer (returns -1 for invalid input)
int r_int() {
    string input;
    getline(cin, input);
    if (input.size() == 1 && isdigit(input[0])) {
        return input[0] - '0';
    }
    return -1;
}

// Read a string, returns "0" if input is empty
string r_str() {
    string input;
    getline(cin, input);
    if (input.empty()) {
        return "0";
    }
    return input;
}

int main() {
    while (true) {
        // Menu display
        cout << "\n--Shopping List--\n";
        cout << "1. Add Item\n2. Delete Item\n3. Show List\n0. Close\nChoice: ";
        int menu = r_int();

        switch (menu) {
            case 1: {  // Add item
                cout << "Item name: ";
                string name = r_str();
                if (name != "0") {
                    cout << "Item quantity: ";
                    string quantity = r_str();
                    if (quantity != "0") {
                        item_names.push_back(name);
                        item_quantities.push_back(quantity);
                        cout << "\nItem added!\n";
                    }
                }
                break;
            }

            case 2: {  // Delete item
                while(true){
                    if (!item_names.empty()) {
                        cout << "\nChoose item to remove:\n";
                        for (size_t i = 0; i < item_names.size(); ++i) {
                            cout << i + 1 << ". " << item_names[i] << "\n";
                        }
                        cout << "0. (Back)\nChoice: ";
                        int choice = r_int();
                        if (choice == 0) break;
                        if (choice > 0 && choice <= static_cast<int>(item_names.size())) {
                            cout << "\nItem " << item_names[choice - 1] << " removed!\n";
                            item_names.erase(item_names.begin() + (choice - 1));
                            item_quantities.erase(item_quantities.begin() + (choice - 1));
                        } else {
                            cout << "\nInvalid Input!\n";
                        }
                    } else {
                        cout << "\nYou don't have any items in the list...";
                        cin.ignore(numeric_limits<streamsize>::max(), '\n');
                        break;
                    }
                }
                break;
            }

            case 3: {  // Show list
                if (!item_names.empty()) {
                    cout << "\nYour shopping list:\n";
                    for (size_t i = 0; i < item_names.size(); ++i) {
                        cout << i + 1 << ". " << item_names[i] << " - " << item_quantities[i] << "\n";
                    }
                    cout << "\n(Back)";
                    cin.ignore(numeric_limits<streamsize>::max(), '\n');
                } else {
                    cout << "\nYou don't have any items in the list...";
                    cin.ignore(numeric_limits<streamsize>::max(), '\n');
                }
                break;
            }

            case 0:  // Exit
                cout << "Exiting...\n";
                return 0;

            default:
                cout << "\nInvalid Input!\n";
        }
    }
}
