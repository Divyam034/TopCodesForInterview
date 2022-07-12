# python program to print diamond pattern
"""

             *
            ***
           *****
          *******
           *****
            ***
             *

"""

def diamond(row):
    mid=row//2+1
    for i in range(mid):
        print(" "*(mid-i-1), end="")
        print("*"*(2*(i+1)-1))
    for i in range(mid, row):
        print(" "*(i+1-mid), end="")
        print("*"*(2*(row-i)-1))

diamond(11)