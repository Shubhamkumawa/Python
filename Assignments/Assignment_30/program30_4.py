######################################################################
#
#   Importing os and sys from the python library
#
######################################################################

import os
import sys
#################################################################################
#
#   Function name : CopyFile
#   Description   : Copying the content from one file to another file
#   Input         : String
#   Output        : String
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 02/02/2026
#
#################################################################################

def CopyFile(SrcFile , DestFile):

    if os.path.isfile(SrcFile):
        with open(SrcFile, "r") as src:
            data = src.read()

        with open(DestFile, "w") as dest:
            dest.write(data)

        print("File copied successfully.")
    else:
        print("Source file is not present in the current directory")

#################################################################################
#
#   Function name : main
#   Description   : call of CopyFile() function
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 02/02/2026
#
#################################################################################
    
def main():
    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        print("Usage : python program.py SourceFile DestinationFile")
        return

    CopyFile(sys.argv[1], sys.argv[2])

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

###########################################################################################
#
#   Command Line Input :
#   python program29.3py Demo.txt Hello.txt
#
#   Output :
#   File copied successfully
#
###########################################################################################
