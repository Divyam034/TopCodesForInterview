# python  program to print hollow square
"""
******
*    *
*    *
*    *
*    *
******

"""

def hollowSquare(n):
    for i in range(n):
        if i==0 or i==n-1:
            print("*"*n)
        else:
            print("*"+" "*(n-2)+"*")

print(hollowSquare(4))