# python program to reverse a number using recursion



def recur_reverse(num,reverse=0):
    # global reverse
    if num==0:
        return reverse
    reverse = reverse*10 + num%10
    num //=10
    return recur_reverse(num,reverse)

# reverse = 0
num = int(input("Enter a number: "))
print(recur_reverse(num))