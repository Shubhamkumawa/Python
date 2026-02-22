#######################################################################
#
#   importing os ,sys and shutil from the python library
#
######################################################################

import os
import sys
import shutil

#######################################################################
#
# Script Name : main()
# Description : Accepts source directory, destination directory and
#               file extension, creates destination directory at
#               run time and copies all matching files
# Input         : Command line (String)
# Output        : Boolean
# Author        : Shubham Shankarlal Kumawat
# Date          : 21/02/2026
######################################################################


def main():
    
    if len(sys.argv) != 4:
        print("Usage: python CopyFilesByExtensionCmd.py <SourceDir> <DestDir> <Extension>")
        sys.exit(1)

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    extension = sys.argv[3]

    
    if not os.path.isdir(src_dir):
        print("Source directory does not exist")
        sys.exit(1)


    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
        print(f"Destination directory '{dest_dir}' created....")

    count = 0

    for file in os.listdir(src_dir):
        if file.endswith(extension):
            src_path = os.path.join(src_dir, file)

            if os.path.isfile(src_path):
                shutil.copy2(src_path, dest_dir)
                print(f"Copied: {file}")
                count += 1

    if count == 0:
        print("No files found with given extension")

                

#######################################################################
#
#   Call of main() function
#
######################################################################

if __name__ == "__main__":
    main()


######################################################################
#
#   Input  : python program31_3.py Demo Gun .pdf
#   Output : Destination directory 'Gun' created....
#            Copied: Demo.pdf
#
######################################################################