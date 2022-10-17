import datetime
def library_stock():
    try:
        '''forming dictionary form the text file'''
        library = {}
        book=[]
        file = open("library.txt", "r")
        i=0
        for line in file:
            i +=1
            line = line.replace("\n","")
            book=(line.split(","))
            library[i]= book
        '''To print the dictionary in tabular form'''     
        print("\n________________________________________________________________\n                    Books In The Library\n________________________________________________________________\n")
        print(": ID :    Book Name       :      Author     : Quantity : Price :")

        for key in library:
            print(":",key," :",
                  library[key][0]," "*(17-len(library[key][0])),":",        #len is used to substract from a fixed value to create even spacing betweens columns in table 
                  library[key][1]," "*(14-len(library[key][1])),":",
                  library[key][2]," "*(7-len(library[key][2])),":",
                  library[key][3]," "*(4-len(library[key][3])),":")
        print("________________________________________________________________\n")
        return library
    except:
        print("Books stocks file library.txt not found.")

def borrow_books():
    library_dic=library_stock() #calling function library_stock() and storing the returned dictionary in library_dic
    borrowed_books = []
    continueloop = 0
    available = "yes"
    price = 0
    priceTotal=0
    name = ""
    borrow_success = False

    while continueloop == 0:   #loops until user continues borrowing multiple books
        try:
            bookno= int(input("Enter the book id to borrow: "))
            available = "yes"
            try:
                if int(library_dic[bookno][2])!= 0:    #Checking if book is available to borrow
                    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nThe book is available.\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

                    #Validation for name
                    if name == "":
                        while(True):
                            name = input("Enter the borrower's name: ")
                            if name.replace(" ","").isalpha():      #Cheking if the input is in alphabets 
                                break
                            print("Please enter name in alphabets.\n")
                    else:
                        print("Name of customer: ",name)
                    
                    price = library_dic[bookno][3].replace("$","")   #replacing $ with empty string for numerical operations
                    priceTotal = priceTotal + int(price)    
                    time_object = datetime.datetime.now()
                    print("\nBorrowed Successfully! \nThe total price is: $",priceTotal, "and the time at borrow is",time_object  )
                    library_dic[bookno][2]= int(library_dic[bookno][2])-1   #decreasing the value in dictionary after borrow
                    borrowed_books.append(library_dic[bookno][0])
                else :
                    print("Sorry! Book is not available.\n")
                    available = "no"
                    stopborrow= input("Press 'y' if the customer wants to borrow any other book instead.\n") #confirming if user wants another book because given book is out of stock
                    if stopborrow.lower() != "y":    
                        break
                    more = "a"

                if available == "yes":
                    more =input("\nIf the customer wants to borrow another book press 'y' else press any other button: ")   #confirming if user wants to borrow another book after a successfull borrow
                    
                    if more.lower() != "y":
                        continueloop = 1
                        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nCustomer Borrow Details\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                        print("Name of customer: ", name, "\nTotal price from borrow: ",price, "\nDate and time of borrow: ",time_object,"\nThe books borrowed are: "+ ', '.join(borrowed_books)+"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                    borrow_success= True
            except:
                print("Sorry, the book ID does not match. Please enter a valid ID.\n")
        except:
            print("Please enter book ID in integer format!\n")
            
    if borrow_success == True:
        '''updating stocks in text file'''
        file_borrowed = open("library.txt", "w")
        for key in library_dic:
            for i in range (4):
                file_borrowed.write(str(library_dic[key][i]))
                if i != 3:
                    file_borrowed.write(",")
            file_borrowed.write("\n")
        '''writing borrow details to a text file'''
        random = str(datetime.datetime.now().minute)+str(datetime.datetime.now().second)+str(datetime.datetime.now().microsecond)
        borrow_txt = open("Borrow_"+name+"("+random+").txt", "w")
        borrow_txt.write("Borrow Details:\n________________________________________________________________\n\nName of borrower: "+name+"\nTotal price of borrow: $"+str(priceTotal)+"\nDate and time of borrow: "+str(time_object)+"\nName of borrowed books: "+', '.join(borrowed_books))





def return_books():
    library_dic=library_stock()      #calling function library_stock() and storing the returned dictionary in library_dic
    returned_books = []
    continueloop = 0
    price = 0
    priceTotal=0
    grandTotal = 0
    name = ""
    return_success = False

    while continueloop == 0:              #loops until user continues returning multiple books
        try:
            bookno= int(input("Enter the book id to return: "))
            try:
                if bookno in library_dic:    #Checking if book exists in library
                    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nThe book is "+library_dic[bookno][0]+"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                    price = library_dic[bookno][3].replace("$","")           #replacing $ with empty string for numerical operations
                    priceTotal = priceTotal + int(price)
                    
                    if name == "":
                        while(True):
                            name = input("Enter the returner's name: ")
                            if name.replace(" ","").isalpha():               #Cheking if the input is in alphabets 
                                break
                            print("Please enter name in alphabets.\n")
                    else:
                        print("Name of customer: ",name)

                    while(True):
                        try:
                            days= int(input("\nEnter the days customer has borrowed the book: "))  #converting days input to integer
                            available = "yes"
                            if days <= 0:       #to reject any negative or 0 value in days
                                    print ("Enter valid number of days.")
                            elif days>10:
                                extra_days = days-10   #calculating extra days and calculating fine
                                fine = extra_days * 1
                                print ("The book is returned ", extra_days,"days late. And the fine amount is: $", fine)
                                break
                            else:
                                fine = 0
                                print ("The book is returned in time. Thank you!")
                                break
                        except:
                            available = "no"
                            print("Invalid format!!! Please enter days in integer format.")
                            continue
                    
                if available == "yes":
                    priceTotal = fine + int(price)
                    time_object = datetime.datetime.now()
                    print("\nReturned Successfully! \nThe total price is: $",priceTotal, "and the time at return is",time_object  )
                    grandTotal = priceTotal+ grandTotal
                    library_dic[bookno][2]= int(library_dic[bookno][2])+1        #increasing the value in dictionary after return
                    returned_books.append(library_dic[bookno][0])
                    more = "a"
                    more =input("\nIf the customer wants to return another book press 'y' else press any other button: ")        #confirming if user wants to return another book after a successfull return
                    
                    if more.lower() != "y":
                        continueloop = 1
                        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nCustomer Return Details\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                        print("Name of customer: ", name, "\nTotal price from return: $",grandTotal, "\nDate and time of return: ",time_object,"\nThe books returned are: "+ ', '.join(returned_books)+"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                    return_success= True
            except:
                 print("Sorry, the book ID does not match. Please enter a valid ID.\n")
        except:
            print("Please enter book ID in integer format!\n")

    if return_success == True:
        '''updating stocks in text file'''
        file_returned = open("library.txt", "w")
        for key in library_dic:
            for i in range (4):
                file_returned.write(str(library_dic[key][i]))
                if i != 3:
                    file_returned.write(",")
            file_returned.write("\n")

        '''writing return details to a text file'''
        random = str(datetime.datetime.now().minute)+str(datetime.datetime.now().second)+str(datetime.datetime.now().microsecond)
        return_txt = open("Return_"+name+"("+random+").txt", "w")
        return_txt.write("Return Details:\n________________________________________________________________\n\nName of returner: "+name+"\nTotal price: $"+str(grandTotal)+"\nDate and time of return: "+str(time_object)+"\nName of returned books: "+', '.join(returned_books))
