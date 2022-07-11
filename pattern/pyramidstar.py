# python program to print pyramid star pattern

"""
     *
    ***
   *****
  *******

"""



def pyramidstar(row):
    k=1
    for i in range(row):
        print(" "*(row-i-1),end="")
        print("*"*k)
        k += 2

row = int(input("Enter no of rows of the Pyramid: "))
print(pyramidstar(row))