######################################################################
#   Function name : Square
#   Description   : return the list of square using map() 
#   Input         : List[]
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 19/01/2026
#######################################################################
 
Square = lambda Number :list(map(lambda No : No**2 , Number))

######################################################################
#   Function name : main
#   Description   : prints the list of square of the number  
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 19/01/2026
#######################################################################
 
def main():
    Size = 0
    Value = []
    Ret = 0

    print("Enter the size of list")
    Size = int(input())
    
    print("Enter the",Size,"elements :")
    for i in range(Size):
        Value.append(int(input()))

    Ret = Square(Value)

    print("List of Squares :",Ret)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 5,[1,2,3,4,5]       Output : list of Square : [1,4,9,16,25] 
#
##############################################################################