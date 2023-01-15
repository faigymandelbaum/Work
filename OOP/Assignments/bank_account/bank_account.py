class BankAccount:

    def __init__(self, account_number, name, balance = 0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print ("Now your account balance is " , self.balance)
        return self.balance




    def withdraw(self, withdraw_amount):
        if self.balance - withdraw_amount >= 0 and withdraw_amount < 4000:
            self.balance = self.balance - withdraw_amount
            print("The task was successfully completed. Now you have " + str(self.balance) + " dollars in your account.")
        elif withdraw_amount > 4000:
            print ("You tried pulling $" + str(withdraw_amount) + " while the max withdrawl is $4000.")    
        else:
            print ('Sorry, we are unable to complete the task.')     



    def __str__(self):
        return self.name + ", welcome to the bank!"  + " We are always happy to serve you."  + " Your account number is " + str(self.account_number)      
