######################################################################
#
#   Importing threading from the python library
#
######################################################################

import threading

######################################################################
#
#   Function name : Even
#   Description   : Prints the Sum of Even factors
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def Even(No):
    Sum = 0
    for i in range (1,No+1):
        if No%i == 0 and i%2 == 0:
            Sum = Sum+i
    print("Sum of even Factors :",Sum)

######################################################################
#
#   Function name : Odd
#   Description   : Prints the Sum of odd factors
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def Odd(No):
    Sum = 0
    for i in range(1,No+1):
        if No %i==0 and i%2!=0:
            Sum = Sum+i
    print("Sum of odd Factors:",Sum)

######################################################################
#   Function name : main
#   Description   : Call of Even and Odd function using threading  
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#######################################################################
 
def main():
    Value = 0
    print("Enter a number :")
    Value = int(input())

    t1 = threading.Thread(target=Even,args=(Value, ))
    t2 = threading.Thread(target=Odd,args=(Value, ))
    t1.start()
    t2.start()
    t1.join() 
    t2.join()
    print("Exit from main")

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

#################################################################################
#
#   Input : 10      Output : Sum of Even factor : 12 
#                            Sum of Odd factor : 6
#                            Exit from main
#
#################################################################################