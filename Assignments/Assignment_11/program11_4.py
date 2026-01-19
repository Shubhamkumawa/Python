######################################################################
#   Function name : ReverseDigit
#   Description   : return the reverse of the digits
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def ReverseDigit(No):
    Rev = 0
    
    while No!=0:
       Digit = No % 10
       Rev = (Rev*10) + Digit
       No = No//10
       
    return Rev 

######################################################################
#   Function name : main
#   Description   : print the reverse of the digits 
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

    Ret = ReverseDigit(Value)
    
    print("Reverse of digit is :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

########################################################################
#   
#   Input : 1234       Output : Reverse of digits is : 4321
#
########################################################################