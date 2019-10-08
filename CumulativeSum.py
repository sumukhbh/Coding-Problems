# Given an Integer, find the cumulative sum of 0 to that integer #

# Recursive solution #
def total(n):
    if n == 0:
        return 0
    else:
        return n + total(n-1)

print(total(4))
print(total(5))
print(total(100))
