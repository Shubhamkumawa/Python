######################################################################
#   Function name : Display
#   Description   : return numbers staring from 1 till given number   
#   Input         : Integer 
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def Display(No):
    Num = []

    for i in range(1,No+1):
        Num.append(i)
    return Num

######################################################################
#   Function name : main
#   Description   : prints numbers staring from 1 till given number   
#   Input         : Integer 
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def main():
    value = 0
    Ret = 0

    print("Enter a number :")
    value = int(input())

    Ret = Display(value)

    print("Numbers are :",Ret)

#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()


########################################################################
#   
#   Input : 5      Output : Number are : [1, 2, 3, 4, 5]
#
########################################################################