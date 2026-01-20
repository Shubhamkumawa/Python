######################################################################
#
#   Importing reduce() from the python library
#
######################################################################\

from functools import reduce

######################################################################
#   Function name : Product
#   Description   : return the product of the list
#   Input         : List[]
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 19/01/2026
#######################################################################
 
Product = lambda Number : reduce(lambda No1,No2 :No1*No2, Number)

######################################################################
#   Function name : main
#   Description   : prints the product of the list    
#   Author        : Shubham Shankarlal Kumawat
#   Date          :19/01/2026
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

    Ret = Product(Value)

    print("Product is :",Ret)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 5,[1,2,3,4,5]       Output : Product is : 120 
#
##############################################################################