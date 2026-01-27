######################################################################
#
#   Importing threading from the python library
#
######################################################################

import threading

######################################################################
#
#   Function name : Maximum
#   Description   : Prints the maximum number from the list
#   Input         : List[]
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def Maximum(No):
    Max = []
    Max = No[0]
    for i in range(1,len(No)):
        if No[i]>Max:
            Max = No[i]
    print("Maximum number from the list :",Max)
        

######################################################################
#
#   Function name : Minimum
#   Description   : Prints the minimum number from the list
#   Input         : List[]
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def Minimum(No):
    Min = []
    Min = No[0]
    for i in range(1,len(No)):
        if No[i]<Min:
            Min = No[i]
    print("Minimum number from the list :",Min)

###########################################################################
#   Function name : main
#   Description   : Call of Maximum and Minimum function using threading  
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
    
    t1 = threading.Thread(target=Maximum,args=(value,))
    
    t2 = threading.Thread(target=Minimum,args=(value,))
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

###########################################################################
#
#   Input : 5,[1,2,3,4,5]   Output : Maximum number from the list : 5
#                                    Minimum number from the list : 1
#
###########################################################################