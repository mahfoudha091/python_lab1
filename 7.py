""" 
Write a Python program to accept a filename from the user and print the extension of that. 
Sample filename : abc.java
Output : java 
"""

file_name = input("input yourfile name > ")
extention = file_name.split(".")
print(f"your extention is {extention[-1]}") 