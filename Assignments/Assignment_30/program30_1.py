######################################################################
# Function Name : CountLines
# Description   : Counts number of lines present in a file
#                 present in the current Directory
# Input         : File name (String)
# Output        : Integer
# Author        : Shubham Shankarlal Kumawat
# Date          : 02/02/2026
######################################################################

def CountLines(filename):
    try:
        with open(filename, 'r') as file:
            count = 0
            for line in file:
                count += 1
            return count

    except FileNotFoundError:
        print("Error: File not found.")
        return -1

    except Exception as e:
        print("Error:", e)
        return -1

######################################################################
# Function Name : Main
# Description   : Call of CountLines function
# Author        : Shubham Shankarlal Kumawat
# Date          : 02/02/2026
######################################################################

def main():
    fname = input("Enter file name: ")
    result = CountLines(fname)

    if result != -1:
        print("Number of lines in file:", result)

######################################################################
#
#   Call of main function
#
######################################################################

if __name__ == "__main__":
    main()

######################################################################
#
#   Input  : Enter file name: Demo.txt
#   Output : Number of lines in file: 5
#
######################################################################