# Longest substring without repeating characters #

def longest_substr(string):
    start = 0
    end = 0
    result = 0
    char_set = set()
    while start < len(string) and end < len(string):
        if string[end] not in char_set:
            char_set.add(string[end])
            end += 1
            result = max(end-start,result)
        else:
            char_set.remove(string[start])
            start += 1
    return result

print(longest_substr("abcabcbb"))
print(longest_substr("bbbbb"))
print(longest_substr("pwwkew"))
