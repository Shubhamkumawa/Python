######################################################################
#   Function name : OddNum
#   Description   : return the odd number till that numnber 
#   Input         : Integer
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def OddNum(No):

    Odd = []
    Num = 0
    for i in range(1,No+1,2):
       Odd.append(i)

    return Odd

######################################################################
#   Function name : main
#   Description   : prints oddnumber till that number    
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
    
    Ret = OddNum(Value)
    print("Odd numbers are :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

########################################################################
#   
#   Input : 10      Output : Odd numbers are : [1, 3, 5, 7, 9]
#
########################################################################