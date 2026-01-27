######################################################################
#   Function name : Display
#   Description   : prints first 10 even numbers
#   Input         : Nothing
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def Display():

    for i in range(2,21,2):
        print(i ,end=" ")
           
######################################################################
#   Function name : main
#   Description   : call of Display function 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():
    Display()

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

############################################################
#
#  Output : 2 4 6 8 10 12 14 16 18 20
#
############################################################