#O(1)
def print_num(n):
    print(n)

#O(n)    
def print_ints(n):
    """(int)->None
    """
    for i in range(1, n+1): 
        print(i)
        print("*")
        
#O(n)
def print_odds(n):
    for i in range(1, n+1, 2): 
        print(i)
        print("*")
        
#O(n^2)
def print_foo(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i,j)

#O(logn)
def mystery(n):
    print("Starting n =", n)
    while n > 1:
        n = n//2
        print(n)


#O(n)
def linear_search(L, v):
    """(list, object)-> int"""
    for i in range(len(L)):
        if L[i] == v:
            return i
    return -1

#O(logn)
def binary_search(l, value):
    """(list, object) -> int
    Returns index of the value if it is in the list.
    Otherwise -1.
    Precondition: list l is sorted.
    """
    
    e = len(l) - 1
    b = 0
    while e-b > 1:
        mid = (b+e)// 2
        key = l[mid]
        if value < key:
            e = mid - 1
        elif value > key:
            b = mid + 1
        else: #found value :)
            return mid
    if l[b] == value:
        return b
    elif l[e] == value:
        return e
    return -1



#O(logn)
def my_binary_search(l, value):
    """(list, object) -> bool
    Returns whether or not the value is in the list.
    Precondition: list l is sorted.
    """
    
    g = list(l)
    while len(g) > 2:
        i = len(g) // 2
        key = g[i]
        if value < key:
            g = g[:i]
        elif value > key:
            g = g[i:]
        else:
            return True
    return g[0] == value or g[1] == value
