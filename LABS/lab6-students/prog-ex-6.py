from sys import stdout

def fib(n):
    l = [0, 1]
    if n == 0:
        return l[0]
    elif n == 1:
        return l[1]
    
    for i in range(2, n+1):
        l.append(l[i-1] + l[i-2])
    return l[-1]
        
    
    
