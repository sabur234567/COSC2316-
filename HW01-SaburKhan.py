import random
# Name: Sabur Khan
# Date: 9/10/19
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description: 
######### Algorithm/Psuedocode ########

#1. create function 1 which receives an int in its parameters and finds if is a prime number
#2. for loop in range2-number.
#3. if the num has a remainder of 0 then that means it is divisable by another number.
#4. Func 2,  2 ints in parameters (a<b). list all prime numbers in bewteen a-b.
#5. receives the 2 numbers then for loop in range(a,b), repeat steps from func1.
#6.Func 3, same steps from function 1 but import random.choice
#7.Also create a list to store the prime numbers into
#8. Func 4, create a range from the num, num*2
#9. Then repeat function 3.



# Function Description: recieves an int that is positive and finds if it is a prime number
# Precondition: positive integer 
# Postcondition: if it's a prime number or not
def prime(num):
    if num > 1:
        for i in range(2,num):
            if(num%i)==0:
                print(num, "is not a prime number.")
                break
        else:
            print(num, "is a prime number.")
    else:
        print("Sorry, invalid number.")
# Function Description: This function will check for prime numbers a- b.
# Precondition: Variable a and b.
# Postcondition: list of prime numbers from a-b.
def primeAtoB(a,b):
    if(a<b):
        for num in range(a,b+1):
            if num>1:
                for j in range(2,num):
                    if(num%j)==0:
                        break
                else:
                    print(num, "is a prime number.")
    else:
        print("Sorry, invalid number.")
# Function Description: This function will check for prime numbers a- b. Then output a random Prime number
# Precondition: Variable a and b.
# Postcondition: a random prime number 
def randPrime(a,b):
    list = []
    prime = True
    if(a<b):
        for num in range(a,b+1):
            if num>1:
                for j in range(2,num):
                    if(num%j)==0:
                        prime = False
                        break
                else:
                    list.append(num)
        print(random.choice(list))
    else:
        print("Sorry, invalid number.")

# Function Description: This function will find the next prime number
# Precondition: number input
# Postcondition: The next prime number
def nextPrime2(num):
    list = []
    prime = True      
    a = num *2
    if(a>num):
        for num in range(num+1,a):
            if num>1:
                for j in range(2,num):
                    if(num%j)==0:
                        prime = False
                        break
                else:
                    list.append(num)
        print(list[0])
    else:
        print("Sorry, invalid number.")
def main():
    loop = True
    while loop:
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Option 4")
        print("0. Exit")
        choice = int(input("Enter the option you would like to choose."))
        if(choice==1):
            print("Option 1 has been selected.")
            num = int(input("Enter a number."))
            prime(num)
        elif(choice==2):
            print("Option 2 has been selected.")
            a= int(input("Enter the first number."))
            b= int(input("Enter the second number."))
            primeAtoB(a,b)
        elif(choice==3):
            print("Option 3 has been selected.")
            a = int(input("Enter the first number."))
            b = int(input("Enter the second number."))
            randPrime(a,b)
        elif(choice==4):
            print("Option 4 has been selected.")
            num = int(input("Enter a number."))
            nextPrime2(num)
        elif(choice==0):
            print("Goodbye.")
            loop = False
            break
        else:
            print("Sorry invalid number. Try again.")  
main()