import math
def find_number_of_repeats(a, b):
    num = 0
    if b in a:
        return 0
    if len(b) < len(a):
        return -1
    
    index = -1
    count = 0
    is_possible = False
    for i in range(len(a)):
        if a[i] == b[0]:
            if index == -1:
                index = i
                is_possible = True
            count += 1
        elif index != -1 and a[i] == b[count]:
            count += 1
        elif index != -1:
            is_possible = False
            break;
        
    if is_possible:
        remaining = len(b) - count
        num = 1 + math.ceil(remaining/len(a))
        if b in a * num:
            return num
        else:
            return -1
    else:
        return -1
    
        
