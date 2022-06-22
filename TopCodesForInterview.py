"""
# Python program to find whether a given number is prime or not
# First of all we will create some test cases
test1 = {
    'input': {
        'num':5
    },
    'output': True
}
test2 = {
    'input': {
        'num':-1
    },
    'output':False
}
test3 = {
    'input':{
        'num':0
    },
    'output': False
}
test4 = {
    'input':{
        'num':2
    },
    'output': True
}

tests = [test1, test2, test3, test4]

def is_prime(num):
    prime = True
    if num <2:
        prime = False
        return prime
    if num == 2:
        return prime
    for i in range(2,num):
        if num%i == 0:
            prime = False
            return prime

    return prime
for i in range(len(tests)):
    print(is_prime(tests[i]['input']['num']) == tests[i]['output'])



# Python program to find prime numbers between a given range
# First of all we will create some test cases

test1 = {
    'input': {
        'start': 2,
        'end':15
    },
    'output': [2, 3, 5, 7, 11, 13]
}
test2 = {
    'input': {
        'start': 3,
        'end': 3
    },
    'output': [3]
}
test3 = {
    'input': {
        'start': 15,
        'end':2
    },
    'output': [2, 3, 5, 7, 11, 13]
}

test4 = {
    'input': {
        'start': -2,
        'end':-1
    },
    'output': [-1]
}
tests = [test1,test2, test3, test4]
def prime_in_range(start, end):
    if start > end:
        start, end = end, start
    if end < 2:
        return [-1]
    if end == 2:
        return [2]
    prime = []
    for i in range(start, end+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime

for i in range(len(tests)):
    print(prime_in_range(tests[i]['input']["start"], tests[i]["input"]["end"]) == tests[i]['output'])



# Python program to find sum of digits of a number
# First of all we will create some test cases



test1 ={
    "input": {
        "num": "12345"
    },
    "output": 15 
}


test3 ={
    "input": {
        "num": "112233"
    },
    "output": 12
}

tests = [test1, test3]

def sumDigitsNumber1(num):              #using while loop
    sum = 0
    while int(num) > 0:
        digit = int(num) % 10
        sum += digit
        num = int(int(num)/10)
    return sum

def sumDigitsNumber2(num):              #using string extraction
    sum = 0
    for i in num:
        sum += int(i)
    return sum

for i in range(len(tests)):
    print(sumDigitsNumber1(tests[i]['input']["num"]) == tests[i]['output'])

for i in range(len(tests)):
    print(sumDigitsNumber2(tests[i]['input']["num"]) == tests[i]['output'])



# Python program to find reverse of a number or string
# First of all we will create some test cases

test1 = {
    "input":{
        "num_str": "87453"
    },
    "output":"35478"
}

test2 = {
    "input":{
        "num_str": ""
    },
    "output": -1
}

test3 = {
    "input":{
        "num_str": "a"
    },
    "output": "a"
}

tests = [test1, test2, test3]

def reverse_num_str(num_str):
    if len(num_str) == 0:
        return -1
    else:
        return num_str[::-1]

for i in range(len(tests)):
    print(reverse_num_str(tests[i]['input']["num_str"]) == tests[i]['output'])




# Python program to find whether a given string is palindrome or not
# First of all we will create some test cases

test1 = {
    "input":{
        "num": "12233221"
    },
    "output": "Palindrome"
}

test2 = {
    "input":{
        "num": "234321"
    },
    "output": "Not Palindrome"
}

tests = [test1, test2]

def palindrome_check1(num):         #string slicing
    reverse = num[::-1]
    if reverse == num:
        return "Palindrome"
    else:
        return "Not Palindrome"

def palindrome_check2(num):
    reverse = 0
    temp = int(num)
    while temp>0:
        digit = temp % 10
        reverse = reverse*10 + digit
        temp = int(temp / 10)

    if str(reverse) == num:
        return "Palindrome"
    else:
        return "Not Palindrome"

for i in range(len(tests)):
    print(palindrome_check1(tests[i]["input"]["num"]) == tests[i]["output"])

for i in range(len(tests)):
    print(palindrome_check2(tests[i]["input"]["num"]) == tests[i]["output"])



# Python program to find whether a given number is armstrong number or not
# First of all we will create some test cases

test1 = {
    "input":{
        "num":153
    },
    "output": True
}

test2 = {
    "input":{
        "num":0
    },
    "output": True
}

test3 = {
    "input":{
        "num":1
    },
    "output": True
}

test4 = {
    "input":{
        "num":123
    },
    "output": False
}

tests = [test1, test2, test3, test4]

def is_armstrong(num):
    sum = 0
    num = str(num)
    power = len(num)
    temp = int(num)
    while temp > 0:
        digit = temp % 10
        temp = int(temp/10)
        sum += digit**power

    if sum == int(num):
        return True
    return False

for i in range(len(tests)):
    print(is_armstrong(tests[i]["input"]["num"])== tests[i]["output"])




# Python program to find armstrong number in a given range
# First of all we will create some test cases

test1 = {
    "input":{
        "start": 100,
        "end": 160
    },
    "output": [153]
}

test2 = {
    "input":{
        "start": 0,
        "end" : 50
    },
    "output": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}

test3 = {
    "input":{
        "start": 2,
        "end": 50
    },
    "output": [2, 3, 4, 5, 6, 7, 8, 9]
}

tests = [test1, test2, test3]

def armstrong_range(start, end):
    arm = []
    for i in range(start, end):
        temp = i
        sum = 0
        power = len(str(i))
        while temp>0:
            digit = temp%10
            sum += digit**power
            temp = int(temp/10)

        if i == sum:
            arm.append(i)
        
    return arm
    

for i in range(len(tests)):
    print(armstrong_range(tests[i]["input"]["start"],tests[i]["input"]["end"] )== tests[i]["output"])



# Python program to find fibonacci series upto n
# First of all we will create some test cases

test1 = {
    "input": {
        "num": 4
    },
    "output": [0,1,1,2]
}

test2 = {
    "input": {
        "num": 6
    },
    "output": [0,1,1,2,3,5]
}

test3 = {
    "input": {
        "num": 2
    },
    "output": [0,1]
}

tests =[test1, test2, test3]

def fibonacci(num):
    fib = [0,1]
    n1, n2 = 0,1
    for i in range(2, num):
        n3 = n2+n1
        n1 = n2
        n2 = n3
        fib.append(n3)
        
    return fib

for i in range(len(tests)):
    print(fibonacci(tests[i]["input"]["num"])== tests[i]["output"])



# Python program to find prime factors of given number
# First of all we will create some test cases

test1 = {
    "input":{
        "num": 10
    },
    "output": [2,5]
}

test2 = {
    "input":{
        "num": 15
    },
    "output": [3,5]
}

test3 = {
    "input":{
        "num": 2
    },
    "output": [2]
}

tests = [test1, test2, test3]

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_factors(num):
    prime = []
    if num == 2:
        prime.append(2)
    for i in range(1, num):
        if num % i == 0:
            if is_prime(i):
                prime.append(i)
    return prime

for i in range(len(tests)):
    print(prime_factors(tests[i]["input"]["num"])== tests[i]["output"])



# Python program to check whether a number is perfect number or not
# First of all we will create some test cases

test1 = {
    "input":{
        "num": 28
    },
    "output": True
}

test2 = {
    "input":{
        "num": 6
    },
    "output": True
}

test3 = {
    "input":{
        "num": 8
    },
    "output": False
}

tests = [test1, test2,  test3]
def is_perfect(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            print(i)
            sum += i
    if sum == num:
        return True
    return False

for i in range(len(tests)):
    print(is_perfect(tests[i]["input"]["num"])== tests[i]["output"])

"""

# Python program to check whether a number is perfect square or not
# First of all we will create some test cases

test1 = {
    "input":{
        "num": 25
    },
    "output": True
}

test2 = {
    "input":{
        "num": 20
    },
    "output": False
}

test3 = {
    "input": {
        "num": 1
    },
    "output": True
}

def is_perfectsquare(num):                  # Time complexity is O(N)
    for i in range(1, num+1):
        rem = int(num/i)
        if rem == i:
            return True
    return False
tests = [test1, test2, test3]
for i in range(len(tests)):
    print(is_perfectsquare(tests[i]["input"]["num"]) == tests[i]["output"])


def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo+hi)//2
        result = condition(mid)
        if result == "found":
            return True
        elif result == "left":
            hi = mid-1
        elif result == "right":
            lo = mid+1
    return False

def is_perfectsquareBS(num):
    def condition(mid):
        if mid**2 == num:
            return "found"
        elif mid**2 < num:
            return "right"
        elif mid**2 > num:
            return "left"
    
    return binary_search(0, num, condition)

for i in range(len(tests)):
    print(is_perfectsquareBS(tests[i]["input"]["num"]) == tests[i]["output"])
