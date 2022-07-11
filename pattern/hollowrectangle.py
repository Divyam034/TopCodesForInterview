# python program to print hollow rectangle

def hollowRectangle(length, breadth):
    for i in range(breadth):
        if i==0 or i==breadth-1:
            print("*"*length)
        else:
            print("*"+" "*(length-2)+"*")

print(hollowRectangle(7,4))