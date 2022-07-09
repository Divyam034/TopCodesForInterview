# power of a number using recursion

def power(num, pow):
    if pow > 0:
        pow -= 1
        return num*power(num,pow)
    else:
        return 1


print(power(3,4))