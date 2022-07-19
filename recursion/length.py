# length of string using python

from itertools import count


def length(str):
    global count
    if str=="":
        return count
    count +=1
    return length(str[1:])
    
count = 0
str = input("Enter a string: ")
print(length(str))