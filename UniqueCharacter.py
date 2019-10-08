# First unique character in a string #

def unique_char(string):
    char_count =  dict()
    for i in string:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    for i,val in enumerate(string):
        if char_count[val] == 1:
            return i
    return -1

print(unique_char("leetcode"))
print(unique_char("loveleetcode"))
