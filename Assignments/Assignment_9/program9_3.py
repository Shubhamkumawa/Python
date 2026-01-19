#############################################################
#   Function name : Squarenum
#   Description   : return the square of the number 
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#############################################################

def Squarenum(No):

    sqa = 0
    sqa = No**2
    return sqa

#############################################################
#   Function name : main
#   Description   : call the Squarenum() function
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#############################################################

def main():

    value = 0
    Ret = 0

    print("Enter the number :")
    value = int(input())

    Ret = Squarenum(value)

    print("Square of",value,"is :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################


if __name__ == "__main__":
    main()

#############################################################
#   
#   Input : 11      Output : Square of 11 is : 121 
#   Input : 21      Output : Square of 11 is : 441
#
#############################################################
