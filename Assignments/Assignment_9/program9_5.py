######################################################################
#   Function name : ChkDivision
#   Description   : return number is divisible by 3 and 5 or not 
#   Input         : Integer
#   Output        : Boolean
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def ChkDivision(No):
    
    if No%3 == 0 and No%5 == 0:

        return True
    
    else:

        return False

   

#############################################################
#   Function name : main
#   Description   : call the ChkDivision() function
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

    Ret = ChkDivision(value)

    if Ret == True:
        
        print(value,"is Divisible by 3 and 5")
    
    else:

        print(value,"is not Divisible by 3 and 5")

#############################################################
#   
#   Call of main() function
#
#############################################################


if __name__ == "__main__":
    main()

#############################################################
#   
#   Input : 15      Output : 15 is Divisible by 3 and 5
#   Input : 21      Output : 21 is not Divisible by 3 and 5
#
#############################################################
