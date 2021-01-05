# Name: Sabur Khan
# Date: 9/26/19
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description: 
######### Algorithm/Psuedocode ########

#1. Create a txt file for the wallet 
#2. Create a list to store all of the contents in the wallet into
#3. append all of the content from wallet onto the list
#4. iterate through list to find all possible values of coins/dollars. Use % 
#5. (100$,50$,20$,10$,5$,2$,1$, 0.5$, 0.25$, 0.10$, 0.05$, 0.01$) possible values
#6. then print all of the contents of the list out by reading lines. (end of function 1)
#6. use a balance variable to determine if user has enough money
#7. ask for bill amount and subtract from balance
#8. using mod and // find the exact amount of bills/coins needed
#9. spit out the amount left by using while loop and reduce the amount of bills slowly



# Function Description: reading contents from wallet.txt
# Precondition: wallet.txt 
# Postcondition: everything inside of wallet.txt with "$"
def balance():
    file1 = open("wallet.txt", "r")
    print("You have this much in your wallet:")
    for lines in file1:
        print("$"+lines)
    file1.close()
    main()
# Function Description: going to get bill and subtract it from total balance, write the change given back into wallet.txt
# Precondition: balance of wallet.txt, bill 
# Postcondition: the remaining amount left onto wallet.txt
def pay(bill):
    list = []
    new_list = []
    hundred = 0
    fifty=0
    twenty=0
    ten=0
    five=0
    two=0
    one=0
    fiftyCent=0
    twentyFiveCent=0
    tenCent=0
    fiveCent=0
    oneCent=0
    file1 = open("wallet.txt", "r")
    for line in file1:
        list.append(line.strip())
    for i in list: 
        new_list.append(float(i))
    tb = sum(new_list)
    if tb<bill:
        print("Insufficent funds Sorry")
    else:
        tb = tb-bill
        if tb>=100:
            hundred = tb//100
            tb %= 100
        if tb >= 50:
            fifty = tb//50
            tb %= 50
        if tb >= 20:
            twenty = tb//20
            tb %= 20
        if tb >= 10:
            ten = tb//10
            tb %= 10
        if tb >= 5:
            five = tb//5
            tb %= 5
        if tb >= 2:
            two = tb//2
            tb %= 2
        if tb >= 1:
            one = tb//1
            tb = tb-one
        if tb >= 0.50:
            fiftyCent = tb//0.50
            tb = tb - 0.50
        if tb >=0.25:
            twentyFiveCent = tb//0.25
            tb = tb- (0.25*twentyFiveCent)
        if tb >=0.10:
            tenCent = tb//0.10
            tb = tb- (0.10*tenCent)
        if tb >=0.05:
            fiveCent = tb//0.05
            tb = tb- (0.05*fiveCent)
        if tb >=0.01:
            oneCent = tb//0.01
            tb = tb- (0.01*oneCent)
        file1 = open("wallet.txt", "w")
        while hundred != 0:
            file1.write("100")
            file1.write("\n")   
            hundred -=1
        while fifty != 0:
            file1.write("50")
            file1.write("\n")   
            fifty -=1
        while twenty != 0:
            file1.write("20")
            file1.write("\n")   
            twenty -=1
        while ten != 0:
            file1.write("10")
            file1.write("\n")   
            ten -=1 
        while five != 0:
            file1.write("5")
            file1.write("\n")   
            five-=1
        while two != 0:
            file1.write("2")
            file1.write("\n")   
            two -=1
        while one != 0:
            file1.write("1")
            file1.write("\n")   
            one -=1
        while fiftyCent != 0:
            file1.write("0.50")
            file1.write("\n")   
            fiftyCent -=1
        while twentyFiveCent != 0:
            file1.write("0.25")
            file1.write("\n")   
            twentyFiveCent -=1
        while tenCent != 0:
            file1.write("0.10")
            file1.write("\n")   
            tenCent -=1
        while fiveCent != 0:
            file1.write("0.05")
            file1.write("\n")   
            fiveCent -=1
        while oneCent != 0:
            file1.write("0.01")
            file1.write("\n")   
            oneCent -=1
        file1.close()
    main() 
# Function Description: menu function, displays all the options.
# Precondition: functions from up top
# Postcondition: either function 1, function 2, or quit. or invalid option
def main():
    choice = int(input("Enter Option 1 to Check what is left in the wallet. \nEnter Option 2 to Pay your bill.\nEnter Option 3 to Quit."))
    if(choice==1):
        print("Option 1 has been selected.")
        balance()
    elif(choice==2):
        print("Option 2 has been selected.")
        bill = float(input("Enter the amount that needs to be payed."))
        pay(bill)
    elif(choice==3):
        print("Option 3 has been selected.")
        print("Exiting.")
    else:
        print("Sorry invalid number. Try again.") 
        main()
main()
