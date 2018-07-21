def min_or_max_index(lst, find_min):
    """(list of numbers, bool) -> tuple of (number, int)
        Return the index of the minimum or maximum and the minimum or maximum.
        Preconditions: len(lst) >= 1
    """
    if find_min:
        return get_min(lst)
    else:
        return get_max(lst)
def get_max(lst):
    """(list of numbers) -> (number,index)
        Return maximum value in list and its index
        Preconditions: len(lst) >= 1
    """
    maximum = lst[0]
    index = 0
    for i in range(len(lst)):
        if lst[i] > maximum:
            maximum = lst[i]
            index = i
    return (maximum, index)

def get_min(lst):
    """(list of numbers) -> (number,index)
        Return minimum value in list and its index
        Preconditions: len(lst) >= 1
    """
    minimum = lst[0]
    index = 0
    for i in range(len(lst)):
        if lst[i] < minimum:
            minimum = lst[i]
            index = i
    return (minimum, index)
