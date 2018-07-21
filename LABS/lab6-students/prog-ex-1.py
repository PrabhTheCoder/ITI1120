def sum_odd_while_v2(n):
    '''(int)->int
        Returns the sum of all odd integers between 5 and n
    '''
    i = 5
    count = 0
    while i <= n:
        count += i
        i += 2
    return count
