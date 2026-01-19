######################################################################
#   Function name : AreaReact
#   Description   : return area of reactangle   
#   Input         : Integer,Integer 
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def AreaReact(No1,No2):

    area = 0

    if No1<0 or No2<0:
        print("Please Enter the values greater than Zero")
        return
    
    area = No1 * No2
    return area

######################################################################
#   Function name : main
#   Description   : prints area of reactangle   
#   Input         : Integer,Integer 
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def main():
    length = 0
    breadth = 0
    Ret = 0

    print("Enter the length :")
    length = int(input())

    print("Enter the breadth :")
    breadth = int(input())

    Ret = AreaReact(length,breadth)

    print("Area of Rectangle :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

##############################################################################
#   
#   Input : 5,6      Output : Area of Rectangle : 30
#
#   Input : -5,-6    Output : Please Enter the values greater than Zero
#                             Area of Rectangle : None
#
##############################################################################