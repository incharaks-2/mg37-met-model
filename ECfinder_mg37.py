# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:14:30 2024

@author: Inchara
"""

import os #OS module of python that interacts with the operating system of the system
print('Get current working directory : ', os.getcwd()) #gets current working directory
#To open the text based file such as textfile, word document or excel sheet
#Both the file and interpreting code should be in same directory
file_handler=open("feature_mg37.txt","r") #.txt file containg feature column of RAST annotation
output_file=open("ECfinder_mg37.txt", "w") 
print("File is open")
for line in file_handler:# as the .txt file has \n as the last charachter in each line end we need to remove it using strip() else after each output we get a blanck line
    if "(EC" in line:
     stripped_line = line.strip()
     #print(stripped_line)
     output_file.write(stripped_line + "\n")
print("Job Done")