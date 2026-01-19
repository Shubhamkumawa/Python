######################################################################
#   Function name : EvenNum
#   Description   : return the even number till that numnber 
#   Input         : Integer
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def EvenNum(No):

    Even = []
    Num = 0
    for i in range(2,No+1,2):
       Even.append(i)

    return Even

######################################################################
#   Function name : main
#   Description   : prints even number till that number    
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
    
    Ret = EvenNum(Value)
    print("Even numbers are :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

########################################################################
#   
#   Input : 10      Output : Even numbers are : [2, 4, 6, 8, 10]
#
########################################################################