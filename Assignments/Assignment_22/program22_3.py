######################################################################
#
#   Function name : Arithmetic
#   Description   : Prints the Addition,Substraction,Multiplication,
#                   Divison of the two numbers
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 27/01/2026
#
######################################################################

class Arithmetic:
    
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
        self.Add = 0
        self.Sub = 0
        self.Multi = 0
        self.Div = 0

    def Accept(self):

        print("Enter first number :")
        self.Value1 = int(input())

        print("Enter second number :")
        self.Value2 = int(input())
    
    def Addition(self):
        
        self.Add = self.Value1 + self.Value2
    
    def Substraction(self):

        self.Sub = self.Value1 - self.Value2
    
    def Multiplication(self):

        self.Multi = self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            return ZeroDivisionError
        else:
            self.Div = self.Value1 / self.Value2

    def Display(self):
        print("Addition is :",self.Add)
        print("Substraction is :",self.Sub)
        print("Multiplication is :",self.Multi)
        print("Division is :",self.Div)
  
Obj1 = Arithmetic()  

Obj1.Accept()
Obj1.Addition()
Obj1.Substraction()
Obj1.Multiplication()
Obj1.Division()
Obj1.Display()
###########################################################################
#
#   Input : 15,10   Output : Addition is : 25
#                            Substraction is : 5
#                            Multiplication is : 150
#                            Division is : 1.5
#
#   Input : 15,0    Output : Addition is : 15
#                            Substraction is : 15
#                            Multiplication is : 0
#                            Division is : 0
###########################################################################