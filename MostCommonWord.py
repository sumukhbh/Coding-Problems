# Most Common Word #

def most_common(sentence, banned_lst):
    for char in sentence:
        if (char == "!") or (char == "?") or (char == "'") or (char == ",") or (char == ";") or (char == ".") or (char == '"'):
            sentence = sentence.replace(char, " ")

    char_dict = {}
    sentence = sentence.lower().split()
    for char in sentence:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    result = ""
    value = 0
    for key,val in char_dict.items():
        if val > value and key not in banned_lst:
            result = key
            value = val
    return result

print(most_common("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(most_common("a,a,c,b,b,b,b,b", ["b"]))
            
            
