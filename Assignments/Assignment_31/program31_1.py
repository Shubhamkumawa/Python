#######################################################################
#
#   importing os from the python library
#
######################################################################

import os

#######################################################################
#
# Function name : ListFilesByExtension
# Description   : Accepts directory name and file extension from user
#                 and displays all files with that extension
# Input         : Directory name ,extensions (String)
# Output        : Boolean
# Author        : Shubham Shankarlal Kumawat
# Date          : 21/02/2026
######################################################################

def ListFilesByExtension(dir_name, extension):

    
    found = False

    if not os.path.isdir(dir_name):
        print("Invalid directory name")
        return

    print(f"\nFiles with extension '{extension}' in '{dir_name}':\n")

    for file in os.listdir(dir_name):
        if file.endswith(extension):
            print(file)
            found = True

    if not found:
        print("No files found with given extension")

#######################################################################
#
# Function name : main
# Description   : call of ListFilesByExtension()
#
######################################################################

def main():
    dir_name = input("Enter directory name: ")
    extension = input("Enter file extension (e.g. .txt, .py): ")

    ListFilesByExtension(dir_name, extension)

#######################################################################
#
#   Call of main() function
#
######################################################################

if __name__ == "__main__":
    main()


######################################################################
#
#   Input  : Enter directory name: Demo
#            Enter file extension (e.g. .txt, .py): .txt
#
#   Output : Files with extension '.txt' in 'Demo':
#            Demo.txt
#
######################################################################