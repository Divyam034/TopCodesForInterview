# HCF of two numbers in python

def Hcf(lst):
    hcf = 1
    for i in range(1, lst[0]+1):
        count = 0
        for j in lst:
            if j % i == 0:
                count+=1
        if count == len(lst):
            hcf = i
    return hcf
