# Buy and sell Stock Problem with only transaction allowed #

# Greedy Approach #

def max_profit(prices):
    min_price = float("inf") # Initialize the min_price to a largest value #
    profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = max(profit, price - min_price)
    return profit

print(max_profit([12,11,15,3,10]))
print(max_profit([7,1,5,3,6,4]))
print(max_profit([7,6,4,3,1]))

