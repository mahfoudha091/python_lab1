""" 
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

data = input("input some comma seprated  numbers > ")
list = data.split(",") 
tuple = tuple(list)
print(f"List :  {list}")
print(f"Tuple :  {tuple}") 