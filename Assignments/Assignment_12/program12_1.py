######################################################################
#   Function name : Vowel
#   Description   : return the character is vowel or not
#   Input         : Character
#   Output        : Boolean
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################

def Vowel(char):
    
    if char == 'a' or char =='e' or char == 'i' or char == 'o' or char == 'u':

        return True
    
    if char == 'A' or char =='E' or char == 'I' or char == 'O' or char == 'U':

        return True

    else:

        return False
    
######################################################################
#   Function name : main
#   Description   : print the character is vowel aor not 
#   Input         : Character
#   Output        : Character
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
   
def main():

    Value = ''
    Ret = 0
    print("Enter a Alphabate :")
    Value = input()
    Ret = Vowel(Value)

    if Ret == True:
        print(Value,"is Vowel")
    else:
        print(Value,"is Consonent")

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

########################################################################
#   
#   Input : a      Output : a is vowel
#   Input : A      Output : A is vowel
#   Input : d      Output : d is consonent
#
########################################################################