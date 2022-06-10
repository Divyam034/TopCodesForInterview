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

"""