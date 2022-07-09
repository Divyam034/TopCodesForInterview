# python program to reverse a number using recursion


def recur_reverse(num):
    global reverse
    if num > 0:
        digit = num%10
        reverse = reverse*10 + digit
        return recur_reverse(num//10)
    return reverse

reverse = 0
num = int(input("Enter a number: "))
print(recur_reverse(num))