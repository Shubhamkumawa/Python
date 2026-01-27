######################################################################
#   Function name : LengDigit
#   Description   : returns the sum of Digits of the number
#   Input         : Integer
#   Output        : Integer 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def LengDigit(No):
    
    Sum = 0
    
    while No!=0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No//10
    return Sum

######################################################################
#   Function name : main
#   Description   : prints the sum of Digits of a number
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():

    value = 0
    iRet = 0

    print("Enter a number :")
    value = int(input())

    iRet = LengDigit(value)

    print("Sum of Digits in the",value,"is :",iRet)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()


#######################################################################
#   
#   Input : 12345     Output : Sum of Digits in 12345 is : 15
#
#######################################################################
