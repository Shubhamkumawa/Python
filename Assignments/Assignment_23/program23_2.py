######################################################################
#
#   Function name : BankAccount
#   Description   : Prints the Book name,Book author,No of Bbooks
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 27/01/2026
#
######################################################################

class BankAccount:
    
    ROI= 10.5
    
    def __init__(self):
        self.Name = ""
        self.Amount = 0  
       
        print("Enter name of the account holder :")
        self.Name = input()

        print("Enter initila amount :")
        self.Amount = int(input())


    def Display(self):
        print(f"\nName of the account holder :{self.Name}")
        print(f"Current Balance :{self.Amount}\n")
    
    def Deposite(self):
        deposite = 0
        print("Enter the amount to be deposite :")
        deposite = int(input())
        self.Amount = deposite + self.Amount
        print(f"Deposited {deposite} successfully.")
        self.Display()
    
    def Withdraw(self):
        withdraw = 0
        print("Enter the amount to withdraw :")
        withdraw = int(input())

        if self.Amount - withdraw < 500:
            print("Insufficient balance...")
        else:
            self.Amount = self.Amount - withdraw
            print(f"Withdrawn{withdraw} sucessfully.")
            self.Display()
    
    def CalculateInterest(self):
        Interest = 0
        Total = 0
        Interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest amount :",Interest)
        Total = self.Amount + Interest
        print("Total Amount After interest :",Total)
    

Obj1 = BankAccount()  
Obj1.Display()
Obj1.Deposite()
Obj1.Withdraw()
Obj1.CalculateInterest()

Obj2 = BankAccount()  
Obj2.Display()
Obj2.Deposite()
Obj2.Withdraw()
Obj2.CalculateInterest()


#######################################################################################################################
#
#   Input1 : Shubham , 100      Output : Name of the account holder :Shubham
#                                        Current Balance :100
#
#                                        Enter the amount to be deposite : 2000
#                                        Deposited 2000 successfully.
#                                        Name of the account holder :Shubham
#                                        Current Balance :2100
#
#                                        Enter the amount to withdraw :
#                                        300
#                                        Withdrawn 300 sucessfully.
#                                        Name of the account holder :Shubham
#                                        Current Balance :1800
#
#                                        Interest amount : 189.0
#                                        Total Amount After interest : 1989.0
# 
#   Input2 : Pranav , 500       Output : Name of the account holder : Pranav
#                                        Current Balance :500
#
#                                        Enter the amount to be deposite : 2000
#                                        Deposited 2000 successfully.
#                                        Name of the account holder : Pranav
#                                        Current Balance :2500
#
#                                        Enter the amount to withdraw :
#                                        3300
#                                        Insufficient balance...
#                                        
#                                        Interest amount : 262.5
#                                        Total Amount After interest : 2762.5
#     
#######################################################################################################################