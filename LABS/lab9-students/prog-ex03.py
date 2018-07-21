def first_one(L):
    """(list L) -> int
    Returns position of first 1
    """
    
    begin = 0
    end = len(L) -1

    while end - begin > 1:
        mid = (begin + end)//2
        key = L[mid]
        if key == 0:
            begin = mid+1
        elif key == 1:
            end = mid -1
    if L[begin] == 1:
        return begin
    elif L[end] == 1:
        return end
    return -1

def last_zero(L):
    """(list L) -> int
    Returns position of last 0
    """
##    begin = 0
##    end = len(L) -1
##    while end - begin > 1:
##        mid = (begin + end)//2
##        key = L[mid]
##        if L[begin] == 1:
##            return begin -1
##        if key == 1:
##            end = mid -1
##        elif key == 0:
##            begin = mid + 1
##    if L[end] == 0:
##        return end
##    elif L[begin] == 0:
##        return begin
##    elif L[begin] == 1:
##        return begin -1
    
    return first_one(L)-1
