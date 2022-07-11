# python program to print hollow pyramid

"""

    *
   * *
  *   *
 *     *
*********


"""


def hollowPyramid(row):
    k = 1
    for i in range(row):
        print(" "*(row-i-1),end="")
        if i==0:
            print("*")
        elif i==row-1:
            print("*"*(k+2))
        else:
            print("*",end="")
            print(" "*k, end="")
            print("*")
            k+=2

print(hollowPyramid(6))