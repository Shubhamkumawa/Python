######################################################################
#   Function name : Square
#   Description   : return the square of a number 
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#######################################################################
 
Square = lambda No : No**2

######################################################################
#   Function name : main
#   Description   : prints the square of a number
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#######################################################################
 
def main():

    value = 0
    iRet = 0

    print("Enter a number :")
    value = int(input())

    iRet = Square(value)

    print("Square is :",iRet)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

##############################################################################
#
#   Input : 90      Output : Square is : 8100
# 
##############################################################################