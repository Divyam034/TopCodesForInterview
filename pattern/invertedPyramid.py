# python program to print inverted pyramid
"""
           *******
            *****
             ***
              *

"""

def invertedPyramid(row):
    # kn = row+1 + (row-1)*(-2)
    for i in range(row):
        print("*"*)