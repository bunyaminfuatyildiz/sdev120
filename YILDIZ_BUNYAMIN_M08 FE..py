# Header Comments
# Name of the submission: Employee Salary Analysis
# Author of the submission: Bunyamin Fuat Yildiz
# Summary/goal of the submission: Store employee names/salaries in tuples, calculate the 
#                                 average salary, and find employees within a range 
#                                 of the average.
# Variables:
#   employees: List to store tuples of employee names and salaries              
#   average_salary: Calculated average salary (float)
#   sentinel: Sentinel value to end input (string)
#   threshold: Salary range from the average for filtering employees (default 5000)

def get_employee_data():
    """Collects input employee names and salaries from the user. """
    employees = []   # to store employee data
    sentinel = "done"  # Uses 'done' as a keyword to stop input.

    print("Enter employee names and salaries. Enter 'done' to finish.")

    while True: 
        name = input("Enter employee name (or 'done' to finish): ")
        if name.lower() == sentinel:  #  Checks if to stop by 'done'
            break

        while True: # Loop to get valid salary input.
            try: # Tries to convert the salary entered into a floating-point number by * 1000.
                salary_input = float(input("Enter salary: "))
                salary = salary_input * 1000  
                break
            except ValueError: # the user doesn't input a valid number.
                print("Invalid input. Please enter a valid salary.")

        employees.append((name, salary))   #  Adds the name and salary as a tuple to the employees list.

    return employees

def calculate_average_salary(employees):
    """Calculates the average salary of employees."""
    if not employees:   # Checks for an empty employee list.
        return 0

    # Concise calculation using a generator expression
    total_salary = sum(salary for _, salary in employees)  # Calculates and returns the average.
    return total_salary / len(employees) # Calculates and returns the average.

def display_employee_data(employees):
    """Displays all employee names and salaries with clear formatting."""
    print("\nEmployee Names and Salaries:")
    for name, salary in employees: #  Iterates over each employee tuple.
        print(f"{name}: ${salary:,.2f}") 

def display_within_range_employees(employees, average_salary, threshold=5000):
    """Displays employees within a specified range of the average salary."""
    print("\nEmployees within $5000 of the average:")
    for name, salary in employees:
        if abs(salary - average_salary) <= threshold: # Checks  the difference from the average salary is threshold.
            print(f"{name}: ${salary:,.2f}") # Displays the employee if they fall within the range

def main(): #  to organise the entire program
    """Coordinates input, calculations, and output."""
    employees = get_employee_data() # Calls the data collection function.
    #If data exists, calculates the average salary.

    if employees: 
        average_salary = calculate_average_salary(employees) 
        print(f"\nAverage Salary: ${average_salary:,.2f}") 
        display_employee_data(employees)
        display_within_range_employees(employees, average_salary) 
    else:
        print("\nNo employee data entered.") 
        
        
"""If this file is being run as the main script, then execute the main() function.
__name__ variable is set to the string "__main__"""
if __name__ == "__main__":
    main()
