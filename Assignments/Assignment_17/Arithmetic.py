######################################################################
#   Function name : Add
#   Description   : returns addition of two number
#   Input         : Integer,Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def Add(No1,No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

######################################################################
#   Function name : Sub
#   Description   : returns subtraction of two number
#   Input         : Integer,Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def Sub(No1,No2):
    Ans = 0
    Ans = No1 - No2
    return Ans

######################################################################
#   Function name : multi
#   Description   : returns multiplication of two number
#   Input         : Integer,Integer
#   Output        : Integer
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def Multi(No1,No2):
    Ans = 0
    Ans = No1 * No2
    return Ans

######################################################################
#   Function name : Div
#   Description   : returns Division of two number
#   Input         : Integer,Integer
#   Output        : Float
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def Div(No1,No2):
    Ans = 0
    if No2 == 0:
        print("Division is not alloweded by Zero")
        return ZeroDivisionError
    Ans = No1 / No2
    return Ans

