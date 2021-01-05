# Name: Sabur Khan
# Date: 9/10/19
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description: To find if a phrase is a palindrome.
######### Algorithm/Psuedocode ########

#1.Asking user for a string input.
#2. Create a temp variable
#3. iterate backwards through the string onto the new variable
#4. Check if the user's string input and temp string variable are the same.
#5. If they're the same it is a palindrome.


# Function Description: 
# Precondition: 
# Postcondition: 

# Function Description: This function will reverse the string
# Precondition: the string input
# Postcondition: a reversed string
def reverseString(orgWord):
    temp=""
    for i in orgWord:
        temp = i + temp
    return temp 

# Function Description: This function will find out if the string is a palindrome.
# Precondition: the reversed string
# Postcondition: If the variable is a palindrome or not.
def isPalindrome(originalWord):
    return(reverseString(originalWord)== originalWord)

#Driver Program
def main():
    fileIn = open ("input.txt", "r")
    fileOut = open("output.txt", "w")
    lines = fileIn.read().splitlines()
    for line in lines:
        print(isPalindrome(line))
        fileOut.write(str(isPalindrome(line))+ "\n")
    fileIn.close()
    fileOut.close()
   
main()