######################################################################
#   Function name : MinNum
#   Description   : return the minimum number 
#   Input         : Integer,Integer
#   Output        : Boolean
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
MinNum = lambda No1,No2 : No1<No2

######################################################################
#   Function name : main
#   Description   : prints the minimum number  
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

    Ret =MinNum(Value1,Value2)

    if Ret == True:
        print("Minimum number is :",Value1)
    else:
        print("Minimum number is :",Value2)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 90,85       Output : Minimum number is : 85
#   Input : 125,155     Output : Minimum number is : 125
#
##############################################################################