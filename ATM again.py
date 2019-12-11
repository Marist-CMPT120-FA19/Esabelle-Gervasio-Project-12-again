import os

class ATMfunc:

    def __init__(self, user, pw, bal1, bal2):
        self.user= user
        self.pw=pw
        self.bal1= bal1
        self.bal2= bal2

    def getTransaction(self):
        transaction=str(input("What would you like to do? "))
        return transaction

    def checkBal(self, kind):
        if (int(kind)==1):
            print("Your current balance is",self.formatCurrency(self.bal1))
        elif (int(kind)==2):
            print("Your current balance is",self.formatCurrency(self.bal2))

    def withdraw(self, amt ,kind):
        if(int(kind)==1):
            if(self.bal1 < amt):
                print("Insufficient funds.")
            else:
                self.bal1 -= amt
                self.checkBal(kind)
                return self.bal1
        elif(int(kind) ==  2):
            if(self.bal2 < amt):
                print("Insufficient funds.")
            else:
                self.bal2 -= amt
                self.checkBal(kind)
                return self.bal2
        else:
            print("Please enter a valid account, checking (1) or savings (2)")

    def deposit(self, amt, kind):
        if(int(kind) == 1):
            if(amt < 0):
                print("Can not deposit negative balance.")
            else:
                self.bal1 += amt
                self.checkBal(int(kind))
                return self.bal1
        elif(int(kind) == 2):
            if(amt < 0):
                print("Can not deposit negative balance")
            else:
                self.bal2 += amt
                self.checkBal(int(kind))
                return self.bal2
        else:
            print("Please enter a valid account, checking (1) or savings (2)") 

    def transfer (self, amt, kind):
        if(int(kind)==1):
            if(self.bal1 < amt):
                print("Insufficient funds in checking account")
            else:
                self.bal1 -= amt
                self.bal2 += amt
                self.checkBal(int(kind))
                return self.bal1
        elif (int(kind)==2):
            if(self.bal2 < amt):
                print("Insufficent funds in savings account")
            else:
                self.bal2 -= amt
                self.bal1 += amt
                self.checkBal(int(kind))
                return self.bal2
        else: 
            print("Please enter a valid account, checking (1) or savings (2)")
            
        
    def formatCurrency(self, amt):
        return "$%.2f" %amt

def readAccounts():
    accounts = []
    with open("accountinfo.txt") as accountFile:
        for line in accountFile:
            account = line.split(" ")
            accounts.append(ATMfunc(account[0], account[1], float(account[2]), float(account[3].strip())))
    return accounts

def writeAccounts(accounts):
    if(os.path.exists("accountinfo.txt")):
        os.remove("accountinfo.txt")
        
    with open("accountinfo.txt", "w") as accountFile:      
        for account in accounts:
            line = account.user + " " + account.pw + " " + str(account.bal1) + " " + str(account.bal2) + "\n"
            accountFile.write(line)
        accountFile.close()

def getUserAccount(accounts):
    id = input("Enter your user id: ")
    pin = int(input("Enter your pin number: "))
    for account in accounts:
        if(account.user == id):
            if(int(account.pw) == pin):
                return account
    print("Account with the given user and pin was not found.")
    return 0

def printMenu():
    print("Welcome to the ATM")
    print("Enter 'b'(balance), 'd'(deposit), 'w'(withdraw), 't'(transfer), or'q'(quit)")

def main(ATMAccount):
    printMenu()
    command= ATMAccount.getTransaction()

    while command!="q":
        if (command=="b"):
            account= input("Would you like to check the balance of (1)checking or (2)savings")
            ATMAccount.checkBal(account)
            printMenu()
            command= ATMAccount.getTransaction()
        elif (command=="d"):
            amt=float(input("Amount to deposit? "))
            account= input("Would you like to deposit into (1)checking or (2)savings")
            ATMAccount.deposit(amt, account)
            printMenu()
            command= ATMAccount.getTransaction()
        elif (command=="w"):
            amt=float(input("Amount to withdraw? "))
            account= input("Would you like to withdraw from (1)checking or (2)savings")
            ATMAccount.withdraw(amt, account)
            printMenu()
            command= ATMAccount.getTransaction()
        elif (command=="t"):
            amt= float(input("How much would you like to transfer: "))
            account= input("Transfer from (1) checking to savings or (2) savings to checking: ")
            ATMAccount.transfer(amt, account)
            printMenu()
            command= ATMAccount.getTransaction()
        else:
            print("Incorrect command. Please try again.")
            printMenu()
            command= ATMAccount.getTransaction()

    print("Goodbye! See you again soon")

accounts = readAccounts()
userAccount = getUserAccount(accounts)
if(userAccount != 0):
    main(userAccount)
    writeAccounts(accounts)
    

   
    
