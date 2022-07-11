# python program to print mirrored rhombus

"""

     ******
    ******
   ******
  ******
 ******
******

"""

def mirr_rhombus(side):
    for i in range(side):
        print(" "*(side-i), end="")
        print("*"*side)

print(mirr_rhombus(5))