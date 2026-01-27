######################################################################
#   Function name : Add
#   Description   : return the addition of two number
#   Input         : Integer,Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def Add(No1,No2):
        
    Ans = 0
    Ans = No1 + No2
    return Ans
   
######################################################################
#   Function name : main
#   Description   : call of Add function 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():
    value1 = 0
    value2 = 0
    iRet = 0

    print("Enter first number :")
    value1 = int(input())

    print("Enter seconf number :")
    value2 = int(input())

    iRet = Add(value1,value2)
    
    print("Addition is :",iRet)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

############################################################
#
#   Input : 4,18       Output : Addition is : 22
#   Input : 5,55       Output : Addition is : 60
#
############################################################