def is_sorted(l):
    """(list) -> bool
        Return whether or not elements in the list l are sorted.
        Preconditions: list can only contain numbers.
        size of list is greater than 1.
    """
    lastnumber = l[0]
    state = True
    for i in l:
        if(lastnumber > i):
            state = False
            break
        else:
            lastnumber = i
        
    return state
