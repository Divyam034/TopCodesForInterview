# Basic incrementing Triangle Pattern initialised = 3

"""

6666
555
44
3




def basicIncrementingTriangle(rows):
    k = 3
    for i in range(rows):
        for j in range(i+1,0,-1):
            print(j)
            # print(k+i-1,end="")
        print()

basicIncrementingTriangle(5)

"""

def is_armstrong(num):
    temp = num
    pow = len(str(num))
    sum = 0
    while temp>0:
        digit = temp%10
        sum += digit**pow
        temp //=10
    if sum == num:
        return "is armstrong"
    else:
        return "not armstrong"
print(is_armstrong(153))