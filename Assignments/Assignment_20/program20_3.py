######################################################################
#
#   Importing threading and time from the python library
#
######################################################################

import threading
import time

######################################################################
#
#   Function name : EvenList
#   Description   : Prints the Sum of Even number
#   Input         : List[]
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def EvenList(No):

    Sum = 0
    for i in No:
        if i%2 == 0:
            Sum = Sum+i
        time.sleep(0.5)
    print("Sum of even numbers :",Sum)

######################################################################
#
#   Function name : OddList
#   Description   : Prints the Sum of odd number
#   Input         : List[]
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def OddList(No):
    Sum = 0
    for i in No:
        if i%2!=0:
            Sum = Sum+i
        time.sleep(0.5)
    print("Sum of odd numbers :",Sum)

##############################################################################
#   Function name : main
#   Description   : Call of EvenList and OddList function using threading  
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
##############################################################################
 
def main():
    Size = 0
    Value = []

    print("Enter the Size of list :")
    Size = int(input())

    print("Enter the",Size,"elements :")
    for i in range(Size):
        Value.append(int(input()))    

    t1 = threading.Thread(target=EvenList,args=(Value, ))
    t2 = threading.Thread(target=OddList,args=(Value, ))
    t1.start()
    t2.start()
    t1.join() 
    t2.join()
    

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

#################################################################################
#
#   Input : 5,[1,2,3,4,5]      Output : Sum of Even numbers : 6 
#                                       Sum of Odd numbers : 9
#
#################################################################################