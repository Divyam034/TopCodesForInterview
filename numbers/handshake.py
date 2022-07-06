# number of handshakes between n people

def handshakes(n):
    return n*(n-1)//2

n = int(input("Enter a number: "))
print(handshakes(n))