# fibonacci sequence #

# Recursive Solution #
def fib(n):
    if n == 0 or n == 1 or n==2:
        return 1
    else:
        return fib(n-1)+ fib(n-2)

print(fib(10))
print(fib(2))
print("\n")

# Iterative Solution #
def fibo(n):
    val1 = 0
    val2 = 1
    for i in range(n):
        new_val = val1 + val2
        val1 = val2
        val2 = new_val
    return val1

print(fibo(10))
print(fibo(2))

