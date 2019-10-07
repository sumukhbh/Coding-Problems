# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A #
def sort_parity(arr):
    odd_arr = list()
    even_arr = list()
    for i in arr:
        if i%2 == 0:
            even_arr.append(i)
        else:
            odd_arr.append(i)
    parity_array = even_arr + odd_arr
    return parity_array

print(sort_parity([3,1,2,4]))
print(sort_parity([1,5,6,2]))
