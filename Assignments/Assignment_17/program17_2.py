######################################################################
#   Function name : Pattern
#   Description   : prints pattern of " * " on console
#   Input         : Integer
#   Output        : Nothing 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def Pattern(No):

    for i in range(No):
       
        print("*\t"*No)

######################################################################
#   Function name : main
#   Description   : call of Pattern function
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():

    value = 0

    print("Enter a number :")
    value = int(input())

    Pattern(value)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

################################################################################
#
#  Input : 5        Output : *       *       *       *       *
#                            *       *       *       *       *
#                            *       *       *       *       *
#                            *       *       *       *       *
#                            *       *       *       *       *
#                              
################################################################################