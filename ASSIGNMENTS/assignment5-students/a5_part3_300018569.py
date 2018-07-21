#Family name: Tara
# Student number: 300018569
# Course: IT1 1120 
# Assignment Number: 5

def digit_sum(n):
    """(int) -> int
    Returns the sum of all digits in a non-negative integer n.
    Precondition: n >= 0
    """
    #no work needed for numbers <= 9
    if n <= 9:
        return n
    else:
        #get ones place
        ones = n % 10
        #get everything not in the ones place
        tens_and_beyond = n//10
        return ones + digit_sum(tens_and_beyond)


def digital_root(n):
    """(int) -> int
    Returns the digital root of a number, n
    Precondition: n >= 0
    """
    if n <= 9:
        return n
    else:
        return digital_root(digit_sum(n))
