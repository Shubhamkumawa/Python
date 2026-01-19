######################################################################
#   Function name : PalindroneDigit
#   Description   : return the digit is palindrone or not
#   Input         : Integer
#   Output        : Boolean
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def PalindroneDigit(No):

    Temp = No
    Rev = 0
    
    while No!=0:
       Digit = No % 10
       Rev = (Rev*10) + Digit
       No = No//10
       
    if Rev == Temp:
        return True
    else:
        return False
     

######################################################################
#   Function name : main
#   Description   : print the digit is palindrone or not 
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

    Ret = PalindroneDigit(Value)
    
    if Ret == True:

        print(Value,"is Palindrone number")

    else:
        print(Value,"is not Palindrone number")

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

########################################################################
#   
#   Input : 121       Output : 121 is Palindrone number
#   Input : 123       Output : 123 is not Palindrone number
#
########################################################################