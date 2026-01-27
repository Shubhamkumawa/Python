######################################################################
#   Function name : PrimeNum
#   Description   : returns number is prime or not
#   Input         : Integer
#   Output        : Boolean
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def PrimeNum(No):
    if No <= 1:
        return False

    for i in range(2,No):
        if No % i == 0:
            return False
        
    return True
        

######################################################################
#   Function name : main
#   Description   : prints number is prime or not
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():

    value = 0
    iRet = 0

    print("Enter a number :")
    value = int(input())

    iRet = PrimeNum(value)

    if iRet == True:
        print("It is Prime Number")

    else:
        print("It is not Prime Number")

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()


##################################################################
#
#   Input : 5        Output : It is Prime Number   
#   Input : 12       Output : It is not Prime Number
#
##################################################################
