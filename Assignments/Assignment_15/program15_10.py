######################################################################
#   Function name : CountEven
#   Description   : return the count of even numbers using filter() 
#   Input         : List[]
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 19/01/2026
#######################################################################
 
CountEven = lambda Number : len(list(filter(lambda No : No%2==0, Number)))

######################################################################
#   Function name : main
#   Description   : prints the Count of Even numbers  
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

    Ret = CountEven(Value)

    print("Count of Even numbers :",Ret)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 5,[1,2,3,4,5]       Output : Count of Even numbers : 2 
#
##############################################################################