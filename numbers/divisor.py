# python program to find number of numbers exactly divisible by divisor

def count_divisor(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count+=1
    return count

def count_numbers(num, divisor):
    count = 0
    for i in range(1, num+1):
        if count_divisor(i) == divisor:
            count+=1
    return count
print(count_numbers(7,2))