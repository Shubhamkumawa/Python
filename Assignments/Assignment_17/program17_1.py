#######################################################################
#   
#   Importing Arithmentic library 
#
#######################################################################

import Arithmetic

######################################################################
#   Function name : main
#   Description   : prints addition , Substraction , Multiplication,
#                   Division  
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():
    value1 = 0
    value2 = 0
    iRet = 0

    print("Enter first number :")
    value1 = int(input())

    print("Enter second number :")
    value2 = int(input())

    iRet = Arithmetic.Add(value1,value2)
    print("Addition is :",iRet)

    iRet = Arithmetic.Sub(value1,value2)
    print("Subtraction is :",iRet)

    iRet = Arithmetic.Multi(value1,value2)
    print("Multiplication is :",iRet)

    iRet = Arithmetic.Div(value1,value2)
    print("Division is :",iRet)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

################################################################################
#
#  Input : 55 , 40       Output : Addition is : 95
#                                 Substraction is : 15 
#                                 Multiplication is : 2200
#                                 Division is : 1.375
#
#  Input : 55 , 0        Output : Addition is : 55
#                                 Substraction is : 55 
#                                 Multiplication is : 0
#                                 Division is not alloweded by Zero
#                                 Division is : <class 'ZeroDivisionError'>
#                                
################################################################################