# Python Program for Printing Basic Right Triangle Number Pattern

"""

    1
    23
    456
    78910

"""

def rightTriangleNum(row):
    k = 1
    for i in range(row):
        for j in range(i+1):
            print(k, end="")
            k+=1
        print()

row = int(input("Enter a number:"))
rightTriangleNum(row)

    