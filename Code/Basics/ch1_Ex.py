# Write a python program to print the contents of a directory using the os module.
#Search online for the function which does that. 
import os
path=r"C:\Users\soban\OneDrive\Documents\5 Sem\SD&A\lab reports" #In Python, backslashes \ are escape characters (like \n for newline, \t for tab). So your path is being misinterpreted. so thats why we use r prefix at start of string 
contents=os.listdir(path)
for item in contents:
    print(item)
#simple Printing 
print("Print any thing ")