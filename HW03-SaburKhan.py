# Name: Sabur Khan
# Date: 10/10/19
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description: Spanish-English Dictionary
######### Algorithm/Psuedocode ########

#1. create function that reads/updates through the dictionary.txt file and stores it into a dictionary, even count will represent english, odd-spanish
#2. create function that iterates through the dictionary from the function above to read all the keys
#3. the next function will do the same thing but this time iterate through the values
#4. To add words into the dictionary Append into the file and use \n to update each line with english/spanish
#5. To display all the spanish words or english words iterate through all keys/values and print them.


# Function Description: Reads the dictionary.txt file 
# Precondition: dictionary.txt
# Postcondition: updates a dictionary with contents from the txt file
def readDict():
    spanishDict ={}
    count = 0
    file1 = open("dictionary.txt", "r")
    for lines in file1:
        lines = lines.strip()
        if count % 2 == 0:
            spanishDict[lines]= "test"
            count+=1
            str = lines
        else:
            if count % 2 ==1:
                spanishDict[str] = lines
                count+=1          
    file1.close()
    return spanishDict
# Function Description: finds the english word in dictionary and prints the spanish translation
# Precondition: spanishDict, dictionary containing all the words
# Postcondition: the spanish translation
def transEnglish():
    english = input("Enter the english word you are trying to translate into spanish: ")
    dict = readDict()
    for i in dict:
        if i == english:
            return dict[i]
# Function Description: finds the spanish word in dictionary and prints the english translation
# Precondition: spanishDict
# Postcondition: english translation     
def transSpanish():
    spanish = input("Enter the spanish word you are trying to translate into english: ")
    dict = readDict()
    for i,j in dict.items():
        if j == spanish:
            return i
# Function Description: adds an english term to txt file with spanish translation
# Precondition: dictionary.txt
# Postcondition: the txt file will be updated with those words              
def addEnglish():
    word = input("Enter a english word into the dictionary: ")
    translation = input("Now enter the spanish translation for that word: ")
    file1 = open("dictionary.txt", "a")
    file1.write("\n" + word + "\n")
    file1.write(translation)
# Function Description: adds an spanish term to txt file with english translation
# Precondition: dictionary.txt
# Postcondition: updates txt file with the words input.
def addSpanish():
    translation = input("Enter a spanish word into the dictionary: ")
    word = input("Now enter the english translation for that word: ")
    file1 = open("dictionary.txt", "a")
    file1.write("\n" + word + "\n")
    file1.write(translation)  

# Function Description: Displays all Key's in spanishDict
# Precondition: spanishDict 
# Postcondition: displays all english words
def displayEnglish():
    dict = readDict()
    for i,j in dict.items():
        print(i)
    main()
# Function Description: Displays all values in the spanishDict
# Precondition: spanishDict
# Postcondition: Display all spanish words
def displaySpanish():
    dict = readDict()
    for i,j in dict.items():
        print(j)
    main()
# Function Description: The main function to represent choices/options
# Precondition: dictionary.txt, and functions above
# Postcondition: the choice selected by user
def main():
    choice = int(input("Option 1 to translate English-Spanish. \nOption 2 to translate Spanish-English. \nOption 3 to add a new English word to the dictionary with Spanish translation. \nOption 4 to add a new Spanish word into the dictionary with English translation.\nOption 5 to display all English words. \nOption 6 to display all Spanish words. \nOption 7. Exit."))
    if(choice==1):
        print("Option 1 has been selected.")
        print(transEnglish())
        main()
    elif(choice==2):
        print("Option 2 has been selected.")
        print(transSpanish())
        main()
    elif(choice==3):
        print("Option 3 has been selected.")
        addEnglish()
        readDict()
        main()
    elif(choice==4):
        print("Option 4 has been selected.") 
        addSpanish()
        readDict()
        main()
    elif(choice==5):
        print("Option 5 has been selected.")
        displayEnglish()
    elif(choice==6):
        print("Option 6 has been selected.")
        displaySpanish()
    elif(choice==7):
        print("Now Exiting.")
    else:
        print("Sorry invalid option, try again")
        main()
main()

    