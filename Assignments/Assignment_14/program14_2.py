######################################################################
#   Function name : Cube
#   Description   : return the cube of the number 
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
Cube = lambda NO : NO**3

######################################################################
#   Function name : main
#   Description   : prints the Cube of the number  
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 18/01/2026
#######################################################################
 
def main():
    Value = 0
    Ret = 0

    print("Enter a number : ")
    Value = int(input())

    Ret = Cube(Value)

    print("Cube of",Value,"is :",Ret)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 5       Output : Cube of 5 is : 125
#
##############################################################################