######################################################################
#   Function name : Result
#   Description   : return the result of given marks 
#   Input         : List[]
#   Output        : Float.String
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def Result(Marks):
    
    Total = 0

    for i in Marks:
        Total = Total + i
    
    Per = (Total/500)*100

    if Per >= 75:
        Grade = "Distinction..."
    elif Per >= 60:
        Grade = "First Class..."
    elif Per >= 50:
        Grade = "Second Class..."
    else:
        Grade = "Fail..."
    return Per , Grade


   
######################################################################
#   Function name : main
#   Description   : prints the result of the student  
#   Input         : List[] 
#   Output        : Float, String
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 17/01/2026
#######################################################################
 
def main():
    Ret = 0
    Marks_list = []
    print("Enter the marks out of 100 only")

    print("Enter English marks :")
    value1 = float(input())

    print("Enter Physics marks :")
    value2 = float(input())

    print("Enter Chemistry marks :")
    value3 = float(input())

    print("Enter Mathematic marks :")
    value4 = float(input())

    print("Enter Information Technology marks :")
    value5 = float(input())

    Marks_list = [value1,value2,value3,value4,value5]

    Ret ,ret =  Result(Marks_list)
    
    print("Total Percentage obtained :",Ret)
    print("Grade obtained :",ret)
    
#############################################################
#   
#   Call of main() function
#
#############################################################

if __name__ == "__main__":
    main()

##############################################################################
#   
#   Input : [85,97,76,81,64]   Output : Total Percentage obtained : 80.60
#                                       Grade Obtained : Distinction... 
#
##############################################################################