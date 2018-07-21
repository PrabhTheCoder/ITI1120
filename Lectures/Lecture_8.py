############################################IN CLASS######################################################
def print_vowels(phrase):
    '''(str) -> None
    Display the vowels in phrase
    '''
    for i in phrase:
        if i.casefold() in "aeiou":
            print(i, end = ' ')
            
def count_vowels(phrase):
    '''(str) -> int
    Return number of vowels in phrase.

    >>> count_vowels("August")
    3
    >>> count_vowels("eye")
    2
    >>> count_vowels("bcd")
    0
    '''
    
    vowel_count = 0
    
    for i in phrase:
        if i.casefold() in "aeiou":
            vowel_count += 1

    return vowel_count

def only_vowels(phrase):
    '''(str) -> str
    Return a string containing all vowels in phrase

    >>> only_vowels("August")
    'Auu'
    >>> only_vowels("eye")
    'ee'
    >>> only_vowels("bcd")
    ''
    '''
    
    v = ""
    
    for i in phrase:
        if i.casefold() in "aeiou":
            v += i

    return v
################## MYSELF #########################################
def count_vowels_v2(phrase):
    '''(str) -> int
    prints number of vowels in phrase.

    >>> count_vowels("August")
    3
    >>> count_vowels("eye")
    2
    >>> count_vowels("bcd")
    0
    '''
    
    print(*map(phrase.casefold().count, "aeiou"))
