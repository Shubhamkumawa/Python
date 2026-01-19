######################################################################
#   Function name : PerfectNum
#   Description   : return the number is perfect or not   
#   Input         : Integer 
#   Output        : Boolean
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def PerfectNum(No):
    Sum = 0
    for i in range(1,No):
        if No%i == 0:
            Sum = Sum + i
    if Sum == No:
        return True
    else:
        return False   
   
######################################################################
#   Function name : main
#   Description   : prints the number is perfect or not   
#   Input         : Integer 
#   Output        : Boolean
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def main():
    value = 0
    Ret = 0

    print("Enter the number :")
    value = int(input())

    Ret =  PerfectNum(value)

    if Ret == True:
        print(value,"is perfect number")

    else:
        print(value,"is not perfect number")
    

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

##############################################################################
#   
#   Input : 496     Output : 496 is perfect number
#   Input : 49      Output : 49 is not perfect number
#
##############################################################################