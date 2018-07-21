# Course: IT1 1120
# Assignment number: 2
# Family name, Given name: Tara, Sahil
# Student number: 300018569

import math
import random

########################
# Ascii name plaque
########################
def ascii_name_plaque(name):
    '''(str) -> None
    Display the specified name in an ascii plaque.
    '''
    length = len(name) + 6
    print('\n' + (length + 2) * '*', '*' + ' ' * length + '*',
    '* __' + name + '__ *', '*' + ' ' * length + '*',
    (length + 2) * '*', sep='\n')

########################
# Primary School Quiz
########################
def primary_school_quiz(flag, n):
    '''(int, int) -> int

        Preconditions: n is a positive integer, flag = 0 or flag = 1.
        
        Generates n math questions for the pupil either subtraction or exponentiation depending on flag, which after answering all n questions
        returns amount of questions answered correctly.
    '''
    correct = 0
    if flag == 0:
        for i in range(n):
            print("Question", str(i + 1) + ":")
            numOne = random.randint(0,9)
            numTwo = random.randint(0,9)
            their_answer = int(input("What is the result of " + str(numOne) + "-" + str(numTwo) + "? "))
            if their_answer == (numOne - numTwo):
                correct += 1
    else:
        for i in range(n):
            print("Question", str(i + 1) + ":")
            numOne = random.randint(0,9)
            numTwo = random.randint(0,9)
            their_answer = int(input("What is the result of " + str(numOne) + "^" + str(numTwo) + "? "))
            if their_answer == (numOne ** numTwo):
                correct += 1
    return correct

#############################
# High school equation solver
#############################
def high_school_eqsolver(a,b,c):
    """ (number, number, number) -> None

        Displays the solution for a quadratic equation given the coefficients
        a, b and c. (Can also solve linear equations)
    """
    if a == 0:
        if b == 0 and c != 0:
            print("The linear equation " + str(b) + "*x + " + str(c) + " = 0")
            print("is satisfied for no number x")
        elif b == 0 and c == 0:
            print("The quadratic equation " + str(a) + "*x^2 + " + str(b) + "*x + " +
                  str(c) + " = 0")
            print("is satisifed for all numbers x")
        else:
            print("The linear equation " + str(b) + "*x + " + str(c) + " = 0")
            print("has the solution:", -c/b)
    else:
        print("The quadratic equation " + str(a) + "*x^2 + " + str(b) + "*x + " +
              str(c) + " = 0")
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            print("has the following real roots:", "\n" + 
                  str((-b + math.sqrt(discriminant))/(2 * a)), "and",
                  (-b - math.sqrt(discriminant))/(2 * a))
        elif discriminant == 0:
            print("has only one solution, a real root:", "\n"+ str(-b/(2*a)))
        else:
            print("has the following two complex roots:",
                  "\n" + str(-b/(2*a)) +  " + " + str(math.sqrt(-discriminant)/(2*a)) + " i",
                  "\nand",
                  "\n" + str(-b/(2*a)) +  " - " + str(math.sqrt(-discriminant)/(2*a)) + " i")             

########################
# Main
########################

ascii_name_plaque("Welcome to my math quiz-generator / equation-solver")

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")

if status=='1':
    ascii_name_plaque(name + ", welcome to my quiz-generator for primary school students.")
    flag = int(input("\What would you like to practice? Enter\n"+
                     "0 for subtraction\n" + 
                     "1 for exponentiation"))
    n = int(input("How many questions would you like to practice? "))
    if n > 0: 
        percentage = (primary_school_quiz(flag, n)/n) * 100
        if percentage >= 90:
            print("/nCongratulations", name, "You’ll probably get an A tomorrow.",
            "Now go eat your dinner and go to sleep.")
        elif percentage >= 70:
            print("/nYou did well", name, "but I know you can do better.")
        else:
            print("/nI think you need some more practice", name + ".")
    else:
        print("A non positive number of questions eh? Hmm...", name, "you must be too tired.")
elif status=='2':

    ascii_name_plaque("quadratic equation, a*x^2 + b*x + c=0, solver for " + name)
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        question = question.strip().casefold()

        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            a = float(input("Enter a number for the coefficient a: "))
            b = float(input("Enter a number for the coefficient b: "))
            c = float(input("Enter a number for the coefficient c: "))
            high_school_eqsolver(a,b,c)
 
else:
    print(name, "you are not a target audience for this software.")

print("Good bye "+name+"!")
