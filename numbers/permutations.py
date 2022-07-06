# Permutations in which n people can occupy r seats in a classroom

def factorial(num):
    factorial = 1
    for i in range(1,num+1):
        factorial *= i
    return factorial

def permutations(n, r):
    return factorial(n)//factorial(n-r)

n, r = map(int, input().split(" "))
print(permutations(n,r))