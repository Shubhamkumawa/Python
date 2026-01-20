######################################################################
#   Function name : MaxNum
#   Description   : return the maximum number 
#   Input         : Integer,Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
MaxNum = lambda No1,No2,No3 : No1 if(No1>No2 and No1>No3)else (No2 if No2>No3 else No3)

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

    print("Enter Third number : ")
    Value3 = int(input())

    Ret =MaxNum(Value1,Value2,Value3)

    print("Maximum number is :",Ret)
     
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 90,85,75       Output : Maximum number is : 90
#   Input : 155,175,125    Output : Maximum number is : 175
#   Input : 155,175,195    Output : Maximum number is : 195
#
##############################################################################