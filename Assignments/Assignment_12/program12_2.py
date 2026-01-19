######################################################################
#   Function name : Factors
#   Description   : return factors of a number 
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def Factors(No):

    Fact = []
    for i in range(1,No+1):
        if No%i == 0:
            Fact.append(i)
    return Fact

######################################################################
#   Function name : main
#   Description   : prints Factors of a number   
#   Input         : Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def main():
    Value = 0 
    Ret = 0

    print("Enter a number :")
    Value = int(input())
    
    Ret = Factors(Value)
    print("Factors of",Value,"is :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

########################################################################
#   
#   Input : 12      Output : Factors of 12 is : [1, 2, 3, 4, 6, 12]
#
########################################################################