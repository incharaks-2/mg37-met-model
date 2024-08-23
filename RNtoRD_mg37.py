# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:55:24 2024

@author: Inchara
"""

import os
import requests

def fetch_reaction_details(reaction_ids):
    base_url = "http://rest.kegg.jp/get/"
    reaction_details = {}

    for reaction_id in reaction_ids:
        try:
            # Make a request to KEGG API
            response = requests.get(base_url + reaction_id)
            response.raise_for_status()  # Check for HTTP errors
            reaction_data = response.text
            
            # Parse the response
            details = {}
            lines = reaction_data.split('\n')
            
            for line in lines:
                if line.startswith('ENTRY'):
                    details['ENTRY'] = line.split(None, 1)[1].strip()
                elif line.startswith('NAME'):
                    details['NAME'] = line.split(None, 1)[1].strip()
                elif line.startswith('EQUATION'):
                    details['EQUATION'] = line.split(None, 1)[1].strip()
                elif line.startswith('DEFINITION'):
                    details['DEFINITION'] = line.split(None, 1)[1].strip()
                elif line.startswith('PATHWAY'):
                    details['PATHWAY'] = line.split(None, 1)[1].strip()
                elif line.startswith('MODULE'):
                    details['MODULE'] = line.split(None, 1)[1].strip()
                elif line.startswith('SUBSTRATE'):
                    details['SUBSTRATE'] = line.split(None, 1)[1].strip()
                elif line.startswith('PRODUCT'):
                    details['PRODUCT'] = line.split(None, 1)[1].strip()
                elif line.startswith('COFACTOR'):
                    details['COFACTOR'] = line.split(None, 1)[1].strip()
                elif line.startswith('ENZYME'):
                    details['ENZYME'] = line.split(None, 1)[1].strip()
                elif line.startswith('REFERENCE'):
                    details['REFERENCE'] = line.split(None, 1)[1].strip()

            # If no details were parsed, consider it an error
            if not details:
                raise ValueError("No reaction data found.")
            
            reaction_details[reaction_id] = details
        
        except requests.RequestException as e:
            reaction_details[reaction_id] = {"error": f"Request error: {str(e)}"}
        except ValueError as e:
            reaction_details[reaction_id] = {"error": str(e)}
    
    return reaction_details

def main():
    # Get the current working directory
    print('Get current working directory:', os.getcwd())

    # Read the input file containing reaction IDs separated by commas
    with open("RNwc_mg37.txt", "r") as input_file:
        reaction_ids = input_file.read().strip().split(',')
        reaction_ids = [rid.strip() for rid in reaction_ids]  # Remove any extra whitespace
    
    # Fetch reaction details for the given IDs
    reaction_data = fetch_reaction_details(reaction_ids)
    
    # Write the results to the output file
    with open("Reaction_Details_mg37.txt", "w") as output_file:
        for reaction_id, details in reaction_data.items():
            output_file.write(f"Details for Reaction ID: {reaction_id}\n")
            if "error" in details:
                output_file.write(f"Error: {details['error']}\n")
            else:
                for key, value in details.items():
                    output_file.write(f"{key}: {value}\n")
            output_file.write("\n")  # Add a newline for readability
    
    print("Output has been written to Reaction_Details_mg37.txt")

if __name__ == "__main__":
    main()