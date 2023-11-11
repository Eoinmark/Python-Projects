""" John Mark J. Lappay     CMSC-12 CD4L

This code is an menu which asks input from user and then uses three functions, one for each option in the main meny to take note the user's orders and stores the price of their orders.

"""
price = 0  #initialize the global variable, price

#Function for Menu
def Menu():
    x = input(""" 
    MAIN MENU
    [1] Choose Burgers
    [2] Add drinks 
    [3] Compute total and pay 
    [0] Exit 
    Enter choice:
    """)
    return x #prints the menu on the terminal and then returns the choice of the user to be used on the if conditions


#Function for choice 1
def choice1():
    price = 0       #initialize the price to zero (no orders yet)
    while(True):     #runs the loop until the user enters 0
        x = int(input("""       
        BURGERS
        [1] Etinum Regrub: P35.00
        [2] Double Etinum Regrub: P47.00
        [3] Bacon Cheese Regrub: P73.00
        [4] Triple Onion Regrub: P600.00
        [0] Back to main menu
        Enter choice:
        """))       #Prints the available burgers

        #using conditional statements, the price of the user's order is updated
        if x == 0:          #if the user chose to exit, stop the loop
            break
        elif x == 1:
            price += 35.0
        elif x == 2:
            price += 47.0
        elif x == 3:
            price += 73.0
        elif x == 4:
            price += 600.0
        else :
            print("choose among the available burgers")
    return price        #returns the total price of the items

#Function for choice 2
def choice2():
    print("Each drink costs 25.0, how many would you like?")
    x = int(input("Enter amount:"))
    drink = 25.50 * x               #calculate the price of the drink
    return drink                    #returns the total price of the items

#Function for choice 3 with formal parameter, price since it will be used to calculate the total bill of the customer
def choice3(price):                
    print("Your total is:", price)
    price = (price *0.07) + price
    print("Your total service charge of 7%",price)
    
    senior_id = input("Do you have a PWD or Senior Citizen ID? (y/n)")
    if senior_id == 'y':
        price = price - (price*0.2)                 #if the user has a senior/PWD ID, discount are made
        print("Your total amount with 20% discount: ",price)
    else:
        price = price
        
    payment = float(input("Enter amount to pay:"))          
    change = payment - price                        #Calculate the change from the user's input on their amount to pay
    print("Your change is:", change)                #display the calculated change of the user on the terminal
    print("Thank you for shopping!")
    
    
#Main program

while(True):                        
    choice = int(Menu())
    
    if choice == 0:                             #if the user chose to exit, stop the loop
        print('Goodbye!')
        break
    elif choice == 1:                           #for the burgers
        price += float(choice1())
        print("Your current price to pay is:", price)
    elif choice == 2:                           #for the drinks
        price += float(choice2())
        print("Your current price to pay is", price)
    elif choice == 3:                           # for the total bill
        choice3(price)
