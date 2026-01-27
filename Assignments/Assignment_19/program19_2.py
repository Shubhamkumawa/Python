######################################################################
#   Function name : Product
#   Description   : return the multiplication of numbers 
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#######################################################################
 
Product = lambda No1,No2 : No1*No2

######################################################################
#   Function name : main
#   Description   : prints the multiplication of numbers
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#######################################################################
 
def main():

    value1 = 0
    value2 = 0
    iRet = 0

    print("Enter first number :")
    value1 = int(input())

    print("Enter second number :")
    value2 = int(input())

    iRet = Product(value1,value2)

    print("Multiplication is :",iRet)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

##############################################################################
#
#   Input : 9,8      Output : Multiplicayion is : 72
# 
##############################################################################