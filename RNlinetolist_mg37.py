# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:25:00 2024

@author: Inchara
"""

# Open the input file for reading
with open("RNline_mg37.txt", "r") as input_file:
    # Read all lines from the file
    lines = input_file.readlines()
    
    # Strip newline characters from each line and join them with a comma
    merged_line = ",".join(line.strip() for line in lines)

# Write the merged line to an output file
with open("RNwc_mg37.txt", "w") as output_file:
    output_file.write(merged_line)

print("Output has been written to RNwc_mg37.txt")