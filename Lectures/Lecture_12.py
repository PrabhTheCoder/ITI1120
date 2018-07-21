#SEARCHING

#O(n)
#LINEAR SEARCH
def count(l,x):
    """ (list, Object) -> int

    """
    count = 0
    for i in l:
        if i == x:
            count += 1
    return count

#O(n^2)
def triplicates(l):
    """ (list) -> bool """

    for item in l:
        if count (l, item) >= 3:
            return True
    return False

#O(n^2)
def k_tuple(l, k):
    for item in l:
        if count(l, item) >= k:
            return True
    return False

def majority(l, k):
    for item in l:
        if count(l, item) >= k:
            return True
    return False
