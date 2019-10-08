# Given a string, we need to check whether it's a palindrome or not #

def valid_palindrome(string):

    # i am considering empty string as a valid palindrome #
    if len(string) == 0:
        return True

    # Input string may contain non alphanumeric characters, Let's remove them from the string #
    string = [s for s in string.lower() if s.isalnum()]
    return string == string[::-1]

print(valid_palindrome("A man, a plan, a canal: Panama"))
print(valid_palindrome("race a car"))

