# calcuate fibonacci series
# import sqrt from the math module
from math import sqrt 

n = int(input("Add a number to get its fibonacci series: "))

theta = 1.618034    #this is a constant

fn = ((theta**n) - (1 - theta)**n) / sqrt(5)
print(round(fn))