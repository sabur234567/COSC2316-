#Description: A function that returns the factorial of a positive number
#pre-condition: the function takes a positive integer n as its input
#post-condition: the function returns n!
def factorial(n):
    fact =1
    if n>0:
        for i in range(1,n+1):
            fact *= i 
        return fact
#Description: A function that returns true if the first parameter is evenly divisible by all number from 1 to the second parameter.
# pre-condition: the function takes two positve integers i and n such that i>=n
# post-condition: the function returns true if i is divisible by [i..n] by all numbers in between it
def divisible(i,n):
    for j in range(1,n+1):
        if i%j!=0:
            return False
    return True
num = int(input("Enter a positive number"))
#test functions
for ans in range(num,factorial(num)+1, num):
    if divisible(ans,num):
        print(str(ans))
        break
    