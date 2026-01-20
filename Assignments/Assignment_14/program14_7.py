######################################################################
#   Function name : ChkDivision
#   Description   : return the number is divisible by 5 or not 
#   Input         : Integer
#   Output        : Boolean
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
ChkDivision = lambda No : (No % 5 == 0)

######################################################################
#   Function name : main
#   Description   : prints the number is divisible by 5 or not 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
def main():
    Value = 0
    Ret = 0

    print("Enter a number : ")
    Value = int(input())

    Ret =ChkDivision(Value)

    if Ret == True:
        print(Value,"is Divisible by 5")
    else:
        print(Value,"is not Divisible by 5")
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 90      Output : 90 is Divisible by 5
#   Input : 16      Output : 16 is not Divisible by 5
# 
##############################################################################