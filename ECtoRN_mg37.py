# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:06:53 2024

@author: Inchara
"""

import requests

def get_kegg_reactions_by_ec(ec_number):
    # Base URL for KEGG API
    base_url = "http://rest.kegg.jp"
    
    # Format EC number for KEGG query
    ec_query = f"ec:{ec_number}"
    
    # Send request to KEGG to get reaction IDs associated with the EC number
    response = requests.get(f"{base_url}/link/reaction/{ec_query}")
    
    if response.status_code == 200:
        # Parse the response text
        data = response.text.strip().split('\n')
        if data[0]:  # Check if there is data returned
            reaction_links = [line.split('\t') for line in data]
            # Extract reaction IDs and return
            reactions = {r[1].replace('rn:', '') for r in reaction_links}
            if reactions:
                return reactions
        return None  # No reactions found
    else:
        # Handle errors by returning None
        return None

def main():
    # Open the input file containing EC numbers separated by commas
    with open("ECwc_mg37.txt", "r") as input_file:
        ec_numbers = input_file.read().split(',')
    
    # Dictionary to hold EC numbers and their corresponding reactions
    ec_reactions = {}
    
    # Process each EC number
    for ec_number in ec_numbers:
        ec_number = ec_number.strip()  # Remove any extra whitespace
        reactions = get_kegg_reactions_by_ec(ec_number)
        if reactions:
            ec_reactions[ec_number] = reactions
        else:
            ec_reactions[ec_number] = ["Error: No reactions found or API error occurred."]
    
    # Write the results to the output file
    with open("RN_mg37.txt", "w") as output_file:
        for ec_number, reactions in ec_reactions.items():
            # Join reactions by a comma and write to the output file
            output_file.write(f"{ec_number}: {', '.join(reactions)}\n")
    
    print("Output has been written to RN_mg37.txt")

if __name__ == "__main__":
    main()