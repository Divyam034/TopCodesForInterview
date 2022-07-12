# python program to print halfDiamond

"""

*
**
***
****
***
**
*

"""

def halfDiamond(row):
    mid = row//2+1
    for i in range(mid):
        print("*"*(i+1))
    for i in range(mid, row):
        print("*"*(row-i))

halfDiamond(11)