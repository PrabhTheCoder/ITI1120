# Course: IT1 1120
# Assignment number: 2
# Family name, Given name: Tara, Sahil
# Student number: 300018569

########################
# Question 1
########################
def min_enclosing_rectangle(radius, x, y):
    """(number, number, number) -> (number, number) or None

        Preconditions: radius >= 0
        
        Return the x and y of the bottom left corner of the rectangle
        enclosing a circle with a radius of radius and centered about x, y.
        If radius is negative returns nothing.
    """
    if radius >= 0:
        return(x-radius, y-radius)
    
########################
# Question 2
########################
def series_sum():
    """(None) -> number or None

    Preconditions: n given by user is a non negative integer
    
    Return the sum of the series 1000 + (1/1)^2 + (1/2)^2 + (1/3)^2 (1/n)^2.
    if entered number is negative returns nothing.
    """
    n = int(input("Please enter a non-negative integer: "))
    sumer = 1000
    if n >= 0:
        for i in range(1, n + 1):
            sumer += 1/i ** 2
        return sumer
            
########################
# Question 3
########################
def pell(n):
    """(int) -> int or None

        Preconditions: n >= 0:
        
        Returns nth pell number if n >= 0 returns nothing otherwise.
    """
    if n >= 0:
        second_last = 0
        last = 1
        answer = 0
        if n == 0:
            answer = 0
        elif n == 1:
            answer = 1
        elif n > 1:
            for i in range(2, n + 1):
                answer = 2 * last + second_last
                if i < n:
                    second_last = last
                    last = answer
        return answer
########################
# Question 4
########################
def countMembers(s):
    """(str) -> int

        Returns the number of extraordinary characters within a string.
        Extraordinary numbers are:
        F to X upper cased letters,
        e to j lower cased,
        Numerals between 2 and 6,
        "!",
        ",",
        and "\".
    """
    num = 0
    for ch in s:
        if ch in "FGHIJKLMNOPQRSTUVWXefghij23456!\\,":
            num += 1
    return num

########################
# Question 5
########################
def casual_number(s):
    """(str) -> int or None
    Return nothing if s is not a number.
    Return comma-less integer from s if s is a number.
    """
    s = s.replace(",", "")
    if s[1:].isnumeric():
        return int(s)

########################
# Question 6
########################
def alienNumbers(s):
    """(str) -> int
        Return the alien number for a string s where T=1024,y=598,!=121, a=42, N=6, U=1
    """
    return s.count("T") * 1024 + s.count("y") * 598 + s.count("!") * 121 + s.count("a") * 42 +  s.count("N") * 6 + s.count("U")

########################
# Question 7
########################
def alienNumbersAgain(s):
    """(str) -> int
        Return the alien number for a string s where T=1024,y=598,!=121, a=42, N=6, U=1 without the use of string functions.
    """
    num = 0
    for ch in s:
        if ch == "T":
            num += 1024
        elif ch == "y":
            num += 598
        elif ch == "!":
            num += 121
        elif ch == "a":
            num += 42
        elif ch == "N":
            num += 6
        elif ch == "U":
            num += 1
    return num

########################
# Question 8
########################
def encrypt(s):
    """(str) -> str
    Returns an encrypted version of s.
    """
    s = s[::-1]
    encrypted = ""
    length = len(s)
    if length <= 1:
        encrypted = s
    else:
        for i in range(length // 2):
            encrypted += s[i] + s[length - i - 1]
        if length % 2 != 0:
            encrypted += s[length // 2]
    return encrypted

########################
# Question 9
########################
def oPify(s):
    """(str) -> str
    Returns a string with the letters o and p between
    consecutive characters. If the first letter is a capital
    the o is capitalized, if not the o is lower case. If
    the second letter is capitalized the p is capitalized,
    if not the p is lower case.
    """
    oped = ""
    num = 1
    if len(s) > 1:
        for ch in s:
            if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if num > 1:
                    if s[num-2].isalpha():
                        oped += "P" + ch
                    else:
                        oped += ch
                    if num != len(s) and s[num].isalpha():
                        oped += "O"
                elif s[num].isalpha():
                    oped += ch + "O"
                else:
                    oped += ch
            elif ch in "abcdefghijklmnopqrstuvwxyz":
                if num > 1:
                    if s[num-2].isalpha():
                        oped += "p" + ch
                    else:
                        oped += ch
                    if num != len(s) and s[num].isalpha():
                        oped += "o"
                elif s[num].isalpha():
                    oped += ch + "o"
                else:
                    oped += ch
            else:
                oped += ch
            num += 1
    else:
        oped = s
    return oped

########################
# Question 10
########################
def nonrepetitive(s):
    """(str) -> bool
    Preconditions: s does not contain spaces.
    Returns whether or not any substring in s repeats consecutively.
    """
    length = len(s)
    state = True
    for i in range(length):
        for j in range(i,length):
            s1 = s[i:j].strip()
            s2 = s[j:2*j - i].strip()
            if s1 == s2 and s1 != "" != s2:
                state = False
            
    return state
