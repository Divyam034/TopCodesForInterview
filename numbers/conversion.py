def b2d(num):
    binary_val = num
    decimal_val = 0
    base = 1
    while num > 0:
        digit = num%10
        decimal_val += digit*base
        num = num//10
        base *= 2
    return decimal_val


num_binary = int(input("Enter a binary number: "))
print(b2d(num_binary))

def o2d(num):
    octal_value = num
    decimal_value = 0
    base = 1
    while num>0:
        digit = num%10
        decimal_value += digit*base
        num = num//10
        base *= 8
    return decimal_value

num_octal = int(input("Enter a octal number: "))
print(o2d(num_octal))


def d2b(num):
    binary = []
    while num>0:
        binary.append(str(num%2))
        num = num//2
    binary = binary[::-1]
    return "".join(binary)

num_decimal = int(input("Enter a Decimal Number: "))
print(d2b(num_decimal))

def d2o(num):
    octal = []
    while num>0:
        octal.append(str(num%8))
        num = num//8
    octal = octal[::-1]
    return "".join(octal)

num_octal = int(input("Enter a Decimal Number: "))
print(d2o(num_octal))