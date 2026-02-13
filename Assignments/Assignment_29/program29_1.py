######################################################################
#
#   Importing os from the python library
#
######################################################################

import os

#################################################################################
#
#   Function name : CheckFile
#   Description   : returns the file exists or not in the current directory
#   Input         : String
#   Output        : Boolean
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 01/02/2026
#
#################################################################################

def CheckFile(Value):

    if os.path.isfile(Value):
        return True
    else:
        return False

#################################################################################
#
#   Function name : main
#   Description   : Prints the file exists or not the current directory
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 01/02/2026
#
#################################################################################
    
def main():

    Ret = False
    FileName = ""
    print("Enter the file name :")
    FileName = input()
    
    Ret = CheckFile(FileName)

    if Ret == True:
        print("File is present in the current directory")
    else:
        print("File is not present in the current directory")

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

###########################################################################################
#   
#   Input : program29_1.py      Output : File is present in the current directory
#
#   Input : program29_2.py      Output : File is not present in the current directory
#
###########################################################################################
