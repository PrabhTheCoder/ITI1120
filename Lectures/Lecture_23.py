import random

####################################################
# quick sort
####################################################

def quick_sort(a):
    """
    (list)->list
    returns a sorted copy of list a"""

    if len(a) < 2:
        return a[:]
    
    x = random.choice(a)
    lt, eq, gt = [], [], []

    for item in a:
        if item < x:
            lt.append(item)
        elif item == x:
            eq.append(item)
        else:
            gt.append(item)

    return quick_sort(lt) + eq + quick_sort(gt)

def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        return merge(left,right)

def merge(L1, L2):
    """(list, list) -> list
    Merge sorted lists L1, L2 into a new list and return that new list
    """
    newL = []
    i1 = 0
    i2 = 0
    while i1 != len(L1) and i2 != len(L2):
        if L1[i1] <= L2[i2]:
            newL.append(L1[i1])
            i1 = i1+1
        else:
            newL.append(L2[i2])
            i2 = i2+1
            
    newL.extend(L1[i1:])
    newL.extend(L2[i2:])
    return newL
