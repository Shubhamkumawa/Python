##########################################################################################
#
#   Importing MarvellousNum User defined Module which checks numbers are prime or not 
#
##########################################################################################

import MarvellouNum

######################################################################
#   Function name : AddPrime
#   Description   : return the addition of prime number from the list 
#   Input         : List[]
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def AddPrime(SumList):

    Sum = 0
    Add = []
    Add = MarvellouNum.ChkPrime(SumList)

    for i in Add:
        Sum = Sum + i
    return Sum

######################################################################
#   Function name : main
#   Description   : return the addition of prime number from the list 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():

    size = 0
    value = []
    iRet = 0

    print("Enter the size of list :")
    size = int(input())

    print("Enter",size,"elments :")
    for i in range(size):
        value.append(int(input()))
    
    iRet = AddPrime(value)

    print("Addition of Prime Numbers are :",iRet)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()
    
##################################################################################
#
#   Input : 5,[1,3,5,7,15,14]       Output : Addition of Prime Numbers are : 15  
#
##################################################################################