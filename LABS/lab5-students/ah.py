def ah(l, x, y):
    """(list, int, int) -> (int,int)

    Return number of elements in list l between integers x, and y
    (inc x and y if applicable), and the minimum element of l that is between
    x and y (inc x and y if applicable).

    Preconditions: x <= y

    >>>ah([5, 1, -2.5, 10, 13, 8], 2, 11)
    (3,5)
    """
    count = 0
    l.sort()
    for i in l:
        if i < x:
            pass
        elif i > y:
            break
        else:
            if count == 0:
                minimum = i
            else:
                minimum = min(minimum, i)
            count += 1
    return (count, minimum)
