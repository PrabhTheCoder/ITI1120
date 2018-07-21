##for i in range(10,0,-1):
##    print(i)
##print("Blast off!")

#while CONDITION:
#    statement(s)
##program continues

from random import randint

def guessing_game():
    rand = randint(1,1000)
    tries = 10
    guess = -1
    while guess != rand and tries > 0:
        guess = int( input("Try and guess: ") )
        if guess < rand:
            print("TOO LOW!!!")
        elif guess > rand:
            print("TOO HIGH!!!")
    if guess == rand:
        print("You Win")
    else:
        print("You are not a very good guesser\n", "Go read up on binary search")

guessing_game()


###n/(2**q) < 1
###q > 1 + log_2 n
###20 for 1 and 1 million.




###Collatz conjecture
##def collatz(n):
##    while n > 1:
##        #print(n)
##        if n % 2 == 0: #even
##            n //= 2
##        else: #odd
##            n = 3 * n + 1
##    return True
##for i in range(1,1000001):
##    collatz(i)





##answer = input("Yes or No, would you like to buy the ticket? ").strip().casefold()
##while "yes" != answer != "no":
##    print("incorrect input. Please answer Yes or No")
##    answer = input("Yes or No, would you like to buy the ticket? ").strip().casefold()



def print_vowels(s):
    for i in range(len(s)):
        if s[i] in "aeiouAEIOU":
            print(s[i])

def print_until_first_vowel(s):
    i = 0
    while i < len(s) and s[i] not in "aeiouAEIOU":
        print(s[i])
        i += 1

def print_vowel_occurance(s):
    print("a e i o u")
    print(*map(s.strip().casefold().count, "aeiou"))


















##i = 10
##
##while i > 0:
##    print(i)
##    i -= 1
##print("Blast off!")



