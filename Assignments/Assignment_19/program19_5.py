######################################################################
#
#   Importing reduce() from the python library
#
######################################################################

from functools import reduce

######################################################################
#
#   Function name : isPrime
#   Description   : filter numbers which are Prime numbers
#   Input         : List[]
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

isPrime = lambda Numbers : list(filter(lambda No :No>1 and all(No%i!=0 for i in range(2,No)), Numbers))


######################################################################
#
#   Function name : Square
#   Description   : return square of each number
#   Input         : List[]
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

Square = lambda Numbers : list(map(lambda No : No*2, Numbers))

######################################################################
#
#   Function name : Maximum
#   Description   : return the maximum number of the list 
#   Input         : List[]
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026 
#
#######################################################################
 
Addition = lambda Numbers : reduce(lambda No1,No2 : No1 if (No1>No2) else No2, Numbers)

######################################################################
#   Function name : main
#   Description   : prints the Addition of the list   
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#######################################################################
 
def main():
    Size = 0
    Value = []
    Filter_List  = []
    Map_List = []
    Reduced_list = 0

    print("Enter the size of list")
    Size = int(input())
    
    print("Enter the",Size,"elements :")
    for i in range(Size):
        Value.append(int(input()))
    
    filter_List = isPrime(Value)
    print("List after filter :",filter_List)

    Map_List = Square(filter_List)
    print("List after map :",Map_List)

    Reduced_list = Addition(Map_List)
    print("Output of reduce :",Reduced_list)
  
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
   main()

##############################################################################
#
#   Input : 6 , [2,1,5,4,8,12]    Output : List after filter : [2,5]
#                                          List after map : [4,10]
#                                          Output of reduce : 10
#
##############################################################################