# python program to find maximum number of element in an array

def find_max(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n-1], find_max(arr, n-1))

arr = [2,4,3,5,2]
n = len(arr)
print(find_max(arr, len(arr)))



#max[2, max[5, max[3, max[4, max[2, 2]]]]]
