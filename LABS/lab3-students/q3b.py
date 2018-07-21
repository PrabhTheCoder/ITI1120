################Question 3b####################
def is_divisible23n8(n):
    '''(int) -> str
    Return yes if n is divisible by 2 or 3 and not 8 otherwise no.
    '''
    if (is_divisible(n, 2) or is_divisible(n, 3)) and (not(is_divisible(n,8))):
        return "yes"
    else:
        return "no"
def is_divisible(n, m):
    '''(int, int) -> bool
    Return if n is divisible by m.
    '''
    return n % m == 0

x = int(input("Enter an integer: "))

if is_divisible23n8(x) == "yes":
    print(x, "is divisible by 2 or 3 but not 8")
else:
    print("It is not true that", x, "is divisible by 2 or 3 but not 8")




    
