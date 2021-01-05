# Name: Sabur Khan
# Date: 9/12/19
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description: To reverse the order of words in a given string
######### Algorithm/Psuedocode ########

#1.Receive the input of strings
#2. use the split function and have the words into a list
#3. reverse the list
#4. open a file with the list of words and run it through function with step #2-3
#5. close the files and output the list onto the output file.

def reverseLine(line):
    temp = [line]
    reverseList = temp[::-1]
    
    return reverseList
    
def main():
    newString = ""
    fileIn = open("input.txt", "r")
    fileOut = open("output.txt","w")
    lines = fileIn.read().splitlines()
    print(lines)
    for line in lines:
        for i in reverseLine(line):
            fileOut.write(i + " ")
        fileOut.write("\n")
    fileOut.close()
    fileIn.close()

main()