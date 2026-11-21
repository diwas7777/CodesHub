# Simple Shopping List CLI App in Python

item_names = []       # stores item names
item_quantities = []  # stores corresponding quantities

while True:
    # Display menu
    print("\n--Shopping List--")
    print("1. Add Item")
    print("2. Delete Item")
    print("3. Show List")
    print("0. Close")
    
    choice = input("Choice: ")
    
    # Validate menu input
    if not choice.isdigit():
        print("\nInvalid option.")
        continue
    
    menu = int(choice)
    
    if menu == 1:  # Add item
        name = input("Item name: ").strip()
        if name:
            quantity = input("Item quantity: ").strip()
            if quantity and quantity[0] != '0':
                item_names.append(name)
                item_quantities.append(quantity)
    
    elif menu == 2:  # Delete item
        while True:
            if item_names:
                print("\nChoose item to remove:")
                for i, name in enumerate(item_names, 1):
                    print(f"{i}. {name}")
                print("0. (Back)")
                
                choice = input("Choice: ")
                if not choice.isdigit():
                    print("\nInvalid input!")
                    continue
                
                choice = int(choice)
                
                if choice == 0:
                    break
                elif 1 <= choice <= len(item_names):
                    removed_name = item_names.pop(choice - 1)
                    item_quantities.pop(choice - 1)
                    print(f"\nItem {removed_name} removed!")
                else:
                    print("\nInvalid input!")
            else:
                print("\nYou don't have any items in the list...")
                input("(Press Enter to continue)")
                break
    
    elif menu == 3:  # Show list
        if item_names:
            print("\nYour shopping list:")
            for i, (name, quantity) in enumerate(zip(item_names, item_quantities), 1):
                print(f"{i}. {name} - {quantity}")
            input("\n(Back)")
        else:
            print("\nYou don't have any items in the list...")
            input("(Press Enter to continue)")
    
    elif menu == 0:  # Exit
        print("Exiting...")
        break
    
    else:  # Invalid menu choice
        print("\nInvalid option.")
