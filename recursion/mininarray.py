# python program to find minimum in array

def find_min(arr, n):
    if n == 1:
        return arr[0]
    return min(arr[n-1], find_min(arr, n-1))

def minInArr(arr):
    global i, min
    if i == n:
        return min
    if arr[i]<min:
        min = arr[i]
    i+=1
    return minInArr(arr)


# driver code
i=0
arr = [int(x) for x in input().split(" ")]
min = arr[0]
n = len(arr)
print("Minimum element in array is:",minInArr(arr))