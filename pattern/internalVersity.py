# Printing Internal Varsity Number Square Pattern
"""

        333
        313
        323
        333


"""

def internalVarsity(len, bre):
    for i in range(bre):
        if i == 0 or i == bre-1:
            print("3"*len)
        else:
            innerNo = str(i)*(len-2)
            print("3"+innerNo+"3")


len, bre = map(int, input("Please enter length and breadth sepated by a space: ").split(" "))
internalVarsity(len,bre)
