######################################################################
#   Function name : ChkNum
#   Description   : check weather number is even or odd 
#   Input         : Integer
#   Output        : Boolean
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def ChkNum(No):

    if (No % 2 == 0):
        return True
    else:
        return False
######################################################################
#   Function name : main
#   Description   : call of ChkNum function 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():
    value = 0
    iRet = False

    print("Enter a number :")
    value = int(input())

    iRet = ChkNum(value)
    if iRet == True:
        print("Even Number")
    else:
        print("Odd Number") 

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

############################################################
#
#   Input : 4       Output : Even Number
#   Input : 5       Output : Odd Number
#
############################################################