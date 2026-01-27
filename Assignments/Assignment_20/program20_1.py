######################################################################
#
#   Importing threading from the python library
#
######################################################################

import threading

######################################################################
#
#   Function name : Even
#   Description   : Prints the first 10 even numbers
#   Input         : Nothing
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def Even():
    even = []
    for i in range (1,11):
        even.append(i*2)
    print("First 10 Even numbers are :",even)

######################################################################
#
#   Function name : Odd
#   Description   : Prints the first 10 odd numbers
#   Input         : Nothing
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def Odd():
    odd = []
    for i in range(1,21):
        if i%2!=0:
            odd.append(i)
    print("First 10 Odd numbers are :",odd)

######################################################################
#   Function name : main
#   Description   : Call of Even and Odd function using threading  
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#######################################################################
 
def main():

    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)
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
#   Output : First 10 Even numbers are : [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#            First 10 Odd numbers are : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#
#################################################################################