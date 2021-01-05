#factorial using recursion
#precondition: n is positive
#postcondition: returns n
from inClassCoding.palindrome import isPalindrome
def factorial(n):
    if(n<=1):
        return 1
    else:
        return n*factorial(n-1)

#recursion of palindrome
def isPalindrome(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            isPalindrome(s[1:-1])
        else:
            return False
        
# each number is the sum of the previous two
# Always do the base case in recursion, for an ex: the if(n==1) and n==0.
def fib(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return fib(n-1) + fib(n-2)
    

def itFib(n):
    old,new = 0,1
    if n ==0:
        return 0
    if n ==1:
        return 1
    for i in range(n-1):
        old,new = new,old+new
    return new


print(isPalindrome("racecar"))