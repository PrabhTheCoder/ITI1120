import math
#########QUESTION: 1########################
def repeater(s1,s2,n):
    return "_" +(s1+s2) * n + "_"

############Question: 2##############
def roots(a,b,c):
    x1 = (-b + math.sqrt( b ** 2 - 4 * a * c ))/(2 * a)
    x2 = (-b - math.sqrt( b ** 2 - 4 * a * c ))/(2 * a)
    print("The quadratic equation with coefficients a = " + str(a) +
            " b = " + str(b) + " c = " + str(c) + "\nhas the following solutions" +
            " (i.e. roots):\n" + str(x1) + " and " + str(x2))
###########Question: 3###############
def real_roots(a,b,c):
    return b ** 2 - 4 * a * c >= 0
###########Question: 4###############
def reverse(x):
    return (x % 10) * 10 + x//10
