def duplicate(l): #O(n)
    """(list) -> bool
    Return True if a duplicate exists in list l,
    otherwise return False.
    """
    max_min = maximum_minimum(l)
    maximum = max_min[1]
    tmp = 0
    if max_min[0] < 0:
        maximum += abs(max_min[0]) 
    bits = [False for i in range(maximum + 1)]
    for i in l:
        if i < 0:
            tmp = max_min[1] + abs(i)
        else:
            tmp = i
        if(bits[tmp]):
            return True
        else:
            bits[tmp] = True
    return False
def maximum_minimum(l): # O(n)
    """(list) -> (int, int)
    Returns maximum and minimum of list l
    (minimum, maximum)
    """
    minimum = maximum = l[0]
    for i in l:
        if i < minimum:
            minimum = i
        elif i > maximum:
            maximum = i
    return (minimum, maximum)

