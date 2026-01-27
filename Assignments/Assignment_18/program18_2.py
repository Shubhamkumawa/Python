######################################################################
#   Function name : MaxNum
#   Description   : return the maximum number from the list  
#   Input         : List[]
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def MaxNum(No):
    
    Max = 0
    for i in No:
        if i>Max:
            Max = i
    return Max

######################################################################
#   Function name : main
#   Description   : prints the maximum number from the list   
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################
 
def main():

    size = 0
    value = []
    iRet = 0

    print("Enter the size of list :")
    size = int(input())

    print("Enter",size,"elements :")
    
    for i in range(size):
        value.append(int(input()))
    
    iRet = MaxNum(value)
    print("Maximum number from List is :",iRet)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

##############################################################################
#
#   Input : 5,[1,2,3,4,5]       Output : Maximum number from List is : 5 
#
##############################################################################