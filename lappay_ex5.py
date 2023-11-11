""" John Mark J. Lappay             CD4L
This program asks the user to input a word in Filipino, in which through string and list operations, it translates into tadbalik. For
instance the word baliktad, becomes tadbalik 
"""

#Ask the user for the input
word = input("Enter a Filipino Word:")
word_listed = []   #declare an empty list for later use
i = 0              #initiate the counter, i

for letter in word:
    i += 1                      #increment the counter to be used to access the list later
    word_listed.append(letter)  #append each letter accessed from the string to the created list
    
for i in range(-1,-i-1, -1):    #access elements of the list, starting from the last letter up to the first letter
    if(word_listed[i]=='a' or word_listed[i]=='e' or word_listed[i]=='i' or word_listed[i]=='o' or word_listed[i]=='u'):
        if (word_listed[i-1] == 'a' or word_listed[i-1] == 'e' or word_listed[i-1] == 'i' or word_listed[i-1] == 'o' or word_listed[i-1] == 'u'): #if found a vowel, check if the letter preceding is a vowel
            index1 = i #include this index as the new starting letter for the translated word
            break #stop the loop since were searching from the last letter of the word, hence the first found consonant is the last consonant in the letter.
        elif (word_listed[i-1] != 'a' or word_listed[i-1] != 'e' or word_listed[i-1] != 'i' or word_listed[i-1] != 'o' or word_listed[i-1] != 'u'): #if found a vowel, check if the letter preceding it is not a vowel (a consonant)
            if(word_listed[i-1]=='g' and word_listed[i-2]=='n' or word_listed[i-2]=='m'): 
                 index1 = i-2  #get the next next preceeding letter on switching to accomodate for mga, nga or ang
            else:   
                index1 = i-1 #first letter of translated word
            break #stop the loop since were searching from the last letter of the word, hence the first found consonant is the last consonant in the letter.

#convert the negative index to positive, to be accessed using positive index
index1_translate = len(word) + index1 #this will be index that indicate the starting letter and where we would slice the word entered.

#print the translated word 
translated_word = word[index1_translate:len(word)] + word [0:index1_translate]
print("The translated word is:", translated_word)