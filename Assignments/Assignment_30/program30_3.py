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
            for line in file:
                print(line,end='')

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
    CountLines(fname)

######################################################################
#
#   Call of main function
#
######################################################################

if __name__ == "__main__":
    main()

################################################################################
#
#   Input  : Enter file name: Demo.txt
#   Output : population = 80000                  # Population of town
#            demand_per_head = 200               # Litres per head per day
#            maximum_demand_factor = 1.50        # Maximum demand factor
#            filtration_rate = 5000              # Litres per hour per m^2
#            hours_per_day = 24                  # Hours in a day
#
################################################################################