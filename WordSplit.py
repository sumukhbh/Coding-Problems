# Given a string and list of words, we should determine if it's possible to split a string in a way in which words can be made from list of words #

# Recursive Solution #

def split_word(string, word_list, out_list = None):
    if out_list == None:
        out_list = []

    for word in word_list:
      if string.startswith(word):
          out_list.append(word)
          return split_word(string[len(word):], word_list, out_list)
    return out_list

print(split_word('themanran',['the','ran','man']))
print(split_word('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))
print(split_word('themanran',['clown','ran','man']))
