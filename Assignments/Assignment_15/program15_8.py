######################################################################
#   Function name : Division
#   Description   : return the list number divisible by both 3 and 5
#   Input         : List[]
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 19/01/2026
#######################################################################
 
Division = lambda Number :list(filter(lambda No : No if (No%3 == 0 and No%5 == 0) else False, Number))

######################################################################
#   Function name : main
#   Description   : prints the list number divisible by both 3 and 5  
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

    Ret = Division(Value)

    print("Numbers divisible by both 3 and 5 :",Ret)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

################################################################################################
#
#   Input : 5,[10,120,30,15,50]       Output : Number divisible by both 3 and 5 : [120,30,15] 
#
################################################################################################