# length of string using python

from operator import length_hint


def length(str):
    if str == "":
        return 0
    return 1+ length(str[1:])

print(length("apple"))