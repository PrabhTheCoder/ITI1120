def power_set(L):
    '''[list) -> 2D list'''
    if len(L) == 0:
        return [[]]
    
    ps = power_set(L[1:])
    psf = ps[:]
    
    for item in ps:
        psf.append([L[0]] + item)

    return psf


def mypow(x,n): # x^n #O(n) operations
    '''(int, int) -> int
    Precondition: n is non-negative'''  
    if n == 0:
        return 1 #O(1)
    else:
        return x * mypow(x, n-1) #O(1) 

#O(log n) operations
def mypow_v2(x, n):
    if n == 0:
        return 1 #O(1)
    if n == 1:
        return x #O(1)
    res = mypow_v2(x, n//2) #O(1)
    if n % 2 == 0:
        return res * res #O(1)
    else:
        return x*res * res #O(1)
    
    

