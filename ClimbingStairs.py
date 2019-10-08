# Climbing Stair Case Problem #
def stair_case(n):
    first = 1
    second = 2
    if n ==1:
        return 1
    for i in range(3, n+1):
        val = first + second
        first = second
        second = val
    return second

print(stair_case(2))
print(stair_case(3))

