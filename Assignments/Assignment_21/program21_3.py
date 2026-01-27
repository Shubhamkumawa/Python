######################################################################
#
#   Importing threading from the python library
#
######################################################################

import threading

######################################################################
#
#   Counter : Global variable
#
######################################################################

Counter = 0

######################################################################
#    Creating a Lock object
######################################################################

lock = threading.Lock()

######################################################################
#
#   Function name : Increment
#   Description   : returns the count of the multiple  threads update 
#                   the shared variable 
#   Input         : Nothing
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
#
######################################################################

def Increment():

    global Counter

    for i in range(1000):
        lock.acquire()
        Counter  = Counter+1       # Lock the shared resources
        lock.release()             # Release the Lock


##################################################################################
#   Function name : main
#   Description   : prints the final value of counter  
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 25/01/2026
##################################################################################

def main():

    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Final value of counter :",Counter)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

###########################################################################
#
#  Output : Final value of counter : 2000
#
###########################################################################