# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 10:01:21 2024

@author: bunya
/*
In this lab, you complete a prewritten Python program for a carpenter who creates personalized house signs. 
The program is supposed to compute the price of any sign a customer orders, based on the following facts:

The charge for all signs is a minimum of $35.00.
The first five letters or numbers are included in the minimum charge; there is a $4 charge for each additional character.
If the sign is make of oak, add $20.00. No charge is added for pine.
Black or white characters are included in the minimum charge; there is an additional $15 charge for gold-leaf lettering.
Instructions

Make sure the file HouseSign.py is selected and open.
You need to assign variables for the following:
A variable for the cost of the sign assigned to 0.00 (charge).
A variable for the number of characters assigned to 8 (num_chars).
A variable for the color of the characters assigned to "gold" (color).
A variable for the wood type assigned to "oak" (wood_type).
Write the rest of the program using assignment statements and if statements as appropriate. The output statements are written for you.
Execute the program by clicking the Run button at the bottom of the screen. Your output should be: The charge for this sign is $82."""

# HouseSign.py - This program calculates prices for custom house signs.

# Initialize variables with the given values
charge = 0.00
num_chars = 8
color = "gold"
wood_type = "oak"

# Base charge for all signs
charge += 35.00

# Calculate additional charges based on options

# Character charge
if num_chars > 5:
    charge += (num_chars - 5) * 4

# Color charge
if color.lower() == "gold":  # Case-insensitive comparison 
    charge += 15.00

# Wood type charge
if wood_type.lower() == "oak":  # Case-insensitive comparison
    charge += 20.00

# Output the final charge
print(f"The charge for this sign is ${charge:.2f}") 
