# python program to find hcf of two numbers using recursion



def HCF(num1, num2):
    if num2 == 0:
        return num1
    return HCF(num2, num1%num2)


num1, num2 = map(int, input().split(" "))
print("HCF is", HCF(num1, num2))

def LCM(num1, num2):
    return (num1*num2)//HCF(num1, num2)

print("LCM is", LCM(num1, num2))