""" file.py. Author: Someone. Date: Jan 18 2017.
 prints all the files and folders in the current working directory.
 execution: python3 file.py " i " ''''''''''''' "".
 dependency: Python3."""

'''
this is a random unrequired multi line comment just to signify that we can use " or """"""""" inside this triple quote
'''

import os 

files = os.listdir() 

# for loop will print all the txt files in the current working directory.
for file in files:
    if file.endswith(".txt"):
        print(file)
