# Name: Sabur Khan
# Date: 9/24/19
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description: To find if a phrase is a palindrome.
######### Algorithm/Psuedocode ########

#1.Read from files
#2. Put it into 2 different lists
#3. compare each of the lists to find words that aren't the same
#4. put contents of the words that are not similar into a new list
#5. print list#3 out.

# Function Description: 
# Precondition: 
# Postcondition: 

# Function Description: This function will read the 2 files
# Precondition: the 2 files
# Postcondition: 2 lists with contents of both files.
def reading():
    list1 = []
    list2 = []
    list3=[]
    file1 = open ("input.txt", "r")
    file2 = open("output.txt", "r")
    for line in file1:
        list1 = line.lower().split(" ")
    for lines in file2:
        list2 = lines.lower().split(" ")
    file1.close()
    file2.close()
    for word in list1:
        uncommon = True
        if word in list2:
            uncommon = False
            list2.remove(word)
        if uncommon:
            list3.append(word)
    return list3 + list2            
print(reading())          
            
