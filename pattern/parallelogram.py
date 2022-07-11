# python program to print parallelogram

"""

******
 ******
   ******
    ******

"""

def parallelogram(length, breadth):
    for i in range(breadth):
        print(" "*i, end="")
        print("*"*(length))

print(parallelogram(6,4))