'''
author: https://github.com/thewhitetulip

Prints the names of all the text files in the current working directory.

Part of 
    1. The video tutorial: https://youtu.be/7wuKDDMb3R4
    1. The ebook: https://github.com/thewhitetulip/build-app-with-python-antitextbook.

'''
import os

files = os.listdir() # listdir() returns a list of all files and folders of the current working directory
for file in files: # loops through each element inside files
    if file.endswith(".txt"):
        print(file)
