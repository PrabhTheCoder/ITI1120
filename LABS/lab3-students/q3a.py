################Question 3a####################
def is_divisible(n, m):
    '''(int, int) -> bool
    Return if n is divisible by m.
    '''
    return n % m == 0

x = int(input("Enter 1st integer:\n"))
y = int(input("Enter 2nd integer:\n"))

print(x, "is" +  " not" *( not(is_divisible(x,y)) ), "divisible by", y)




    
