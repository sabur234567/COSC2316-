import itertools
import string
import hashlib
# Name: Sabur Khan
# Date: 11/10/19
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description: MD%  and SHA! Hash values
######### Algorithm/Psuedocode ########
#1. enter md5 value
#2. enter sha1 value
#3 iterate through a-z 0-9 for all possible combinations
#4. to iterate through all letters string.ascii_letters, numbers: string.digits

# Function Description: Takes in the MD5 Hash value, tries to find the string version of it
# Precondition: a String that is not empty, proper MD5 Hash value of 3 letters and 3 digits
# Postcondition: Returns the password if it is found, if not. Then returns value was not found
def askMd5():
    testInput = input("Enter the MD5 Hash Value you wish to crack.")
    
    for s in itertools.product(string.digits,repeat=3):
        for d in itertools.product(string.ascii_letters,repeat=3):
            x = (''.join(d+s  ))
            md5Test = hashlib.md5(x.encode())
            if md5Test.hexdigest() == testInput:
                print("Found the password: " +x)
                main()
            else:
                continue
    print("Your Value was not found.")
    main()
# Function Description: Takes in the SHA1 Hash value, tries to find the string version of it
# Precondition: a String that is not empty, proper sha1 Hash value of 3 letters and 3 digits
# Postcondition: Returns the password if it is found, if not. Then returns value was not found
def askSha1():
    testInput = input("Enter the SHA1 Hash Value you wish to crack.")
    
    for s in itertools.product(string.digits,repeat=3):
        for d in itertools.product(string.ascii_letters,repeat=3):
            x = (''.join(d+s  ))
            sha1Test = hashlib.sha1(x.encode())
            if sha1Test.hexdigest() == testInput:
                print("Found the password: " + x)
                main()
            else:
                continue
    print("Your Value was not found.")
    main()
# Function Description: Takes in the values from functions and outputs the password is found or not through menu options
# Precondition: proper options are entered by user to select option
# Postcondition: Returns the function that is asked for by user.
def main():
    choice = int(input("Option 1 to enter a MD5 hash value \nOption 2 to enter a SHA1 hash value. \nOption 3. Exit."))
    if(choice==1):
        print("Option 1 has been selected.")
        askMd5()
        main()
    elif(choice==2):
        print("Option 2 has been selected.")
        askSha1()
        main()
    elif(choice==3):
        print("Option 3 has been selected. GoodBye!")
    else:
        print("Sorry Invalid Option, try again.")
        main()
main()      