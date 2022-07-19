# python program to find hcf of two numbers using recursion


def hcf(num1, num2):
    if num2 == 0:
        return num1
    return hcf(num2,num1%num2)

num1, num2 = map(int, input("Enter two numbers separated by space: ").split(" "))

print("HCF is", hcf(num1, num2))
def LCM(num1, num2):
    return (num1*num2)//hcf(num1, num2)

print("LCM is", LCM(num1, num2))