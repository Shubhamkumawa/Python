######################################################################
#   Function name : Prime
#   Description   : return the number is prime or not 
#   Input         : Integer
#   Output        : Boolean
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def Prime(No):
    
    for i in range(2,No):
        
        if No % i == 0:
        
            return False
    return True    

######################################################################
#   Function name : main
#   Description   : print the number is prime or not 
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

    Ret = Prime(Value)
    
    if Ret == True:
    
        print(Value,"is Prime number")
    
    else:
    
        print(Value,"is not Prime number")

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()


########################################################################
#   
#   Input : 11      Output : 11 is Prime number
#   Input : 12      Output : 12 not is Prime number
#
########################################################################