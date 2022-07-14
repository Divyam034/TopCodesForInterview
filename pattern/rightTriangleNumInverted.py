# Basic Right Triangle Number Pattern (Inverted)

"""

10987
456
32
1


"""

def rightTriangleNumberInverted(row):
    k = 1
    for i in range(1,row+1):
        for j in range(i):
            k = i*(i+1)//2
            print(k-j,end="")

        print()

rightTriangleNumberInverted(5)
    