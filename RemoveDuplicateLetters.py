# Remove duplicate letters from the string by just keeping the first occurrences only #

def remove_duplicate(string):
    # we will use a set to solve this problem #
    res = set()
    ans = []

    for char in string:
        if char not in res:
            res.add(char)
            ans.append(char)

    return "".join(ans)

print(remove_duplicate("tree traversal"))
print(remove_duplicate("Sumukh"))
