# python program to find minimum in array

def find_min(arr, n):
    if n == 1:
        return arr[0]
    return min(arr[n-1], find_min(arr, n-1))


# driver code
arr = [int(x) for x in input().split(" ")]
n = len(arr)
print(find_min(arr, n))