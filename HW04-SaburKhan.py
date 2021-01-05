# Name: Sabur Khan
# Date: 10/29/19
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description: Hawaiian words
######### Algorithm/Psuedocode ########

#1. Create two dictionaries that will include vowels and the groups of vowels. Don't need consonants b/c you can just call the index of the word
#2. Have a while loop to check the word length and keep the program running, keep a counter and tracker to keep track of each letter/group
#3. Increase index by one to see if any of the grouping matches 
#4. Otherwise if nothing is collected. By using None since were using a dictionary just collect the index 
#5. If data is collected then add the '-'
#6. Lastly append the data to the list then convert it to a string to return it to main menu.

# Function Description: Reads the dictionary's down below in order to translate an enlgish word into hawaiian
# Precondition: a String that is not empty
# Postcondition: returns the translation and pronounciation of the word with the dashes.
def readDict(word):
    vowels = {
    'a': 'ah',
    'e': 'eh',
    'i': 'ee',
    'o': 'oh',
    'u': 'oo'
    }

    Vowel_groups = {
    'iw': 'v',
    'ew': 'v',   
    'ai': 'eye',
    'ae': 'eye',
    'ao': 'ow',
    'au': 'ow',
    'ei': 'ay',
    'eu': 'eh-oo',
    'iu': 'ew',
    'oi': 'oyo',
    'ou': 'ow',
    'ui': 'ooey'
    }   
    word = word.lower()
    final = []
    i=0
    
    while i<len(word):
        check = word[i]
        if(i < len(word)-1):
            count = check + word[i+1]
            dvowel = Vowel_groups.get(count)
            if(dvowel == None):
                dvowel = vowels.get(check)
            else:
                i+=1
        else:
            dvowel = vowels.get(check)
            
        if(dvowel != None and i<len(word)-1): #adds the dash between the words as long as more words remain 
            dvowel+= '-'
            
        final.append(dvowel or check) #appends the pair/character 
        i+=1
    str = ""
    return (str.join(final))

def main():
    choice = input("Enter the word you are trying to translate: ")
    if not choice:
        print("Sorry please try again.")
        main()
    else:
        print("The translation is: " + readDict(choice))
    choice2 = input("Would you like to try another word? Y/N ")
    if choice2 == 'Y':
        main()
    elif choice2 == 'N':
        print("Goodbye!")
main()
    
            
        
    