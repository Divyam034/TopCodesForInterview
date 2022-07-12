# python program to print inverted pyramid
"""
           *******
            *****
             ***
              *

"""

def invertedPyramid(row):
    for i in range(row):
        print(" "*i, end="")
        star = 2*(row-i)-1
        print("*"*star)

invertedPyramid(5)