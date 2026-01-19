#############################################################
#   Function name : Cubenum
#   Description   : return the Cube of the number 
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#############################################################

def Cubenum(No):

    cub = 0
    cub = No**3
    return cub

#############################################################
#   Function name : main
#   Description   : call the Cubenum() function
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

    Ret = Cubenum(value)

    print("Cube of",value,"is :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################


if __name__ == "__main__":
    main()

#############################################################
#   
#   Input : 11      Output : Cube of 10 is : 1000
#   Input : 21      Output : Cube of 21 is : 9261
#
#############################################################
