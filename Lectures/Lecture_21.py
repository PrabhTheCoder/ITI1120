def silly_printer(n):
    if n==0:
        print("Blast Off")
    else:
        silly_printer(n-1)
        print(n)
silly_printer(10)

#n! is defined for non negative integers.
#0! = 1
#n*(n-1)! n >= 1
def fact(n):
    """Precondition: n is non-negative integer"""
    if n == 0:
        return 1
    return n*fact(n-1)


def summation(L):
    if len(L) == 0:
        return 0
    return L[0] + summation(L[1:])

def summer_v2(L):
    if len(L) == 0:
        return 0
    if len(L) == 1:
        return L[0]

    return summer_v2(L[:len(L)//2]) + summer_v2(L[len(L)//2:])
