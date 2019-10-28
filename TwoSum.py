# Two Sum #

def two_sum(nums,target):
    num_dict = dict()
    for i,val in enumerate(nums):
        if target - val in num_dict:
           return([num_dict[target-val],i])
        else:
            num_dict[val] = i
    return -1
    

print(two_sum([10,15,3,7], 17))
print(two_sum([5,3,4], 10))
    
