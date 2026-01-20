######################################################################
#   Function name : ChkEven
#   Description   : return the even number or not 
#   Input         : Integer
#   Output        : Boolean
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
ChkEven = lambda No : (No % 2 == 0)

######################################################################
#   Function name : main
#   Description   : prints the even number or not 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
def main():
    Value = 0
    Ret = 0

    print("Enter a number : ")
    Value = int(input())

    Ret =ChkEven(Value)

    if Ret == True:
        print(Value,"is Even number")
    else:
        print(Value,"is not Even number")
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 90      Output : 90 is Even number
#   Input : 125     Output : 125 is not Even number
# 
##############################################################################