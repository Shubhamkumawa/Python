######################################################################
#   Function name : RevDisplay
#   Description   : return list from given number till 1   
#   Input         : Integer 
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def RevDisplay(No):
    Num = []

    for i in range(No,0,-1):
        Num.append(i)
    return Num

######################################################################
#   Function name : main
#   Description   : prints numbers in reverse order    
#   Input         : Integer 
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def main():
    value = 0
    Ret = 0

    print("Enter a number :")
    value = int(input())

    Ret = RevDisplay(value)

    print("Revrse order from given number is :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()


##############################################################################
#   
#   Input : 5      Output : Revrse order from given number is : [5,4,3,2,1]
#
##############################################################################