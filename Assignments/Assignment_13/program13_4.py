######################################################################
#   Function name : Binary
#   Description   : return the binary equivalent of the number  
#   Input         : Integer 
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def Binary(No):
    binary = ""

    if No == 0:
        return 0
    
    binary = bin(No)[2:]
    
    return binary

   
######################################################################
#   Function name : main
#   Description   : prints the binary equivalent of the number  
#   Input         : Integer 
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def main():
    value = 0
    Ret = 0

    print("Enter the number :")
    value = int(input())

    Ret =  Binary(value)

    print("Binary Equivalent :",Ret)
    
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

##############################################################################
#   
#   Input : 5     Output : Binary Equivalent : 101
#   Input : 100   Output : Binary Equivalent : 1100100
#
##############################################################################