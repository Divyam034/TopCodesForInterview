# python program to find maximum number of element in an array


def maxInArr(arr):
    if n == len:
        return max
    if arr[i] > max:
        max = arr[i]
    i+=1
    return maxInArr(arr)

# driver code
i=0
arr = [int(x) for x in input().split(" ")]
max = arr[0]
n = len(arr)
print("Minimum element in array is:",maxInArr(arr))