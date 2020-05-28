# Recursive implementation of reversing a string #

def rev_string(string):
    # Base case #
    if len(string) <= 1:
        return string
    return rev_string(string[1:]) + string[0]

print(rev_string("hello"))
print(rev_string("Sumukh"))

