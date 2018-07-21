def largest_34(a):
    """(list of numbers) -> number
        Returns the sum of the 3rd and 4th largest number
        Preconditions: len(a) >= 4
    """
    first = float("-inf")#lowest possible numbers so will get replaced with larger
    second = float("-inf")
    third = float("-inf")
    fourth = float("-inf")
    for num in a:
        if num >= first:
            fourth = third
            third = second
            second = first
            first = num
        elif num >= second:
            fourth = third
            third = second
            second = num
        elif num >= third:
            fourth = third
            third = num
        elif num >= fourth:
            fourth = num
    return third + fourth

def largest_third(a):
    """(list of numbers) -> number
        Returns the sum of the largest third of numbers
        Preconditions: len(a) >= 3
    """
    tmp = sorted(a, reverse=True)
    tmp = tmp[:len(a)//3]
    summation = 0
    for i in tmp:
        summation += i
    return summation

def third_at_least(a):
    """(list of numbers) -> number or None
        Returns the value that occurs len(a)//3+1 times, if none
        exist returns None. If more than one exists returns smaller
        value
        Preconditions: len(a) >= 4
    """
    
    tmp = sorted(a)
    third_of_a = len(a)//3
    third = None
    for i in range(len(tmp) - third_of_a):
        if tmp[i] == tmp[i+third_of_a]:
            if third == None:
                third = tmp[i]
            elif tmp[i] < third:
                third = tmp[i]
    return third

def sum_tri(a, x):
    """(list of numbers, number) -> bool
        Returns True if a value a[i] + a[j] + a[k] = x exists.
        Otherwise returns False.
    """
    tmp = sorted(a)
    for i in range(len(tmp)):
        j = i
        k = len(tmp) -1
        while j <= k:
            test_sum = tmp[i]+tmp[j]+tmp[k]
            if test_sum == x:
                return True
            elif test_sum > x:
                k -= 1
            else:
                j += 1
    return False
