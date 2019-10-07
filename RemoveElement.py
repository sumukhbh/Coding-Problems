# Given an array and a value, remove all instances of value in-place and return new length#
def remove_element(arr, val):
    while val in arr:
        arr.remove(val)
    return len(arr)

print(remove_element([3,2,2,3], 3))
print(remove_element([0,1,2,2,3,0,4,2],2))

