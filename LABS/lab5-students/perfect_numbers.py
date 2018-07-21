import math
def perfect_numbers():
    """(None) --> (None)
        Prints all perfect numbers (sum of all positive divisors = itself)
    """
    i = 1
    while True:
        if is_perfect(i):
            print(i)
        i += 1

def is_perfect(n):
    """(int) -> bool
        Return whether or not a number is perfect.
        Preconditions: n > 0
    """
    l = []
    if n % 2 == 0:
        for i in range(1, int(math.sqrt(n)) + 1):
            if i == n:
                break
            if n % i == 0:
                l.insert(0, i)
                other = n // i
                if other != n:
                    l.insert(0, other)
    return sum(l) == n
