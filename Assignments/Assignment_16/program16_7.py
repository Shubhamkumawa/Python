######################################################################
#   Function name : ChkDiv
#   Description   : returns True if number is divisible by 5
#   Input         : Integer
#   Output        : Boolean
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def ChkDiv(No):

    if No % 5 == 0:
        return True
    else:
        return False

   
######################################################################
#   Function name : main
#   Description   : call of ChkDiv function 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():
    value = 0
    iRet = False

    print("Enter a number :")
    value = int(input())

    iRet = ChkDiv(value)

    print(iRet)    

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

############################################################
#
#   Input : 10       Output : True
#   Input : 24       Output : False
#
############################################################