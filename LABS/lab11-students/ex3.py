def is_palindrome(s):
    """(str) -> bool
    Return whether or not a string is a palindrome.
    """
    if len(s) <= 1:
        return True

    if s[0].casefold() != s[-1].casefold():
        return False

    return is_palindrome(s[1:-1])

    
