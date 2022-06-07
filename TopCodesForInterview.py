# Python program to find whether a given number is prime or not
# First of all we will 
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