# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 10:01:21 2024

@author: bunya
"""

# HouseSign.py - This program calculates prices for custom house signs.

# Initialize variables here.
charge = 0.00
num_chars = 8
color = "gold"
wood_type = "oak"

# Charge for this sign.
charge += 35.00  # Minimum charge for all signs

# Number of characters.
if num_chars > 5:
    charge += (num_chars - 5) * 4

# Color of characters.
if color.lower() == "gold":
    charge += 15
# Type of wood.
if wood_type == "oak":
    charge += 20
# Write assignment and if statements here as appropriate.

# Output Charge for this sign.
print(f"The charge for this sign is ${charge:.2f}")