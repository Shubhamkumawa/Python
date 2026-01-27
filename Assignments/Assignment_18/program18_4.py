######################################################################
#   Function name : FreqNum
#   Description   : return the frequency of number from the list  
#   Input         : List[]
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def FreqNum(No1,No2):
    
    Freq = 0
    for i in No1:
        if i == No2:
            Freq = Freq + 1
    return Freq
        

######################################################################
#   Function name : main
#   Description   : prints the frequency of number from the list   
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################
 
def main():

    size = 0
    value = []
    Num = 0
    iRet = 0

    print("Enter the size of list :")
    size = int(input())

    print("Enter",size,"elements :")
    
    for i in range(size):
        value.append(int(input()))
    
    print("Enter number to be searched from list :")
    Num = int(input())

    iRet = FreqNum(value,Num)
    print("Frequency of",Num,"from List is :",iRet)
   
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

##############################################################################
#
#   Input : 5,[1,5,3,5,5]       Output : Frequency of 5 from List is : 3 
#
##############################################################################