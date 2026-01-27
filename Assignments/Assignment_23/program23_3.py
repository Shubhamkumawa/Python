######################################################################
#
#   Function name : Numbers
#   Description   : Prints Pirme , Perfect , Factors , Sum of factors 
#                   of a number 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 27/01/2026
#
######################################################################

class Numbers:
    
    
    
    def __init__(self):
        
        self.Value = 0

        print("Enter a number :")
        self.Value = int(input())
    
    def ChkPrime(self):
        isPrime = False
        if self.Value <= 1:
            isPrime = False
        else:
            isPrime = True
            for i in range(2,self.Value):
                if self.Value%i == 0:
                    isPrime = False

        if isPrime == True:
            print(f"{self.Value} is Prime number")
        else:
            print(f"{self.Value} is not Prime number")

    def ChkPerfect(self):

        isPerfect = 0

        for i in range(1,self.Value):
            if self.Value % i == 0:
                isPerfect = isPerfect + i

        if isPerfect == self.Value:
            print(f"{self.Value} is Perfect number")
        else:
            print(f"{self.Value} is not Perfect number")

    def Factors(self):

        print(f"Factors of {self.Value} are :",end=" ")
        for i in range(1,self.Value):
            if self.Value%i == 0:
                print(i,end=" ")
    
    def SumFactors(self):
        sum = 0
        for i in range(1,self.Value):
            if self.Value%i == 0:
                sum = sum + i
        print(f"\nSum of factors of {self.Value} is :",sum)
        

Obj1 = Numbers()  
Obj1.ChkPrime()
Obj1.ChkPerfect()
Obj1.Factors()
Obj1.SumFactors()

Obj2 = Numbers()  
Obj2.ChkPrime()
Obj2.ChkPerfect()
Obj2.Factors()
Obj2.SumFactors()

Obj3 = Numbers()  
Obj3.ChkPrime()
Obj3.ChkPerfect()
Obj3.Factors()
Obj3.SumFactors()

#######################################################################################################################
#
#   Input1 : 7            Output : 7 is Prime number
#                                 7 is not Perfect number
#                                 Factors of 7 are : 1
#                                 Sum of factors of 7 is : 1 
#
#   Input2 : 10           Output : 10 is not Prime number
#                                  10 is not Perfect number
#                                  Factors of 10 are : 1,2,5
#                                  Sum of factors of 10 is : 8 
#
#   Input2 : 15           Output : 15 is not Prime number
#                                  15 is not Perfect number
#                                  Factors of 15 are : 1,3,5
#                                  Sum of factors of 15 is : 9
#######################################################################################################################