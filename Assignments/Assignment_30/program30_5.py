######################################################################
#
#   Importing os and sys from the python library
#
######################################################################

import os
import sys
#################################################################################
#
#   Function name : FreqFile
#   Description   : prints the given name is present in that file 
#   Input         : String
#   Output        : String
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 02/02/2026
#
#################################################################################

def CompareFile(SrcFile,Word):
    count = 0
    if os.path.isfile(SrcFile):

        with open(SrcFile, "r") as file:
            data = file.read()
        words = data.split()
        for value in words:
            if value == Word:
                count = count + 1

        if count > 0:
            print("Word is present in the file")
        else:
            print("Word is not present in the file")

    else:
        print("File is not present in the current directory")


#################################################################################
#
#   Function name : main
#   Description   : call of CompareFile() function
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 02/02/2026
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
#   python program30_5.py Demo.txt Population
#
#   Output :
#   Word is present in the file
#
###########################################################################################