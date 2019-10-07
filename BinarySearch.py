# Binary search #

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]> target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(binary_search([-1,0,3,5,9,12], 9))
print(binary_search([-1,0,3,5,9,12], 2))


