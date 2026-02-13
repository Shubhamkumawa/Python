######################################################################
#
#   Importing os from the python library
#
######################################################################

import os

#################################################################################
#
#   Function name : CheckFile
#   Description   : prints the file contents on the console 
#                   present in the current directory
#   Input         : String
#   Output        : String
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 01/02/2026
#
#################################################################################

def CheckFile(Value):

    if os.path.isfile(Value):
        with open(Value, "r") as file:
            print("\nFile contents:\n")
            print(file.read())
    else:
        print("File is not present in the current directory")

#################################################################################
#
#   Function name : main
#   Description   : call of CheckFile() function
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 01/02/2026
#
#################################################################################
    
def main():

    Ret = False
    FileName = ""
    print("Enter the file name :")
    FileName = input()
    
    CheckFile(FileName)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

###########################################################################################
#   
#   Input : Demo.txt            Output : File contents:
#
#                                        Jay Ganesh.......
#
#   Input : program29_3.py      Output : File is not present in the current directory
#
###########################################################################################
