######################################################################
#   Function name : FactNum
#   Description   : returns the addition of factors of a number
#   Input         : Integer
#   Output        : Integer 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def FactNum(No):

    sum = 0

    for i in range(1,No):
        if No % i == 0:

            sum = sum + i

    return sum

######################################################################
#   Function name : main
#   Description   : prints the addition of factors of a number
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():

    value = 0
    iRet = 0

    print("Enter a number :")
    value = int(input())

    iRet = FactNum(value)

    print("Addition of factors of",value,"is :",iRet)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()


##################################################################
#   
#   Input : 12       Output : Addition of factors of 12 is : 16 
#
##################################################################
