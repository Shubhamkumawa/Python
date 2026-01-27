######################################################################
#   Function name : Display
#   Description   : prints marvellous on console
#   Input         : Integer
#   Output        : String
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def Display(No):
        
    for i in range(No):
        print("Marvellous")
   
######################################################################
#   Function name : main
#   Description   : call of Display function 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():
    value = 0
    print("Enter a number :")
    value = int(input())
    Display(value)
    

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

############################################################
#
#   Input : 5       Output : Marvellous
#                            Marvellous
#                            Marvellous
#                            Marvellous
#                            Marvellous
#
############################################################