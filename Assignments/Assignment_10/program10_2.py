######################################################################
#   Function name : SumNNatural
#   Description   : return sum of N natural number 
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def SumNNatural(No):

    Sum = 0
    while No!=0:
        Sum = Sum + No
        No = No-1
    return Sum

######################################################################
#   Function name : main
#   Description   : prints sum of N natural number   
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
    
    Ret = SumNNatural(Value)
    print("Sum of fist",Value,"natural number is :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

########################################################################
#   
#   Input : 5      Output : Sum of fist 5 natural number is : 15
#
########################################################################