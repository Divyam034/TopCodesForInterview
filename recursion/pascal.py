# python program to print pascal's triangle

def pascal(rows):
    res = [[1]]
    for i in range(rows-1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1])+1):
            row.append(temp[j]+temp[j+1])
        res.append(row)
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ", end="")
        for j in range(i+1):
            print(res[i][j], end=" ")
        print()
print(pascal(7))