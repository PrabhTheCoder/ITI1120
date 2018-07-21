def arithmetic(l):
    """(list) -> bool
        Return whether or not elements in the list l are progressing
        arithmetically.
        Preconditions: list can only contain numbers.
        size of list is greater than 1.
    """
    diff = l[1]-l[0]
    lastnumber = l[0]
    state = True
    for i in l:
        if(lastnumber + diff != i and lastnumber != i):
            state = False
            break
        else:
            lastnumber = i
        
    return state


