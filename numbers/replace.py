# Python program to replace all 0's with 1's

def replace(num):
    num = list(num)
    for i in range(len(num)):
        if num[i] == "0":
            num[i] = "1"
    return "".join(num)

num = input("Enter any number: ")
print(replace(num))