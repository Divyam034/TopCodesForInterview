# addition of two fractions

def hcf(num1, num2):
    hcf = 1
    for i in range(1, num1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
    return hcf

def addition_fractions(n1,n2,d1,d2):
    num = (n1*d2+n2*d1)
    den = (d1*d2)
    divisor = hcf(num, den)
    ans_num = num//divisor
    ans_den = den//divisor
    return f"{ans_num} / {ans_den}"

print(addition_fractions(2,8,4,9))