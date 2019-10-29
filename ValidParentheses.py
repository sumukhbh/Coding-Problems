# valid parentheses #

def valid_paren(s):
    if len(s)%2 != 0:
        return False
    open_paren = set("({[")
    match_paren = set([("(",")"),("{", "}"),("[", "]")])
    stack = []

    for char in s:
        if char in open_paren:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            val = stack.pop()
            if (val, char) not in match_paren:
                return False
    return len(stack) == 0

print(valid_paren("()"))
print(valid_paren("({[]})"))
print(valid_paren("(({[})"))
                
        
    
