# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 19:25:06 2024

@author: cansa
"""
import sys

gifts = [
    "Book", "Toy", "Gadget", "Video Game", "Headphones", "Smartphone",
    "Laptop", "Watch", "Shoes", "Wallet", "Headset", "Camera", "Drone",
    "Smart Watch", "Bluetooth Speaker"
]

# Get indices from command-line arguments
if len(sys.argv) != 2:
    print("Error: Please provide gift indices.")
    sys.exit(1)

# Parse the indices from the argument
gift_indices = [int(index) for index in sys.argv[1].split(',')]

# Select the gifts based on the indices
selected_gifts = [gifts[index] for index in gift_indices]

# Calculate the unique gift code using bitwise OR
gift_code = 0
for index in gift_indices:
    gift_code |= (1 << index)  # Bitwise OR to calculate unique code

# Output the results
print("Selected Gifts:", ", ".join(selected_gifts))
print("Unique Gift Code:", gift_code)


