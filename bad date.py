"""Program Name: BadDate.py
Function: This program determines if a date entered by the user is valid.
Input: Interactive
Output: Valid date is printed or user is alerted that an invalid date was enteredbad date
.
""" 
# Declare variables
valid_date = True
min_year, min_month, max_month, min_day, max_day = 0, 1, 12, 1, 31

def housekeeping():
    """Prompts for and retrieves year, month, and day from the user."""
    global year, month, day
    year_str = input("Enter year: ")
    month_str = input("Enter month: ")
    day_str = input("Enter day: ")

    # Convert Strings to integers
    year = int(year_str)
    month = int(month_str)
    day = int(day_str)

def endOfJob():
    """Outputs whether the entered date is valid or invalid."""
    if valid_date:
        print(month, "/", day, "/", year, " is a valid date")
    else:
        print(month, "/", day, "/", year, " is an invalid date")

# Call the housekeeping function to start the program
housekeeping()

# This is the work of the detailLoop() method
# Check to be sure date is valid
if year <= min_year:  # invalid year
    valid_date = False
elif month < min_month or month > max_month:  # invalid month
    valid_date = False
elif day < min_day or day > max_day:  # invalid day
    valid_date = False

# Call the endOfJob function to print the final result
endOfJob()
