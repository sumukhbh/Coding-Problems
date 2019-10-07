# Intersection of two arrays #

def intersect_array(arr1,arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    if len(set1) > len(set2):
        return list(set1.intersection(set2))
    else:
        return list(set2.intersection(set1))

print(intersect_array([1,2,2,1],[2,2]))
print(intersect_array([4,9,5], [9,4,9,8,4]))
