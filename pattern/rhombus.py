# python program to display rhombus star pattern
"""

*****
 *****
   *****
    *****
     *****


"""
def rhombus(num):
    for i in range(num):
        print(i*" ", end="")
        print("*"*num)

print(rhombus(5))
