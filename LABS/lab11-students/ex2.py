def count_digits(n):
    """(int) -> int
    Return the number of digits in the integer n.
    Precondition: n >= 0
    """
    # If it is 0 it is a 1 digit number no work needed
    if n // 10 == 0:
        return 1
    return 1 + count_digits(n//10)
