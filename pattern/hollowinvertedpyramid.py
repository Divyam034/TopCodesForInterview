# python program to print hollow inverted pyramid

"""

           *******
            *   *
             * *
              *

"""

def invertedHollowPyramid(row):
    for i in range(row):
        print(" "*i,end="")
        if i == 0 or i == row-1:
            print("*"*(2*(row-i)-1))
        else:
            print("*"+" "*(2*(row-i)-3)+"*")

invertedHollowPyramid(5)