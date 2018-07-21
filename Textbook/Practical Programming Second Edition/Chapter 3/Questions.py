############################
#       QUESTION 3
############################

def triple(n):
    """(number) -> number

    Return n tripled

    >>> triple(0)
    0
    >>> triple(-3)
    -9
    >>> triple(5)
    15
    >>> triple(0.1)
    0.3
    """
    
    return n*3

############################
#       QUESTION 4
############################

def absolute_difference(n1,n2):
    """(number, number) -> number

    Return absolute value difference between n1 and n2

    >>> absolute_difference(-1, 3)
    4
    >>> absolute_difference(1,-3)
    4
    >>> absolute_difference(-5,-6)
    1
    >>> absolute_difference(0, 111)
    111
    >>> absolute_difference(111,111)
    0
    >>> absolute_difference(100, 10)
    90
    """
    
    return abs(n1-n2)

############################
#       QUESTION 5
############################

def km2mi(d):
    """(number) -> number

    Precondition: d >= 0
    
    Return the distance d in miles from kilometers

    >>> km2mi(3)
    1.875
    >>> km2mi(5)
    3.125
    >>> km2mi(0)
    0.0
    """
    
    return d/1.6

############################
#       QUESTION 6
############################
        

def grade_average(first, second, third):
    """(number, number, number) -> number

    Precondition: 0 <= first, second, third <= 100

    Return the average of three grades.

    >>>grade_average(100, 100, 100)
    100.0
    >>>grade_average(0, 100, 50)
    50.0
    >>>grade_average(92, 100, 92.5)
    94.83333333333333
    """
    
    return (first + second + third)/3

############################
#       QUESTION 7
############################

def best_grade_average(g1, g2, g3, g4):
    """(number,number,number,number) -> number

    Precondition: 0 <= g1, g2, g3, g4 <= 100
    
    Return the average of the best three grades

    >>>best_grade_average(0,100,100,100)
    100.0
    >>>best_grade_average(20,100,0,50)
    56.666666666666666
    >>>best_grade_average(99,92,100,96)
    98.333333333333333
    """
    
    return max( grade_average(g1, g2, g3), grade_average(g1, g2, g4),
                grade_average(g1, g3, g4), grade_average(g2, g3, g4) )

############################
#       QUESTION 8
############################

def weeks_elapsed(day1, day2):
    """ (int, int) -> int

    day1 and day2 are days in the same year. return the number of
    full weeks that elabsed between the two_days.

    """
