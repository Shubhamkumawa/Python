######################################################################
#
#   Importing reduce() from the python library
#
######################################################################

from functools import reduce

######################################################################
#
#   Function name : ChkNum
#   Description   : filter numbers between 70 and 90
#   Input         : List[]
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

ChkNum = lambda Numbers : list(filter(lambda No : No >= 70 and No <= 90, Numbers))


######################################################################
#
#   Function name : IncreNum
#   Description   : increase each number by 10
#   Input         : List[]
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

IncreNum = lambda Numbers : list(map(lambda No : No+10, Numbers))

######################################################################
#
#   Function name : Multiplication
#   Description   : return the product of the list 
#   Input         : List[]
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026 
#
#######################################################################
 
Multiplication = lambda Numbers : reduce(lambda No1,No2 : No1 * No2, Numbers)

######################################################################
#   Function name : main
#   Description   : prints the product of the list   
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
    
    filter_List = ChkNum(Value)
    print("List after filter :",filter_List)

    Map_List = IncreNum(filter_List)
    print("List after map :",Map_List)

    Reduced_list = Multiplication(Map_List)
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
#   Input : 5 , [78,98,88,70,95]    Output : List after filter : [78, 88, 70]
#                                            List after map : [88, 98, 80]
#                                            Output of reduce : 689920
#
##############################################################################