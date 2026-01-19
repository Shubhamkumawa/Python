#############################################################
#   Function name : ChkGreater
#   Description   : return the greater number 
#   Input         : Integer , Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#############################################################

def ChkGreater(No1,No2):
    if No1 > No2:
        return No1
    else:
        return No2

#############################################################
#   Function name : main
#   Description   : call the ChkGreater() function
#   Input         : Integer, Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#############################################################

def main():

    value1 = 0
    value2 = 0
    Ret = 0

    print("Enter First number :")
    value1 = int(input())

    print("Enter Second number :")
    value2 = int(input())
    
    Ret = ChkGreater(value1,value2)

    print(Ret,"is Greater number")

#############################################################
#   
#   Call of main() function
#
#############################################################


if __name__ == "__main__":
    main()

#############################################################
#   
#   Input : 11, 21      Output : 21 is Greater number
#   Input : 51, 21      Output : 51 is Greater number
#
#############################################################
