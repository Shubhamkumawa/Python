######################################################################
#   Function name : Addition
#   Description   : return sum of two numbers 
#   Input         : Integer,Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def Addition(No1,No2):
    Ans = 0

    Ans = No1 + No2
    return Ans

######################################################################
#   Function name : Substraction
#   Description   : return difference of two numbers 
#   Input         : Integer,Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def Substraction(No1,No2):
    
    Ans = 0    
    Ans = No1 - No2
    return Ans  

######################################################################
#   Function name : Multiplication
#   Description   : return product of two numbers 
#   Input         : Integer,Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def Multiplication(No1,No2):
    Ans = 0    
    Ans = No1 * No2
    return Ans 

######################################################################
#   Function name : Division
#   Description   : return division of two numbers 
#   Input         : Integer,Integer
#   Output        : Float
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def Division(No1,No2):
    
    Ans = 0 
    try:
        Ans = No1 / No2
    except ZeroDivisionError as zobj:
        print("Inside Except :",zobj)
    
    return Ans 

######################################################################
#   Function name : main
#   Description   : prints Factors of a number   
#   Input         : Integer , Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def main():
    value1 = 0
    value2 = 0
    Ret = 0

    print("Enter First number :")
    value1 = int(input())

    print("Enter Second number :")
    value2 = int(input())

    Ret = Addition(value1,value2)
    print("Addition is :",Ret)

    Ret = Substraction(value1,value2)
    print("Substraction is :",Ret)

    Ret = Multiplication(value1,value2)
    print("Multiplication is :",Ret)

    Ret = Division(value1,value2)
    print("Division is :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

########################################################################
#   
#   Input : 12,4      Output : Addition is : 16
#                              Substraction is : 8
#                              Multiplication is : 48
#                              Division is : 3.0
#
#   Input : 12,0      Output : Addition is : 12
#                              Substraction is : 12
#                              Multiplication is : 0
#                              Inside Except : division by zero
#                              Division is : 0.0
########################################################################