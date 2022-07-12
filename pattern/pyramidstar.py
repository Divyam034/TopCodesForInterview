# python program to print pyramid star pattern

"""
     *
    ***
   *****
  *******

"""



def pyramidstar(row):
    for i in range(row):
        # nth term = 1+(n-1)2 = 2n -1
        print(" "*(row-i-1),end="")
        print("*"*(2*((i+1)-1)-1))

row = int(input("Enter no of rows of the Pyramid: "))
print(pyramidstar(row))