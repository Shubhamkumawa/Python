######################################################################
#
#   Function name : Demo
#   Description   : Prints the instance variable in Fun and Gun function 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 27/01/2026
#
######################################################################

class Demo:
    Value = 0

    def __init__(self,No1,No2):
        self.No1 = No1
        self.No2 = No2
    
    def Fun(self):
        print("Instance Variable in Fun :",self.No1,self.No2)
    
    def Gun(self):
        print("Instance Variable in Gun :",self.No1,self.No2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()
obj2.Fun()

obj1.Gun()
obj2.Gun()

###########################################################################
#
#   Output : Instance Variable in Fun : 11 21
#            Instance Variable in Fun : 51 101
#            Instance Variable in Gun : 11 21
#            Instance Variable in Gun : 51 101
#
###########################################################################