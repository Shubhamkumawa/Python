######################################################################
#
#   importing os,sys,hashlib from the python library
#
######################################################################

import os
import sys
import hashlib

######################################################################
#
#   Function Name : DuplicateFile
#   Description   : Calculates MD5 checksum of file
#   Input         : File path
#   Output        : Checksum string
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 21/02/2026
#
######################################################################

def DuplicateFile(file_path):
    hash_object = hashlib.md5()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(1000)
            if not data:
                break
            hash_object.update(data)
    return hash_object.hexdigest()

######################################################################
#
#   Call of DuplicateFile() function
#
######################################################################

def main():
    if len(sys.argv) != 2:
        print("Usage : python duplicate.py <Directory_Name>")
        exit()

    dir_name = sys.argv[1]

    if not os.path.isdir(dir_name):
        print("Invalid directory name")
        exit()

    checksum_dict = {}
    duplicate_found = False
    log_file = "Log.txt"

    with open(log_file, "w") as log:
        log.write("Duplicate Files Log\n")

        for filename in os.listdir(dir_name):
            file_path = os.path.join(dir_name, filename)

            if os.path.isfile(file_path):
                checksum = DuplicateFile(file_path)

                if checksum in checksum_dict:
                    log.write(filename + "\n")
                    duplicate_found = True
                else:
                    checksum_dict[checksum] = filename

        if not duplicate_found:
            log.write("There is no duplicate file\n")

    print("Check Log.txt created in the current directory......")

######################################################################
#
#   Call of main() function
#
######################################################################

if __name__ == "__main__":
    main()

######################################################################
#
#   Input  : python program32_2.py Demo.txt
#
#   Output : Check Log.txt created in the current directory......
#            Inside Log.txt 
#            Duplicate Files Log
#            F.txt
#            G.txt
#
######################################################################