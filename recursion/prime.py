# prime number using recursion

def is_prime(num, i =2):
    if num == i:
        return True
    elif num%i == 0:
        return False
    return is_prime(num, i+1)
    

print(is_prime(7))