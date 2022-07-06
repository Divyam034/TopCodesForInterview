# coordinate axis program in Python

def coordinate(num1, num2):
    if num1 > 0 and num2 > 0:
        return "First Quadrant"
    elif num1 < 0 and num2 > 0:
        return "Second Quadrant"
    elif num1 < 0 and num2 < 0:
        return "Third Quadrant"
    elif num1 > 0 and num2 < 0:
        return "Fourth Quadrant"
    elif num1 == 0 and num2 != 0:
        return "Lies on Y-Axis"
    elif num1 != 0 and num2 == 0:
        return "Lies on X-Axis"
    else:
        return "Lies on Origin"

num1, num2 = map(int, input().split(" "))
print(coordinate(num1, num2))