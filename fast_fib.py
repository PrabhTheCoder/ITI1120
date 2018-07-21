#Original Pre-Lecture 22
def fib(n):
    """ (int) -> int
        Return the nth fibonacci number.
    """
    L = [[1, 1], [1, 0]]
    if n <= 0:
        return 0
    
    power(L, n-1)
    return L[0][0] #O(n)
    
def power(L, n):
    L2 = [[1, 1], [1, 0]]
    for i in range(2, n+1):
        two_d_multiply(L, L2)
    
#Post-lecture 22
#O(logn)
def fast_fib(n):
    """ (int) -> int
        Return the fibonacci number.
    """
    L = [[1, 1], [1, 0]]
    if n <= 0:
        return 0
    
    fast_power(L, n-1) # Since L^n results in [[Fn+1, Fn] [Fn, Fn-1]] where F is the fibonacci sequence
    return L[0][0]
    
def fast_power(L, n):
    """(2D list of int, int) -> None
    Mutates the List L into L to the power of n
    """
    v = [[1, 1], [1, 0]]
    if n == 1 or n == 0: # No work needed for these 2 cases
        return
    fast_power(L, n//2)  # Get our O(logn) time by dividing the exponent by 2 every time :)
    two_d_multiply(L, L) # The above line only gives L ^ (n/2) so we need to multiply it by itself to get L^n
    if n % 2 == 1: # Odd (Remember the odd case from class?) This pretty much accounts for the fact that the result will be L^(n-1) for an odd due to how integer division works.
        two_d_multiply(L, v)
def two_d_multiply(L, v):
    """(2D list of int, 2D list of int) -> None
    Mutates the List L into the result of matrix multiplying L by M
    """
    #Does basic matrix multiplication 
    #if you need help refer to https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplying-matrices-by-matrices/v/multiplying-a-matrix-by-a-matrix
    p1 = L[0][0] * v[0][0] + L[0][1] * v[1][0]
    p2 = L[0][0] * v[0][1] + L[0][1] * v[1][1]
    p3 = L[1][0] * v[0][0] + L[1][1] * v[1][0]
    p4 = L[1][0] * v[0][1] + L[1][1] * v[1][1]
    L[0][0] = p1
    L[0][1] = p2
    L[1][0] = p3
    L[1][1] = p4
