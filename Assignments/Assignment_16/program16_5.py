######################################################################
#   Function name : RevNum
#   Description   : print reverse number on console
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def RevNum(No):

    for i in range(No,0,-1):
        print(i)
   
######################################################################
#   Function name : main
#   Description   : call of RevNum function 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():
    value = 0
    print("Enter a number :")
    value = int(input())
    RevNum(value)
    

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

############################################################
#
#   Input : 10       Output : 10 9 8 7 6 5 4 3 2 1
#
############################################################