# Course: IT1 1120
# Assignment number: 1
# Family name, Given name: Tara, Sahil
# Student number: 300018569

import math, turtle

########################
# Question 1
########################

def mh2kh(s):
    '''(number) -> number

    Return the speed in kph given mph.

    Preconditions: speed is a non-negative number
    '''
    return s * 1.60934

########################
# Question 2
########################

def pythagorean_pair(a, b):
    '''(int, int) -> bool

    Return whether or not the integers are a pythagorean pair
    '''
    c = math.sqrt( a ** 2 + b ** 2 )
    return c // 1 == c

########################
# Question 3
########################

def in_out(xs, ys, side):
    '''(number, number, number) -> bool

    Return whether or not a point is in the box with a given side length and
    given coordinate of the bottom left corner of the box.
    '''
    x = float(input("Enter a number for the x coordinate of a query point: "))
    y = float(input("Enter a number for the y coordinate of a query point: "))
    return (xs <= x <= xs + side) and (ys <= y <= ys + side)

########################
# Question 4
########################

def safe(n):
    '''(int) -> bool

    Return whether or not a number is safe (doesn't contain a 9 and is not
    divisible by 9)

    Preconditions: n must be a non-negative integer.
    '''
    return not((n % 10 == 9) or (n // 10 == 9) or (n % 9 == 0))

########################
# Question 5
########################

def quote_maker(quote, name, year):
    '''(str, str, int)-> str

    Return a sentence, that contains a specified year, name, and quote.

    Preconditions: Year is a non-negative integer.
    '''
    return ('In ' + str(year) + ', a person called '
            + name + ' said: "' + quote + '"')

########################
# Question 6
########################

def quote_displayer():
    '''(None) -> None

    Display a sentence, that contains a specified year, name, and quote
    fed after a given prompt.

    Preconditions: The year given cannot be a non-negative integer.
    '''
    print(quote_maker(input("Give me a quote: "), input("Who said that? "),
                      input("What year did she/he say that? ")))

########################
# Question 7
########################

def rps_winner():
    '''(None) -> None

    Display the winner of a rock paper scissors game and indicates whether
    or not its a tie.
    '''
    p1 = input("What choice did player 1 make?\n Type one" +
                   " of the following options: rock, paper, scissors: ")
    
    p2 = input("What choice did player 2 make?\n Type one" +
                   " of the following options: rock, paper, scissors: ")
    
    print("Player 1 wins. That is " + str(   (p1 == "rock" and p2 == "scissors")
                                          or (p1 == "paper" and p2 == "rock")
                                          or (p1 == "scissors" and p2 == "paper")
                                            ) +
          "\nIt is a tie. That is not " + str(not(p1 == p2)))
          
             

########################
# Question 8
########################

def fun(x):
    '''(number) -> number

    Return the value of y in the function 10^4y = x+3 given x.
    Preconditions: x is a non-negative number.
    '''
    return math.log10(x+3)/4

########################
# Question 9
########################

def ascii_name_plaque(name):
    '''(str) -> None
    Display the specified name in an ascii plaque.
    '''
    length = len(name) + 6
    print((length + 2) * '*', '*' + ' ' * length + '*',
    '* __' + name + '__ *', '*' + ' ' * length + '*',
    (length + 2) * '*', sep='\n')

########################
# Question 10
########################

def draw_bike():
    '''(None) -> None
    Draw and display a picture of a bike.
    '''
    t = turtle.Turtle()
    t.shape('turtle')
    t.speed('fastest')

    #Draw outer left wheel
    t.penup()
    t.goto(-200,-75)
    t.pendown()
    t.pen(pencolor="gray", pensize=8)
    t.circle(70)
    
    #Draw outer right wheel
    t.penup()
    t.goto(150,-75)
    t.pendown()
    t.pen(pencolor="gray", pensize=8)
    t.circle(70)

    #Draw inner right wheel
    t.pen(fillcolor="gray", pencolor="black", pensize=3)
    t.penup()
    t.goto(150,-20)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    
    #Draw Frame
    t.penup()
    t.pen(pencolor=(0.12, 0.41, 0.6), pensize=10)
    t.goto(-200, 0)
    t.pendown()
    t.left(60)
    t.forward(160)

    t.right(60)
    t.forward(240)

    t.right(90)
    t.forward(100)
    t.left(35)
    t.forward(55)

    t.left(180)
    t.forward(55)
    t.right(35)
    t.forward(100)

    t.left(140)
    t.forward(160)

    t.right(45)
    t.forward(210)
    t.right(180)
    t.forward(210)

    t.left(132)
    t.forward(190)
    t.right(40)
    t.forward(50)

    t.right(180)
    t.forward(50)
    t.left(40)
    t.forward(190)
    t.left(92)
    t.forward(155)
    t.left(40)
    t.forward(50)

    #Draw Handle
    t.pen(pencolor=(0.85, 0.72, 0.74), pensize=13)
    t.left(60)
    t.forward(30)
    t.left(180)
    t.forward(60)

    #Draw Seat
    t.penup()
    t.goto(-125, 195)
    t.pen(pencolor="brown", pensize=13)
    t.pendown()
    t.left(30)
    t.forward(25)
    t.left(180)
    t.forward(50)

    #Draw upper peddle
    t.setheading(0)
    t.pen(pencolor="black", pensize=8)
    t.penup()
    t.goto(15, 15)
    t.pendown()
    t.left(75)
    t.forward(60)
    t.right(90)
    t.pensize(10)
    t.forward(10)
    t.left(180)
    t.forward(20)
    
    #Draw peddles outer circle
    t.setheading(0)
    t.pen(fillcolor="gray", pencolor="black", pensize=3)
    t.penup()
    t.goto(15, 0)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    #Draw peddles inner circle
    t.pen(fillcolor="white", pencolor="black", pensize=3)
    t.penup()
    t.goto(15, 10)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    
    #Draw lower peddle
    t.pen(pencolor="black", pensize=8)
    t.penup()
    t.goto(15, 10)
    t.pendown()
    t.left(255)
    t.forward(40)
    t.right(90)
    t.pensize(10)
    t.forward(10)
    t.left(180)
    t.forward(20)
    
    #Draw inner left wheel
    t.setheading(0)
    t.pen(fillcolor="gray", pencolor="black", pensize=3)
    t.penup()
    t.goto(-200,-20)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

########################
# Question 11
########################

def alogical(n):
    '''(number) -> int

    Return the minimum number of divisions by 2 to be done on n to get a number
    less than or equal to one.

    Preconditions: n >= 1
    '''
    return math.ceil(math.log2(n))

########################
# Question 12
########################

def time_format(h,m):
    '''(int, int) -> str
    Return a message describing the time to the nearest 5th minute.
    Preconditions: h is between 0 and 23 inclusive. is between 0 and 59
    inclusive.
    '''
    m = round(m / 5) * 5

    if m == 60:
        h += 1
        m %= 60

    s = str( (h + (m > 30)) % 24 ) + " o'clock"

    if 0 < m < 30:
        s = str(m) + " minutes past " + s

    elif m == 30:
        s = "half past " + s

    elif m > 30:
        s = str(60 - m) + " minutes to " + s
    
    return s

########################
# Question 13
########################

def cad_cashier(price, payment):
    '''(number, number) -> number

    Return the change to give back to the customer in canadian dollars,
    given a price and the payment they gave.

    Preconditions: price & payment >= 0, payment >= price. 2nd decimal of
    payment must be a 0 or 5.
    '''
    return round( round((payment - price) / 0.05) * 0.05, 2 )

########################
# Question 14
########################

def min_CAD_coins(price, payment):
    '''(number, number) -> (int, int, int, int, int)

    Return the minimum coins in toonies, loonies, quarters, dimes, and nickels
    to give back to the customer as change.
    
    Preconditions: price & payment >= 0, payment >= price. 2nd decimal of
    payment must be a 0 or 5.
    '''
    change = round(cad_cashier(price, payment) * 100)
    return (change // 200, change % 200 // 100, change % 200 % 100 // 25,
            change % 200 % 100 % 25 // 10, change % 200 % 100 % 25 % 10 // 5)

