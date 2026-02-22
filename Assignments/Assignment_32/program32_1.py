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
#   Function Name : CalculateChecksum
#   Description   : Calculates checksum of all files present in the 
#                   directory
#   Input         : File path
#   Output        : Checksum string
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 21/02/2026
#
######################################################################

def CalculateChecksum(file_path):
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
#   Call of CalculateChecksum() function
#
######################################################################
def main():
    if len(sys.argv) != 2:
        print("Usage : python checksum.py <Directory_Name>")
        exit()

    dir_name = sys.argv[1]

    if not os.path.isdir(dir_name):
        print("Invalid directory name")
        exit()

    print(f"\nChecksums of files in directory : {dir_name}\n")

    for filename in os.listdir(dir_name):
        file_path = os.path.join(dir_name, filename)

        if os.path.isfile(file_path):
            checksum = CalculateChecksum(file_path)
            print(f"{filename} : {checksum}")

######################################################################
#
#   Call of main() function
#
######################################################################

if __name__ == "__main__":
    main()
    
######################################################################
#
#   Input  : python program32_1.py Demo.txt
#
#   Output : Checksums of files in directory : Demo.txt
#
#            A.txt : d41d8cd98f00b204e9800998ecf8427e
#            B.txt : d41d8cd98f00b204e9800998ecf8427e
#            C.txt : d41d8cd98f00b204e9800998ecf8427e
#            D.txt : d41d8cd98f00b204e9800998ecf8427e
#            E.txt : d41d8cd98f00b204e9800998ecf8427e
#
######################################################################