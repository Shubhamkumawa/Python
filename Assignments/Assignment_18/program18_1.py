######################################################################
#   Function name : AddList
#   Description   : return the sum of the list  
#   Input         : List[]
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def AddList(No):
    
    sum = 0
    for i in No:
        sum = sum + i
    return sum

######################################################################
#   Function name : main
#   Description   : prints the sum of the list   
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
    
    iRet = AddList(value)
    print("Addition of elements are:",iRet)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

##############################################################################
#
#   Input : 5,[1,2,3,4,5]       Output : Addition of elements are : 15 
#
##############################################################################