######################################################################
#   Function name : MaxNum
#   Description   : return the maximum number 
#   Input         : Integer,Integer
#   Output        : Boolean
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
MaxNum = lambda No1,No2 : No1>No2

######################################################################
#   Function name : main
#   Description   : prints the maximum number  
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter First number : ")
    Value1 = int(input())

    print("Enter Second number : ")
    Value2 = int(input())

    Ret =MaxNum(Value1,Value2)

    if Ret == True:
        print("Maximum number is :",Value1)
    else:
        print("Maximum number is :",Value2)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 90,85       Output : Maximum number is : 90
#   Input : 155,175     Output : Maximum number is : 175
#
##############################################################################