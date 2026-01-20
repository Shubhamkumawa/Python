######################################################################
#   Function name : ChkOdd
#   Description   : return the Odd number or not 
#   Input         : Integer
#   Output        : Boolean
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
ChkOdd = lambda No : (No % 2 == 1)

######################################################################
#   Function name : main
#   Description   : prints the Odd number or not
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
def main():
    Value = 0
    Ret = 0

    print("Enter a number : ")
    Value = int(input())

    Ret =ChkOdd(Value)

    if Ret == True:
        print(Value,"is Odd number")
    else:
        print(Value,"is not Odd number")
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 90      Output : 90 is not Odd number
#   Input : 125     Output : 125 is Odd number
# 
##############################################################################