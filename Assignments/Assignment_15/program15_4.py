######################################################################
#
#   Importing reduce() from the python library
#
######################################################################\

from functools import reduce

######################################################################
#   Function name : Addition
#   Description   : return the sum of the list  
#   Input         : List[]
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 19/01/2026
#######################################################################
 
Addition = lambda Number : reduce(lambda No1,No2 : No1 + No2, Number)

######################################################################
#   Function name : main
#   Description   : prints the sum of the list   
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 19/01/2026
#######################################################################
 
def main():
    Size = 0
    Value = []
    Ret = 0

    print("Enter the size of list")
    Size = int(input())
    
    print("Enter the",Size,"elements :")
    for i in range(Size):
        Value.append(int(input()))

    Ret = Addition(Value)

    print("Addition of all elements are :",Ret)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 5,[1,2,3,4,5]       Output : Addition of all elements are : 15 
#
##############################################################################