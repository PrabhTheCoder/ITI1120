def divisors(n):
    """(int) -> str
    Returns a string containing divisors of n.
    Preconditions: n > 0
    """
    divisors = "1"
    for i in range(1, n):
        if(n % (i+1) == 0):
            divisors += ", " + str(i+1)
    return divisors

def prime(n):
    """(int) -> bool
    Returns whether or not a number is a prime.
    Preconditions: n > 0.
    """
    return divisors(n) == "1, " + str(n)

num = int(input("Enter a non-negative integer: "))
print(divisors(num))
if prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
