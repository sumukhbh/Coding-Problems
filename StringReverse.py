# Reverse a string #
# Recursive Solution #
def reverse_string(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse_string(s[:len(s)-1])

# Iterative Solution #
def rev_string(s):
    s = list(s)
    for i in range(len(s)//2):
        s[i], s[len(s)-1 -i] = s[len(s)-1-i], s[i]
    return "".join(s)

print(reverse_string("abc"))
print(reverse_string("xyz"))
print(reverse_string("hello"))
print("\n")


print(rev_string("abc"))
print(rev_string("xyz"))
print(rev_string("hello"))
