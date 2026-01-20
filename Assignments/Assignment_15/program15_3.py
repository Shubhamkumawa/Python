######################################################################
#   Function name : OddNum
#   Description   : return the list of odd numbers using filter() 
#   Input         : List[]
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 19/01/2026
#######################################################################
 
OddNum = lambda Number :list(filter(lambda No : No%2==1, Number))

######################################################################
#   Function name : main
#   Description   : prints the list of Odd numbers  
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

    Ret = OddNum(Value)

    print("List of Odd numbers :",Ret)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 5,[1,2,3,4,5]       Output : list of Odd numbers : [1,3,5] 
#
##############################################################################