######################################################################
#   Function name : Square
#   Description   : return the square of the number 
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
Square = lambda NO : NO**2

######################################################################
#   Function name : main
#   Description   : prints the square of the number  
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
def main():
    Value = 0
    Ret = 0

    print("Enter a number : ")
    Value = int(input())

    Ret = Square(Value)

    print("Square of",Value,"is :",Ret)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 5       Output : Square of 5 is : 25
#
##############################################################################