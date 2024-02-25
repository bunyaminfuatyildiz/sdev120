# JumpinJive.py - This program looks up and prints the names and prices of coffee orders.
# Input:  Interactive.
# Output:  Name and price of coffee orders or error message if add-in is not found.
# Check if the user wants to quit

# Initialize variables.
NUM_ITEMS = 5

# Initialized list of add-ins.
addIns = ["Cream", "Cinnamon", "Chocolate", "Amaretto", "Whiskey"]

# Initialized list of add-in prices.
addInPrices = [.89, .25, .59, 1.50, 1.75]

# Initialize order total.
orderTotal = 2.00  # All orders start with a 2.00 charge

# Get user input.
addIn = input("Enter coffee add-in or XXX to quit: ")

# Check if the user wants to quit
while addIn != "XXX":
    # Check if the add-in is in the list
    if addIn in addIns:
        # Find the index of the add-in
        index = addIns.index(addIn)
        # Print the name and price of the add-in
        print(f"{addIns[index]} @ ${addInPrices[index]:.2f}")
        # Update the total price
        orderTotal += addInPrices[index]
    else:
        # Print error message if the add-in is not found
        print("Sorry, we do not carry that.")
    
    # Get the next user input
    addIn = input("Enter coffee add-in or XXX to quit: ")

# Print the final order total
print(f"Your total is ${orderTotal:.2f}")
