######################################################################
#
#   Importing threading and time from the python library
#
######################################################################

import threading
import time

######################################################################
#
#   Function name : Small
#   Description   : Prints the number of lowercase characters
#   Input         : String
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def Small(text):

    thread = threading.current_thread()
    count = 0
    for ch in text:
        if ch.islower():
            count = count +1
        time.sleep(0.1)
    print(f"[{thread.name} | ID: {thread.ident}] Lowercase characters count: {count}")


######################################################################
#
#   Function name : Capital
#   Description   : Prints the number of Uppercase characters
#   Input         : String
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def Capital(text):
    thread = threading.current_thread()
    count = 0
    for ch in text:
        if ch.isupper():
            count = count +1
        time.sleep(0.1)
    print(f"[{thread.name} | ID: {thread.ident}] Uppercase characters count: {count}")

######################################################################
#
#   Function name : Digits
#   Description   : Prints the number of numeric digits
#   Input         : String
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def Digits(text):
    thread = threading.current_thread()
    count = 0
    for ch in text:
        if ch.isdigit():
            count = count + 1
        time.sleep(0.1)    
    print(f"[{thread.name} | ID: {thread.ident}] Numeric digits count: {count}")

#################################################################################
#   Function name : main
#   Description   : Call of Small , Capital , Digits function using threading  
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#################################################################################
 
def main():
    Value = ''

    print("Enter the string :")
    Value = input()    

    t1 = threading.Thread(target=Small,args=(Value, ))
    t2 = threading.Thread(target=Capital,args=(Value, ))
    t3 = threading.Thread(target=Digits,args=(Value, ))

    t1.start()
    t2.start()
    t3.start()

    t1.join() 
    t2.join()
    t3.join()
    

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

####################################################################################################
#
# Input : Hello World 123  Output : [Thread-3 (Digits) | ID: 24148] Numeric digits count: 3
#                                   [Thread-2 (Capital) | ID: 18332] Uppercase characters count: 2
#                                   [Thread-1 (Small) | ID: 8756] Lowercase characters count: 8
#
####################################################################################################