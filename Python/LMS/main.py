import functions #importing functions from functions.py
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n             Welcome to Library Management System \n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
functions.library_stock() #calling function library_stock() from functions.py

'''To show and perform actions on the main menu'''
a=0
while a != 3:
    try:
        a = int(input(
            "Enter '1' to borrow a book \nEnter '2' to return a book \nEnter '3' to exit.\n\nPlease select an option: "))
        if a == 1:
            print("You will now borrow a book \n")
            functions.borrow_books()   #calling function borrow_books() from functions.py
            
        elif a == 2:
            print("You will now return the book \n")
            functions.return_books()   #calling function return_books() from functions.py

        elif a == 3:
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n        Thank you for using our Library Management System \n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n")
            exit 

        else:
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \nInvalid input !!! \nPlease provide value as 1, 2 or 3 \n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n")
    except:
        print("Please provide input in integer form.\n")   #handling exception for non int values


