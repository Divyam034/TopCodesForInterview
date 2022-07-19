# prime number using recursion

def isPrime(num):
    global i
    if num == 2:
        return True
    if num < 2:
        return False
    if i == num:
        return True
    if num % i == 0:
        return False
    i+=1
    return isPrime(i)

i = 2
num = int(input("Enter a number: "))
print(isPrime(num))