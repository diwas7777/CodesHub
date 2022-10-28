import pickle
lib = open('books.dat', 'wb')
lib.close
while(1):
    print("1.Write \n2.Read \n3.Search \n4.Exit \nEnter Your Choice: ")
    x = int(input())
    if(x == 1):
        library = open('books.dat', 'ab')
        n = int(input("Enter the number of books to write:"))
        while(n):
            bookArray = []
            bookArray.append(input("\nEnter the Book ISSN: "))
            bookArray.append(input("Enter the Book Title: "))

            bookArray.append(input("Enter the Book Price: "))
            bookArray.append(input("Enter the Book Edition: "))
            bookArray.append(input("Enter the Book Year: "))
            bookArray.append(input("Enter the Book Author Name: "))
            pickle.dump(bookArray, library)
            n -= 1
        library.close
    elif(x == 2):
        library = open('books.dat', 'rb')
        while(1):
            try:
                bookinfo = pickle.load(library)
                print("Book Details:", bookinfo)
            except EOFError:
                library.close
                break
    elif(x == 3):
        library = open('books.dat', 'rb')
        booktitle = input("Enter the book title you want to search: ")
        while(1):
            try:
                bookinfo = pickle.load(library)
                if(booktitle == bookinfo[1]):
                    print("\n------BOOK FOUND------\n")
                    print("BOOK ISSN  :", bookinfo[0], "\nBOOK TITLE   :", bookinfo[1], "\nBOOK PRICE   : ", bookinfo[2],
                          "\nBOOK EDITION : ", bookinfo[3], "\nBOOK YEAR     : ", bookinfo[4], "\nBOOK AUTHOR NAME : ", bookinfo[5])
                    break
            except EOFError:
                print("\nBook Not Found\n")
                library.close
                break
    elif(x == 4):
        exit()
    else:
        print("Invalid Input.\n")
