######################################################################
#   Function name : SumDigit
#   Description   : return the Sum of the digits
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def SumDigit(No):
    Sum = 0
    
    while No!=0:
       Digit = No % 10
       Sum = Sum + Digit
       No = No//10
       
    return Sum  

######################################################################
#   Function name : main
#   Description   : print the sum of the digits 
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def main():
    Value = 0
    Ret = 0

    print("Enter a number :")
    Value = int(input())

    Ret = SumDigit(Value)
    
    print("Sum of digits is :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

########################################################################
#   
#   Input : 1234       Output : Sum of digits is : 10
#
########################################################################