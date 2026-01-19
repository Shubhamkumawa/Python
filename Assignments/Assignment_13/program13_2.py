######################################################################
#   Function name : AreaCirc
#   Description   : return area of circle   
#   Input         : Integer 
#   Output        : Float
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def AreaCirc(No):

    area = 0

    if No<0:
        print("Please Enter the radius greater than Zero")
        return
    
    area = 3.14*No**2
    return area

######################################################################
#   Function name : main
#   Description   : prints area of Circle   
#   Input         : Integer 
#   Output        : Float
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def main():
    Radius = 0
    Ret = 0

    print("Enter the Radius :")
    Radius = int(input())

    Ret = AreaCirc(Radius)

    print("Area of Circle :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

##############################################################################
#   
#   Input : 5     Output : Area of Circle : 78.5
#
#   Input : -5    Output : Please Enter the radius greater than Zero
#                             Area of Circle : None
#
##############################################################################