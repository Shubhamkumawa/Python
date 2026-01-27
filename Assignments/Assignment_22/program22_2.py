######################################################################
#
#   Function name : Circle
#   Description   : Prints the area and circumference of the circle
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 27/01/2026
#
######################################################################

class Circle:
    
    PI = 3.14

    def __init__(self):
        self.Radius = 0
        self.Area = 0
        self.Circumference = 0

    def Accept(self):

        print("Enter the Radius :")
        self.Radius = int(input())
    
    def CalculateArea(self):
        
        self.Area = Circle.PI*(self.Radius**2)
    
    def CalculateCircumference(self):

        self.Circumference = 2*Circle.PI*self.Radius
    
    def Display(self):
        print("Radius is :",self.Radius)
        print("Area is :",self.Area)
        print("Circumference is :",self.Circumference)
  
Obj1 = Circle()  

Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()
###########################################################################
#
#   Input : 5   Output : Radius is : 5
#                        Area is : 78.5
#                        Circumference is : 31.400000000000002 
#
###########################################################################