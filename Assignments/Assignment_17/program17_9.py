######################################################################
#   Function name : LengDigit
#   Description   : returns the length of the number
#   Input         : Integer
#   Output        : Integer 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def LengDigit(No):
    
    Count = 0
    while No!=0:
        Count = Count+1
        No = No//10
    return Count

######################################################################
#   Function name : main
#   Description   : prints the number of Digits of a number
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():

    value = 0
    iRet = 0

    print("Enter a number :")
    value = int(input())

    iRet = LengDigit(value)

    print("Number of Digits in the",value,"is :",iRet)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()


#######################################################################
#   
#   Input : 12345     Output : Number of Digits in 12345 is : 5
#
#######################################################################
