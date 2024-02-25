# SUMMARY
# In this lab, you complete a partially prewritten Python program that uses a list.

# The program prompts the user to interactively enter eight batting averages, which the pgoram
# stores in an array. It should then find the minimum and maximum batting averages stored in the
# array, as well as the average of the eight batting averages. The data file provided for this
# lab includes the input statement and some variable declarations. Comments are included to help
# you write the remainder of the program.

# INSTRUCTIONS
# 1. Make sure the file BattleAverage.py is selected and open.
# 2. Write the Python statements as indicated by the comments.
# 3. Execute the program by clicking the Run button at the bottom of the screen. Enter the following
# batting averages: .299, .157, .242, .203, .198, .333, .270, .190. The minimum batting average
# should be .157 and the maximum batting average should be .333. The average should be .2365.

# Declare a named constant for array size here.
MAX_AVERAGES = 8

# Declare array here.
averages = []
# Write a loop to get batting averages from user and assign to array.
for i in range(MAX_AVERAGES):
    averageString = input("Enter a batting average: ")
    battingAverage = float(averageString)
    # Assign value to array.
    averages.append(battingAverage)
# Assign the first element in the array to be the minimum and the maximum.
minAverage = averages[0]
maxAverage = averages[0]
# Start out your total with the value of the first element in the array.
total = 0
# Write a loop here to access array values starting with averages[1]
for i in range(MAX_AVERAGES):
    # Within the loop for the minimum and maximum batting averages.
    if averages[i] < minAverage:
        minAverage = averages[i]

    if averages [i] > maxAverage:
        maxAverage = averages[i]
    
    total = total + averages[i]
    # Also accumulate a total of all batting averages.

# Caluculate the average of the 8 batting averages.
average = total / MAX_AVERAGES

# Print the batting averages stored in the averages array.
print(averages)

# Print the maximum batting average, minimum batting average, and average batting average.
print("Minimum batting average is ", minAverage)
print("Maximum batting average is ", maxAverage)
print("Average batting average is ", average)