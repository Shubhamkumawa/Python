#######################################################################################
#   Function name : StringLen
#   Description   : return the list of String length greater than 5 using filter() 
#   Input         : List[]
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 19/01/2026
#######################################################################################
 
StringLen = lambda String :list(filter(lambda Str : len(Str) > 5, String))

######################################################################
#   Function name : main
#   Description   : prints the list of String length greater than 5  
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
        Value.append(str(input()))

    Ret = StringLen(Value)

    print("String length greater than 5 are :",Ret)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

###################################################################################################################
#
#   Input : 5,[Marvellous,Shubham,Way,Say,Summatiom]   
#   
#   Output : String length greater than 5 are :  ['Marvellous', 'Shubham ', 'Summatiom'] 
#
####################################################################################################################