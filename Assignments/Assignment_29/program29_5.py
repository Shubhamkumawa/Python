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
#   Description   : prints the frequency of the given name in that file 
#   Input         : String
#   Output        : String
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 01/02/2026
#
#################################################################################

def FreqFile(SrcFile,Word):
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
            print("Frequency of", Word, "is :", count)
        else:
            print("Word is not present in the file")
            print("Frequency is : 0")

    else:
        print("File is not present in the current directory")


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

    FreqFile(sys.argv[1], sys.argv[2])

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
#   python program29_5.py Demo.txt Ganesh
#
#   Output :
#   Word is present in the file
#   Frequency of Ganesh is : 1
#
###########################################################################################