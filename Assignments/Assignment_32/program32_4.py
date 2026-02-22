######################################################################
#
#   importing os,sys,hashlib,time from the python library
#
######################################################################

import os
import sys
import hashlib
import time

######################################################################
#
#   Function Name : DeleteDuplicateFile
#   Description   : Calculates MD5 checksum of file
#   Input         : File path
#   Output        : Checksum string
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 21/02/2026
#
######################################################################

def DeleteDuplicateFile(file_path):
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
#   Call of DeleteDuplicateFile() Function
#
######################################################################

def main():

    start_time = time.time()
    if len(sys.argv) != 2:
        print("Usage : python duplicate.py <Directory_Name>")
        exit()

    dir_name = sys.argv[1]

    if not os.path.isdir(dir_name):
        print("Invalid directory name")
        exit()

    checksum_dict = {}
    deleted_files = []
    log_file = "Duplicate.txt"

    for filename in os.listdir(dir_name):
        file_path = os.path.join(dir_name, filename)

        if os.path.isfile(file_path):
            checksum = DeleteDuplicateFile(file_path)

            if checksum in checksum_dict:
                os.remove(file_path)          # Delete duplicate file
                deleted_files.append(filename)
            else:
                checksum_dict[checksum] = filename

    with open(log_file, "w") as log:
        log.write("Deleted Duplicate Files Log\n")

        if deleted_files:
            for file in deleted_files:
                log.write(file + "\n")
        else:
            log.write("There is no duplicate file\n")

    end_time = time.time()     
    execution_time = end_time - start_time

    print("Check Duplicate.txt created in the current directory......")
    print(f"Execution Time : {execution_time:.4f} seconds")

######################################################################
#
#   Call of main() function
#
######################################################################

if __name__ == "__main__":
    main()

######################################################################
#
#   Input  : python program32_3.py Demo.txt
#
#   Output : Check Duplicate.txt created in the current directory......
#            Execution Time : 0.0033 seconds
#            Inside Duplicate.txt 
#            Deleted Duplicate Files Log
#            F.txt
#            G.txt
#
######################################################################