######################################################################
#
#   Importing threading from the python library
#
######################################################################

import threading

######################################################################
#
#   Function name : Prime
#   Description   : Prints the prime number from the list
#   Input         : List[]
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def Prime(No):
    prime = list()

    for i in range(len(No)):
        if No[i]<2:
            continue
        bflag = True
        for j in range(2,No[i]):
            if No[i]%j == 0:
                bflag = False
        if bflag == True:
            prime.append(No[i])
    print("Prime Numbers are :",prime)

######################################################################
#
#   Function name : NonPrime
#   Description   : Prints the non prime number from the list
#   Input         : List[]
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def NonPrime(No):
    nonprime = list()

    for i in range(len(No)):
        if No[i]<2:
            continue
        bflag = True
        for j in range(2,No[i]):
            if No[i]%j == 0:
                bflag = False
        if bflag == False:
            nonprime.append(No[i])
    print("Non Prime Numbers are :",nonprime)

###########################################################################
#   Function name : main
#   Description   : Call of Prime and NonPrime function using threading  
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
###########################################################################

def main():

    size = 0
    value = []

    print("Enter the size of the list :")
    size  = int(input())

    print("Enter",size,"elements :")
    for i in range(size):
        value.append(int(input()))
    
    t1 = threading.Thread(target=Prime,args=(value,))
    
    t2 = threading.Thread(target=NonPrime,args=(value,))
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

#######################################################################
#
#   Input : 5,[2,4,3,7,6]   Output : Prime Numbers are : [2, 3, 7]
#                                    Non Prime Numbers are : [4, 6]
#
#######################################################################