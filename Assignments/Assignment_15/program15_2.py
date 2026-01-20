######################################################################
#   Function name : EvenNum
#   Description   : return the list of even numbers using filter() 
#   Input         : List[]
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 19/01/2026
#######################################################################
 
EvenNum = lambda Number :list(filter(lambda No : No%2==0, Number))

######################################################################
#   Function name : main
#   Description   : prints the list of Even numbers  
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

    Ret = EvenNum(Value)

    print("List of Even numbers :",Ret)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 5,[1,2,3,4,5]       Output : list of Even numbers : [2,4] 
#
##############################################################################