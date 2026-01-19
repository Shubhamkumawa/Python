######################################################################
#   Function name : Factorial
#   Description   : return factorial of a number 
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def Factorial(No):

    Fact = 1
    while No!=0:
        Fact = Fact * No
        No = No-1
    return Fact

######################################################################
#   Function name : main
#   Description   : prints Factorial of a number   
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
    
    Ret = Factorial(Value)
    print("Factorial of",Value,"is :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

########################################################################
#   
#   Input : 5      Output : Factorial of 5 is : 120
#
########################################################################