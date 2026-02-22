#######################################################################
#
#   importing os from the python library
#
######################################################################

import os

#######################################################################
#
# Function name : RenameFiles
# Description   : Accepts directory name and two file extensions from user
#                 and renames all files with first extension to second
# Input         : Directory name ,extensions (String)
# Output        : Boolean
# Author        : Shubham Shankarlal Kumawat
# Date          : 21/02/2026
######################################################################

def RenameFiles(dir_name, old_ext, new_ext):

    if not os.path.isdir(dir_name):
        print("Invalid directory name")
        return

    for file in os.listdir(dir_name):
        if file.endswith(old_ext):
            old_path = os.path.join(dir_name, file)
            new_file = file.replace(old_ext, new_ext)
            new_path = os.path.join(dir_name, new_file)

            os.rename(old_path, new_path)
            print(f"Renamed: {file} -> {new_file}")

#######################################################################
#
# Function name : main
# Description   : call of ListFilesByExtension()
#
######################################################################

def main():
    dir_name = input("Enter directory name: ")
    old_ext = input("Enter first file extension (e.g. .txt): ")
    new_ext = input("Enter second file extension (e.g. .doc): ")

    RenameFiles(dir_name, old_ext, new_ext)


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
#            Enter first file extension (e.g. .txt): .txt
#            Enter second file extension (e.g. .doc): .py
#   Output : Renamed: Demo.txt -> Demo.py
#
######################################################################