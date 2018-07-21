def is_palindrome_v2(s):
    """(str) -> bool
    Return whether or not a string is a palindrome. While ignoring
    letters not of the english alphabet
    """
    # Base case, if length 1 or less its a palindrome
    if len(s) <= 1:
        return True
    
    # If the first letter is not of the alphabet ignore it then check the next
    if not s[0].isalpha():
        return is_palindrome_v2(s[1:])

    # If last letter is not of the alphabet ignore it then check the one prior
    if not s[-1].isalpha():
        return is_palindrome_v2(s[:-1])

    # If the first and last letter are not equal then it is not a palindrome
    if s[0].casefold() != s[-1].casefold():
        return False
    
    return is_palindrome_v2(s[1:-1])

    
