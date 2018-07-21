def sum_5_consecutive(l):
    """(list of numbers) -> bool
    Return True if the sum of 5 consecutive numbers in a list is 0
    otherwise return false.
    """
    length = len(l)
    if length < 5:
        return False
    else:
        for i in range(length):
            if i + 4 >= length:
                break;
            if l[i] + l[i+1] + l[i+2] + l[i+3] + l[i+4] == 0:
                return True
        return False
    
def sum_5_consecutive_v2(l):
    """(list of numbers) -> bool
    Return True if the sum of 5 consecutive numbers in a list is 0
    otherwise return false.
    """
    length = len(l)
    if length < 5:
        return False
    else:
        i = 0
        while i+4 < length:
            if l[i] + l[i+1] + l[i+2] + l[i+3] + l[i+4] == 0:
                return True
            i += 1
        return False              
