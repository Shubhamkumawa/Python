######################################################################
#   Function name : CountDigit
#   Description   : return the count of the digit in a number
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def CountDigit(No):
    count = 0
    while No!=0:
       
       No = No//10
       count = count + 1

    return count  

######################################################################
#   Function name : main
#   Description   : print the count of the digit in a number 
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

    Ret = CountDigit(Value)
    
    print("Number of digits is :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

########################################################################
#   
#   Input : 98754       Output : Number of digits is : 5
#
########################################################################