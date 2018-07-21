#Pythons functions aren't reserved.
def abs(x):
    """(number) -> number

    Return the absolute value of x
    
    >>>abs(0.1)
    0.1
    >>>abs(-1)
    1
    >>>abs(80)
    80
    """
    
    if(x >= 0):
        return x
    else:
        return -x
    
def abs_v2(x):
    """(number) -> number

    Return the absolute value of x
    
    >>>abs(0.1)
    0.1
    >>>abs(-1)
    1
    >>>abs(80)
    80
    """
    
    if x < 0:
        x = -x
    return x

def format_age(age):
    """ (int) -> str

    Return a sentence describing the age.
    """
    if age < 20:
        result = str(age)
    elif age < 30:
        result = "twenty something"
    elif age < 40:
        result = "thirty something"
    elif age < 50:
        result = "fourty something"
    else:
        result = "ancient"

    return result

def letter_grade(grade):
    """ (int) -> str

    Precondition: 0 <= grade <= 100
    
    Return a letter grade corresponding to grade

    >>>letter_grade(20)
    F
    >>>letter_grade(60)
    C
    >>>letter_grade(70)
    B
    >>>letter_grade(80)
    A
    """
    
    if grade < 60:
        letter = 'F'
    elif grade < 70:
        letter = 'C'
    elif grade < 80:
        letter = 'B'
    else:
        letter = 'A'

    return letter

def foo(g1, g2, g3):
    """ (int, int, int)-> bool

    """
    if(g1 >= 50 and g2 >= 50 and g3 >= 50 and (g1 >= 80 or g2 >= 80 or g3 >= 80)):
        return True
    return False

