######################################################################
#   Function name : Table
#   Description   : return table of given number 
#   Input         : Integer
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def Table(No):

    result = []

    for i in range(1,11):

        result.append(No*i)

    return result

######################################################################
#   Function name : main
#   Description   : prints the table of the given number  
#   Input         : Integer
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def main():
    Value = 0 
    Ret = 0

    print("Enter a number :")
    Value = int(input())
    
    Ret = Table(Value)
    print("Table of",Value,"is :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

########################################################################
#   
#   Input : 5      Output : Table of 5 is :
#                           [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#
########################################################################