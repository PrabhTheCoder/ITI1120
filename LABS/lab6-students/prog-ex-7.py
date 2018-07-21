def inner_product(l, k):
    """(list of ints, list of ints) -> int
    Return the inner product of the 2 lists.
    """
    answer = 0
    for i in range(len(l)):
        answer += l[i] * k[i]
    return answer
