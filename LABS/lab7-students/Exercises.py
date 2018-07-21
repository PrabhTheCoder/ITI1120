from itertools import combinations
from math import log2, floor
#5.16
def indexes(word, c):
    """(str, str) -> list of int
    Return list of indexes where str c occurs in word
    """
    indicies = []
    for i in range(len(word)):
        if word[i] == c:
            indicies.append(i)
    return indicies

#5.17
def doubles(l):
    """(list of int) -> None
    Displays a list of integers that are doubles of the previous index in l
    (L[i-1] = 1/2 L[i])
    """
    prev = None
    for i in l:
        if prev != None and i == 2*prev:
            print(i)
        prev = i

#5.18
def four_letter(l):
    """(list of str) -> list of str
    Return a list containing only strings of length 4 from l.
    """
    sublist = []
    for string in l:
        if len(string) == 4:
            sublist.append(string)
    return sublist

#5.19
def inBoth(lst_1, lst_2):
    """(list of objects, list of objects) -> bool
    Return true if there is an item common in both lists
    otherwise return False
    """
    for i in lst_1:
        if i in lst_2:
            return True
    return False

#5.20
def intersect(lst_1, lst_2):
    """(list of objects, list of objects) -> list of objects
    Return a list which only contains thecommon elements of lst_1 and lst_2.
    """
    intersection = []
    for i in lst_1:
        if i in lst_2:
            intersection.append(i)
    return intersection

#5.21
def pair(lst_1, lst_2, n):
    """(list of int, list of int, int) -> None
    Print the pairs of numbers in lst_1 and lst_2 that add up to n.
    """
    for i in lst_1:
        if n - i in lst_2:
            print(i, n-i)

#5.22
def pairSum(l, n):
    """(list of int, int) -> None
    Return a pair of indicies in l which refer to integers that add up to n.
    Preconditions: l contains only distinct integers.
    """
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]+l[j] == n:
                print(i, j)

#5.29
def lastfirst(l):
    """(list of str) -> list of [list of str, list of str]
    Return a list containing 2 lists. One list is a list of firstnames.
    the other is a list of lastnames. in the format[First, last]
    Preconditions: l must have strings in the format <Lastname, Firstname>
    """
    first = []
    last = []
    for s in l:
        tmp = s.split(", ")
        first.append(tmp[1])
        last.append(tmp[0])
    return [first, last]

#5.31
def subsetSum(l, n):
    """(list of numbers, number) -> bool
    Return true if there are three numbers that add up to a target.
    Preconditions: len(l) > 2
    """
    
    return any(sum(x) == n for x in combinations(l,3))

#5.33
def mystery(n):
    """(int) -> int
    Return how many times n can be halved using integer division before reaching 1
    """
    return floor(log2(n))

#5.46
def inversions(s):
    """(str) -> int
    Return how many pairs of inversions exist in a string s.
    Preconditions: string contains only uppercase letters from A-Z
    """
    count = 0
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if s[i] > s[j]:#left value greater than right value 
                count += 1
    return count
    
#5.48
def sublist(lst_1, lst_2):
    """(list of objects, list of objects) -> bool
    Return True if lst_1 is a sublist of lst_2,
    otherwise return false.
    """
    tmp = []
    for item in lst_2:
        if item in lst_1:
            tmp.append(item)
    return tmp[:] == lst_1[:]
            
#5.37
def mssl(l):
    """(list of int) -> int
    Returns maximum sum contained as a sublist of elements in list l.
    """
    running_sum = maximum_sum = 0
    for i in l:
        running_sum = max(running_sum + i, 0) #if running sum becomes negative sets to 0
        maximum_sum = max(maximum_sum, running_sum)#compares current max sum with running sum
    return maximum_sum
