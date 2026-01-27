######################################################################
#   Function name : Display
#   Description   : returns length of Char
#   Input         : Nothing
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def Display(char):

    return len(char)
           
######################################################################
#   Function name : main
#   Description   : call of Display function 
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def main():
    Name = ''
    iRet = 0

    print("Enter a Name :")
    Name = str(input())

    iRet = Display(Name)

    print("Length of Name is :",iRet)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

################################################################
#
#  Input : Marvellous       Output : Length of Name is : 10
#
################################################################