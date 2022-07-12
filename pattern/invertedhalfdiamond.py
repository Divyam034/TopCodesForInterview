# python program to print inverted half diamond

def invertedHalfDiamond(row):
    mid = row//2+1
    for i in range(mid):
        print(" "*(mid-i-1), end="")
        print("*"*(i+1))
    for i in range(mid, row):
        print(" "*(i-mid+1), end="")
        print("*"*(row-i))


invertedHalfDiamond(5)