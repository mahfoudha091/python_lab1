""" 
 Write a Python program which accepts the radius of a circle from the user and compute the area. 
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

from math import pi
radius = float(input(" input radius of the circle > "))
area = pi * radius**2
print(f"area of circle with radius {radius} is = {area}")