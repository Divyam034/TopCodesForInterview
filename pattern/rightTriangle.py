# python program to print right angled triangle

"""

*
**
***
****
*****

"""

def rightTriangle(row):
    for i in range(row):
        print("*"*(i+1))

row = int(input("Please enter row's number: "))
print(rightTriangle(row))