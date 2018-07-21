def first_neg(l):
    """(list of numbers) -> int or None
    Return the index of the first negative number in a list
    if one exists, otherwise return nothing.
    """
    i = 0
    while (i + 1) < len(l) and l[i] >= 0:
        if l[i+1] < 0:
            return i+1
        i += 1
    
