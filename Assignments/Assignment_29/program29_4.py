######################################################################
#
#   Importing os and sys from the python library
#
######################################################################

import os
import sys
#################################################################################
#
#   Function name : CompareFile
#   Description   : Compare the contents of two files in the current directory
#   Input         : String
#   Output        : String
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 01/02/2026
#
#################################################################################

def CompareFile(SrcFile , DestFile):

    if os.path.isfile(SrcFile) and os.path.isfile(DestFile):
        with open(SrcFile, "r") as src:
            data1 = src.read()

        with open(DestFile, "r") as dest:
            data2 = dest.read()

            if data1 == data2:
                print("Both files are same")
            else:
                print("Both files are different")
    else:
        print("Source file is not present in the current directory")

#################################################################################
#
#   Function name : main
#   Description   : call of CompareFile() function
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 01/02/2026
#
#################################################################################
    
def main():
    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        print("Usage : python program.py SourceFile DestinationFile")
        return

    CompareFile(sys.argv[1], sys.argv[2])

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
#   python program29.4py Demo.txt Hello.txt
#
#   Output :
#   Both files are same
#   OR
#   Both files are different
#
###########################################################################################