def is_palindrome_v3(s):
    """ (str) -> bool

    Return True iff s is a palindrome.

    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('dented')
    False
    """
    i = 0
    j = len(s) - 1
    #[ | | | | ] -> [i| | |j] -> [ |i|j| ] -> [ |j|i| ] ->x<-
    #Compares pairs of letters.
    while i < j and s[i] == s[j]:
        i = i+1
        j = j-1
    return j <= i
