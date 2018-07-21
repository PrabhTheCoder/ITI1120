def is_divisible(n,m):
     '''(int, int)->bool
     returns True if n is divisible by n, and False otherwise.'''
     return n%m==0

def is_divisible23n8(n):
    '''(int) -> str
    Return yes if n is divisible by 2 or 3 and not 8 otherwise no.
    '''
    if (is_divisible(n, 2) or is_divisible(n, 3)) and (not(is_divisible(n,8))):
        return "yes"
    else:
        return "no"
     
def print_all_23n8(num):
    """(int) -> None
     Return all positive integers less than num that are
     divisible by 2 or 3 but not 8.
     Preconditions: num >= 0
    """
    for i in range(num):
         if is_divisible23n8(i) == "yes":
              print(i)
     
n = int(input("Please enter a non-negative integer: "))
print_all_23n8(n)
