# Trainers/enrollees
# Bunyamin Fuat YILDIZ
# This application categorizes trainers based on new member enrollments, 
# Variables
trainers = []  # List to store the trainer last names 
enrollees = []  # List to store the number of new members enrolled by each trainer
#categ represents enrolled members in each of three categories respectively :   0-5 new members, 6-10 new members, 11 to 15 new members. 
categ_0_5 = 0
categ_6_10 = 0
categ_11_15 = 0

# Get input for 15 trainers 
for i in range(15):
    while True:
        try: #  for handling errors and exceptions that might occur 
            trainer_name = input("Enter trainer's last name: ")
            enrollees_nbr = int(input(f"Enter number of new enrollees for {trainer_name}: "))
            if 0 <= enrollees_nbr <= 15:  #Checks if the entered enrollees is within range (0 to 15).
                break
            else:
                print("Please enter a number between 0 and 15.") #  is executed if the entered number was not within the valid range.
        except ValueError: # except block will catch ValueError
            print("Invalid input. Please enter a number.") # inform the user of the invalid input format.

    trainers.append(trainer_name) # Appends the entered trainer_name
    enrollees.append(enrollees_nbr) # Appends the entered enrollees_nbr

# Categorize trainers and calculate sums.
categ_0_5 = sum(1 for n in enrollees if 0 <= n <= 5) 
categ_6_10 = sum(1 for n in enrollees if 6 <= n <= 10)
categ_11_15 = sum(1 for n in enrollees if 11 <= n <= 15)

# Display results
print("     Enrollment Results    ")
print("Trainers with 0-5 new enrollees:", categ_0_5)
print("Trainers with 6-10 new enrollees:", categ_6_10)
print("Trainers with 11-15 new enrollees:", categ_11_15)




