""" John Mark J. Lappay             CMSC 12 - CD4L
This code is emulates a bookstore inventory system by implementing the use of a dictionary. Users can input a book code which serves as the key in the book inventory dictionary, in which corresponds to a book title, author and quantity contained as a list for the key value. The program furthermore use defined functions for each choice of action the user do from the available choices in  the menu.
"""

#declare an empty dictionary
book_inventory = {}
empty = True                   #this flag is used to signify that the book_inventory is empty

# Functions
def Menu():                    #to display a Menu and ask input from user which action they want to do 
    x = input("""MAIN MENU \n       
    [1] Add Book
    [2] View All Books
    [3] Delete a Book
    [4] Delete All Books
    [5] Restock a Book
    [6] Consume a Book
    [0] Exit
    """)
    return x                   #returns a string value from 0-6 to be used in the loop of the main program

def addBook():                  #adds a new key and corresponding value to the book_inventory dictionary
    print("ADD BOOK")       
    book_code = input("Enter book code:")       #ask the user for a book code to be used as key in the dictionary
    book_title = input("Enter title:")
    book_author = input("Enter Author:")
    book_quantity = input("Enter quantity:")
    
    TitleAuthorQuantity = [book_code, book_title, book_author, book_quantity]  #A list to store book title, author and quantity.
    book_inventory[book_code] = TitleAuthorQuantity                 #The list is used as a value to correspond to a unique key which is the book_code for easier access of its corresponding book title, author and quantity
    print("The book has been succesfully added!")
    
    return book_inventory
    
        
def viewBooks():
    print("VIEW BOOKS \n")
    if empty == True:
        print("The inventory is empty")
    else:
        for book_code in book_inventory:     #To access information in a specific book through a book code key in the book inventory dictionary
            print("Code:", book_inventory[book_code][0])
            print("Title:", book_inventory[book_code][1])
            print("Author:", book_inventory[book_code][2])
            print("Quantity:", book_inventory[book_code][3],"\n")
    
    
def deleteBook():
    print("DELETE BOOK \n")
    book_code = input("Enter Book Code:")  #asks the user for a book code of which book to delete
    flag = book_code in book_inventory     #used as a flag to check whether the user inputted book code is in the book inventory
   

    if flag == False:                      #if the flag is false, then book is not currently stored in the book inventory
        print("This book does not exist")
    else:                                  #if the book is currently stored, then the book is deleted
        del book_inventory[book_code]
        print("The book has been deleted.")
    
def deleteAllBooks():
    print("DELETE ALL BOOKS \n")
    
    book_inventory.clear()                 #deletes all existing keys and values stored in the book inventory dictionary
    print("All books has been deleted.")

def restockBook():
    print("RESTOCK BOOK \n")
    if empty == True:                      #checks whether the inventory is empty through the empty flag
        print("The inventory is empty, nothing to restock.")
    else:                                  #if the inventory is not empty,asks the user for a book code
        book_code = input("Enter book code:")
        flag = book_code in book_inventory  #used to check if the book is currently in the inventory
        if flag == False:                  # if the book is not in the inventory.
            print("This book does not exist.")
        else:                       
            restock_amount = int(input("Enter amount to restock:"))     #if the book is currently in the inventory, asks the user the amount to restock
            previous_amount = int(book_inventory[book_code][3])         #accesses the current stock of the book
            new_amount = restock_amount + previous_amount               #adds the current stock to the amount to be restocked as specified by the user
            book_inventory[book_code][3] = new_amount                   #stores the restocked amount in the list value stored in the book inventory dictionary
            print("New stock of ", book_inventory[book_code][1] ," : ", book_inventory[book_code][3])   
    

def consumeBooks():
    print("CONSUME BOOK")
    if empty == True:                      # if the inventory is empty, tells the user there is nothing to consume
        print("The inventory is empty, nothing to consume.")
    else:                                  
        book_code = input("Enter book code:") #if the invetory is not empty, asks the user for a book code
        flag = book_code in book_inventory    #checks whether the book code is stored in the book inventory dictionary
        if flag == False:                     #if the book code is not stored in the dictionary, tells the user that the book does not exist
            print("This book does not exist.")
        else:
            consume_amount = int(input("Enter amount to consume:")) #if the book exists, asks the user the amount to consume
            previous_amount = int(book_inventory[book_code][3])     #accesses the current stock of the book
            new_amount = previous_amount - consume_amount           #decreases the amount of stocks based on the amount to consume as specified by the user
            if new_amount < 0:                                      #if the amount consumed is greater than the current stock (that is if their difference is negative or less than 0), then informs the user that there is not enough stock
                print("There is not enough stock")
            else:                                                   #if there is enough stock to consume, the new amount is stored in the book inventory dictionary
                book_inventory[book_code][3] = new_amount
                print("New stock of ", book_inventory[book_code][1] ," : ", book_inventory[book_code][3]) 
                print("Consumed ", consume_amount, " of ", book_inventory[book_code][1], " by ", book_inventory[book_code][2])
            


#Main program
while(True):
    choice = int(Menu())

#Using conditionals to do specific functions for each choice of the user    
    if choice == 0:       #break the loop if the user chooses to exit
        print("Goodbye!")
        break    
    elif choice == 1:
        addBook()
        empty = False     #Set empty to false since a book is added
    elif choice == 2:
        viewBooks()
    elif choice == 3:
        deleteBook()
    elif choice == 4:
        deleteAllBooks()
        empty = True      #Set this flag to true since all books are deleted, hence the inventory becomes empty
    elif choice == 5:
        restockBook()
    elif choice == 6:
        consumeBooks()
    else:
        print("please pick among the choices")

