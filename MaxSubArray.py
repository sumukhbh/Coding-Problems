# Maximum Subarray #

def Max_sub(num_lst):
    global_max = float("-inf")
    max_seen = float("-inf")
    for num in num_lst:
        max_seen += num
        global_max = max(global_max, max_seen, num)
        if max_seen < num:
            max_seen = num
    return global_max

print(Max_sub([-2,1,-3,4,-1,2,1,-5,4]))
