# Program to check whether two strings are anagrams #
def anagram(s,t):
    dict1 = dict()
    dict2 = dict()
    for i in s:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    for j in t:
        if j in dict2:
            dict2[j] += 1
        else:
            dict2[j] = 1
    if dict1 == dict2:
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")

anagram('dog', 'god')
anagram("rat", "car")
anagram("anagram", "nagaram")
