######################################################################
#   Function name : FactNum
#   Description   : returns the factorial of a number
#   Input         : Integer
#   Output        : Integer 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def FactNum(No):

    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i
    return Fact

######################################################################
#   Function name : main
#   Description   : prints the factorial of a number
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():

    value = 0
    iRet = 0

    print("Enter a number :")
    value = int(input())

    iRet = FactNum(value)

    print("Factorial of",value,"is :",iRet)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()


#############################################################
#   
#   Input : 5       Output : Factorial of 5 is : 120
#
#############################################################
