# Given an integer, find the sum of individual digits in that integer #

# Recursive Solution #
def digit_sum(n):
    if n == 0:
        return 0
    else:
        return n%10 + digit_sum(n//10)

print(digit_sum(4321))
print(digit_sum(12))
print(digit_sum(24))
