def gcd(a,b):
    """(int, int) -> int
    Returns the greatest common denominator using euclid's algorithm
    Precondition a >= b, b > 0
    """
    #if remainder 0 remainder is a
    if b == 0:
        return a
    # gcd(a, b) = gcd(b, r) 
    return gcd(b, a % b)
