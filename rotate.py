# Name: Sabur Khan
# Date: 9/17/19
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description: To rotate a string ex: roate by 2 the string "hello" = "llohe"
######### Algorithm/Psuedocode ########

#1. receive the line by an input text file
#2. read each line 
#3. have a function that splits each word by the space in between them
#4. Then split the word by the input given to rotate
#5. so for rotate 2 in "Hello" [0:2] then store it into a variable and add it back into the string
#6. write the contents onto the output file

        
def rotate():
    num = int(input("Enter the rotation value: "))
    temp = []
    with open('input.txt', 'r') as i:
        lines = i.read().splitlines()
        for line in lines:
            line = line.rstrip()
            temp.append(line)  

def main():


        
main()