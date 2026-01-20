######################################################################
#   Function name : Multiplication
#   Description   : return the maultiplication of two number 
#   Input         : Integer , Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
Multiplication = lambda No1,No2 : (No1 * No2)

######################################################################
#   Function name : main
#   Description   : prints the Multiplication of two number 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter First number : ")
    Value1 = int(input())

    print("Enter Second number : ")
    Value2 = int(input())

    Ret =Multiplication(Value1,Value2)

    print("Multiplication is :",Ret)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 9,12      Output : Multiplication is : 108
# 
##############################################################################