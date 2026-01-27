######################################################################
#
#   Importing threading from the python library
#
######################################################################

import threading

######################################################################
#
#   Function name : Sum_List
#   Description   : Prints the sum of the list
#   Input         : List[]
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def Sum_List(No):
    sum = 0
    for i in No:
        sum = sum + i
    print("Addition of list is :",sum)        

######################################################################
#
#   Function name : Product_List
#   Description   : Prints the product of the list
#   Input         : List[]
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def Product_List(No):
    Multi = 1
    for i in No:
        Multi = Multi*i
    print("Product of the list is :",Multi)

##################################################################################
#   Function name : main
#   Description   : Call of Sum_List and Product_List function using threading  
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
##################################################################################

def main():

    size = 0
    value = []

    print("Enter the size of the list :")
    size  = int(input())

    print("Enter",size,"elements :")
    for i in range(size):
        value.append(int(input()))
    
    t1 = threading.Thread(target=Sum_List,args=(value,))
    
    t2 = threading.Thread(target=Product_List,args=(value,))
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
#   Input : 5,[1,2,3,4,5]   Output : Addition of list is : 15
#                                    Product of the list is : 120
#
###########################################################################