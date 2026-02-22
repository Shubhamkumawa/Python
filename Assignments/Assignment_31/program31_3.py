#######################################################################
#
#   importing os , sys , shutil from the python library
#
######################################################################

import sys
import os
import shutil

#######################################################################
#
# Function Name : main
# Description   : Accepts source and destination directory names from
#                 command line, creates destination directory at runtime
#                 and copies all files
# Input         : Command line (String)
# Output        : Boolean
# Author        : Shubham Shankarlal Kumawat
# Date          : 21/02/2026
######################################################################


def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python CopyFilesUsingSys.py <SourceDir> <DestDir>")
        sys.exit(1)

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    # Check source directory
    if not os.path.isdir(src_dir):
        print("Source directory does not exist")
        sys.exit(1)

    # Create destination directory at runtime
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
        print(f"Destination directory '{dest_dir}' created")

    for file in os.listdir(src_dir):
        src_path = os.path.join(src_dir, file)

        if os.path.isfile(src_path):
            shutil.copy2(src_path, dest_dir)
            print(f"Copied: {file}")

#######################################################################
#
#   Call of main() function
#
######################################################################

if __name__ == "__main__":
    main()


######################################################################
#
#   Input  : python program31_3.py Demo Hello
#   Output : Destination directory 'Hello' created
#            Copied: Demo.pdf
#
######################################################################