
############# PART 1 ##############

def info_day(today, weather, temperature):
     print(today, "is a", weather, "day. The temperature is", temperature, "degrees Celsius.")

     #Create a string s below such that print(s) command below
     #prints the exact same message as the above print statement.
     # Once you are done, uncomment the two lines of code below
     #
     s = (today + " is a " + weather + " day. The temperature is " +
          str(temperature) + " degrees Celsius.")
     print(s)

info_day("Saturday", "nice", 29)
info_day("Monday", "so so", 15)

############# PART 2 #############

# Uncomment the 3-4 lines of code starting with def below.
# Run the program. Why does it crash?
# Can you fix it without chaning function call: letter_grade("B")

def letter_grade(grade):
     print("Your grade is", grade)

letter_grade("B")

############# PART 3 #############

# Rewrite the following program so that it computes the average
# in a function called average_of_two. 
# Obtaining the input from the user and printing of the result
# must still be outside of the the function.
#
# Make sure to write DOCSTRINGS for your function, including TYPE CONTRACT.
# Test it by running help(average_of_two) in python shell.

def average_of_two(num1, num2):
     '''(number, number) -> float
     Return the average of two numbers.
     '''
     return (num1 + num2)/2

x=float(input("Give me 1st number: "))
y=float(input("Give me 2nd number: "))
print("The average of", x, "and", y,"is", average_of_two(x,y))

########## Question 1 ######################
def pay(hourly, hours):
     '''(int,int) -> number
     Preconditons: hourly & hours > 0
     Return wage for employee given hourly rate and hours worked.
     '''
     if hours <= 40:
          wage = hours * hourly
     elif 40 < hours <= 60:
          wage = hourly * (40 + (hours - 40)*1.5)
     else:
          wage = hourly * (40 + 20 * 1.5 + (hours - 60) * 2)
     return wage

######### Question 2 ######################
def rps(p1,p2):
     '''(str, str) -> int
     Precondition: p1 & p2 == 'R' Or 'P' Or 'S'
     Return the winner of a rock paper scissors game using integers.
     -1 if player 1 wins, 0 if tie, 1 if player 2 wins.

     '''
     if p1 == p2:
          return 0
     elif( (p1 == 'R' and p2 == 'S') or (p1 == 'P' and p2 == 'R') or
           (p1 == 'S' and p2 == 'P') ):
          return -1
     else:
          return 1
          
