# python program to count number of times a digit occurs in a number

def count_digit(num, digit):
    count = 0
    while num>0:
        rem = num%10
        if digit == rem:
            count +=1
        num //=10
    return count

print(count_digit(123212,1))