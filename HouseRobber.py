# House Robber Problem #

# Dynamic Programming Approach #

def rob_house(house_lst):
    if len(house_lst) == 0:
        return 0
    if len(house_lst) == 1:
        return house_lst[0]
    if len(house_lst) == 2:
        return max(house_lst)

    dp = [0 for i in range(len(house_lst))]
    dp[0] = house_lst[0]
    dp[1] = max(house_lst[0], house_lst[1])

    for i in range(2,len(house_lst)):
        dp[i] = max(dp[i-1], house_lst[i]+ dp[i-2])

    return dp[-1]

print(rob_house([1,2,3,1]))
print(rob_house([2,7,9,3,1]))
