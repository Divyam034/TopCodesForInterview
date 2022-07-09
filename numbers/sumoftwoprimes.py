# Can a number be expressed as a sum of two prime numbers


def is_prime(num):
    if num == 2:
        return True
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sumoftwoprimes(num):
    ans = ""
    for i in range(1,num):
        if is_prime(i) and is_prime(num-i) and i<= num-i:
            ans += f"{num} is sum of two primes {i} and {num-i} \n"         
    return ans
num = int(input("Please enter a number: "))
print(sumoftwoprimes(num))