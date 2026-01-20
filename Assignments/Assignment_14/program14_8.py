######################################################################
#   Function name : Addition
#   Description   : return the addition of two number 
#   Input         : Integer , Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
Addition = lambda No1,No2 : (No1 + No2)

######################################################################
#   Function name : main
#   Description   : prints the addition of two number 
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

    Ret =Addition(Value1,Value2)

    print("Addition is :",Ret)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 90,120      Output : Addition is : 210
# 
##############################################################################