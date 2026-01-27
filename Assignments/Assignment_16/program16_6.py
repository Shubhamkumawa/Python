######################################################################
#   Function name : ChkNum
#   Description   : Prints number is positve or negative or zero
#   Input         : Integer
#   Output        : String
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def ChkNum(No):

    if No > 0 :
        print("Positive Number")

    elif No < 0:
        print("Negative Number")

    else:
        print("Zero")

   
######################################################################
#   Function name : main
#   Description   : call of ChkNum function 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():
    value = 0
    print("Enter a number :")
    value = int(input())
    ChkNum(value)
    

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

############################################################
#
#   Input : 10       Output : Positive Number
#   Input : -10      Output : Negative Number
#   Input : 0        Output : Zero
#
############################################################