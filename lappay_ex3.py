""" John Mark J. Lappay  CMSC-12 CD4L 
This code asks the user for a positive integer, N, then outputs the number of even and odd digits of N. If the user entered a nonpositive integer, the program exits.
"""

while(True) : #We put a loop to run continously under any conditions until a break statement 
    x = (input("Enter an integer, N: ")) #Ask input from user
    z = int(x)            #Convert input to integer
    if z <= 0:            # If the input is negative, break the loop
        break
    
    #Initialize counter variables"
    even_counter = 0        #Counter for even digits
    odd_counter = 0         #Counter for odd digits
               
    for element in x:        #To check for every digits of the integer, N
        check = int(element) #A "checker" to see if a digit is even or odd
        if check%2 == 0:     #If the modulo of a number with 2 is zero, then it is even
            even_counter += 1
        else :               #If the number has a remainder with 2, then it is odd
            odd_counter += 1
    #Print the output
    print("the even digits are:", even_counter) 
    print("the odd digits are:", odd_counter)
    
    

print("Goodbye!") #When the loop breaks, print goodbye