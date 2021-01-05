# Name: Sabur Khan
# Date: 10/15/19
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description: Largest Prime Factor
######### Algorithm/Psuedocode ########


#1. Function checking for factors
#2. Function checking for the Prime numbers
#3. Append all of it to a list 
#4. Find max() of list
#5. print max 



# Function Description: Factors of n 
# Precondition: positive number
# Postcondition: finds all factors of n 
def factors(n):
    list=[]
    for i in range(1,n+1):
        if n%i==0:
            list.append(i)
    return list
def isPrime(list): # isPrime doesn't work
    new_list = []
    for i in list:
        for j in range(2,i):
            if i%j ==0:
                return False
            else:
                new_list.append(j)
    return max(new_list)
            
def main():
    x = int(input("Enter a num."))
    list = factors(x)
    print(isPrime(list))
main()