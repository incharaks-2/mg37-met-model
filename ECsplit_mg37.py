# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:00:43 2024

@author: Inchara
"""

import os # OS module of python that interacts with the operating system of the system

print('Get current working directory : ', os.getcwd()) # Gets current working directory

# Ensure that the file exists before trying to open it
if not os.path.exists("ECfinder_mg37.txt"):
    print("The file ECfinder_mg37.txt does not exist.")
else:
    # List to store extracted numbers
    extracted_numbers = []

    # Using 'with' to ensure the file is properly closed
    with open("ECfinder_mg37.txt", "r") as file_handler:  # Input the ECfinder.txt file
        print("File is open")

        for line in file_handler:
            # Strip whitespace and split by 'EC ' to get the number part
            if 'EC ' in line:
                ec_number = line.strip().split('EC ')[-1]
                # Add extracted number to the list (if any)
                if ec_number:
                    extracted_numbers.append(ec_number)

    # Write the extracted numbers to the output file
    with open("ECsplit.txt", "w") as output_file:  # Get output in .txt file
        for ec_number in extracted_numbers:
            output_file.write(ec_number + "\n")

    print("Job done")