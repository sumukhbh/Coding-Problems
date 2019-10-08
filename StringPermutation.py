# Given a String, find all permutations of that string #

def permute(s):
    result = list()
    if len(s) == 1:
        result.append(s)
    else:
        for letter in range(len(s)):
            for perm in permute(s[:letter]+s[letter+1:]):
               result += [s[letter]+perm]
    return result

print(permute("abc"))
print(permute("def"))
