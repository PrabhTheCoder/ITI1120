import random

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    # YOUR CODE GOES HERE
    print("Shuffling the deck...")
    random.shuffle(deck)
def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    # YOUR CODE GOES HERE

    #creates a list of blank elements
    board = [None] * len(original_board)

    #Note: discovered is a list of indicies as strings where items have been discovered ["0", "1", "2",...]

    #Display items already paired.
    for i in discovered:
        board[int(i)] = original_board[int(i)]
    
    #Display items at p1 and p2 
    
    board[p1-1] = original_board[p1-1]
    board[p2-1] = original_board[p2-1]
    
    #Fill rest of board with dull sides.
    for i in range(len(board)):
        if board[i] == None:
            board[i] = '*'
    print_board(board)

#############################################################################
#   FUNCTIONS FOR OPTION 2 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l): #nlogn
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]
    
    # YOUR CODE GOES HERE
    tmp_list = sorted(l)
    
    #Remove all stars
    cards = count_cards_without_stars(tmp_list)

    #Remove odd numbered cards
    board_string = ''  
    for i in cards:
        repeats = (i[1] // 2) * 2
        if repeats > 0:
            board_string += i[0] * repeats
            
    playable_board = list(board_string)
    
    return playable_board


def is_rigorous(l): #nlogn
    '''list of str->bool
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''
    # YOUR CODE GOES HERE
    tmp = sorted(l) #Make sure list is sorted!
    cards_with_frequency = count_cards_without_stars(tmp)
    for i in cards_with_frequency:
        if i[1] != 2:
            return False
    return True

def count_cards_without_stars(l):
    """(list of str) -> list of list of [str,int]

    Return a list of lists containing the symbol with the
    number of times it appears in list l excluding
    the * symbol.

    Precondition: list l is sorted,
    """

    last_char = ''
    count = 0
    cards_with_frequency = []
    for i in l:
        
        if last_char == i:
            count += 1
        else:
            if '' != last_char != '*':    
                cards_with_frequency.append([last_char, count])
            last_char = i
            count = 1
    if '' != last_char != '*':
        cards_with_frequency.append([last_char, count])
        
    return cards_with_frequency

######################################
#   MISCELLANEOUS HELPER FUNCTIONS   #
######################################
def ascii_name_plaque(name):
    '''(str) -> None
    Display the specified name in an ascii plaque.
    '''
    length = len(name) + 6
    print((length + 2) * '*', '*' + ' ' * length + '*',
    '* __' + name + '__ *', '*' + ' ' * length + '*',
    (length + 2) * '*', sep='\n')

def print_blank_lines(n):
    '''(int) -> None
    Display n blank lines
    '''
    s = "\n" * (n-1)
    print(s)
        
def clear_screen():
    """() -> None
    Clears the screen by spamming blank lines after waiting for user to press
    enter.
    """
    wait_for_player()
    print_blank_lines(45)
    
######################################
    
def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")

    # this is the funciton that plays the game
    # YOUR CODE GOES HERE

    #Variables
    discovered = []
    guess = 0
    length = len(board)
    optimal = length // 2
    expect = int(0.8 * length)
    current_board = ['*']*length
    
    prompt = "Enter two distinct positions on the board that you want" + \
             " revealed.\ni.e two integers in the range [1, " + str(length) + \
             "]"
    
    while len(discovered) != length:
        guess = do_turn_and_update_values(prompt, length, guess, discovered, current_board, board)

    display_game_end_message(optimal, expect, guess)
    
def do_turn_and_update_values(prompt, length, guess, discovered, current_board, board):
    """(str, int, int, list of str, list of str, list of str) -> int

        Returns guess incremented by 1 after processing a valid turn and updating
        values current_board, and discovered to reflect current state of the game.

        Preconditions: length is the length of the board.
    """ 
    doesnotcount = "Please try again. This guess did not count. Your current " + \
               "number of guesses is " + str(guess)

    print_board(current_board)

    print_blank_lines(2)
    print(prompt)
    p1 = int(input("Enter position 1: "))
    p2 = int(input("Enter position 2: "))
    
    while (p1 == p2 or not (1 <= p1 <= length) or not(1 <= p2 <= length)
           or str(p1-1) in discovered or str(p2-1) in discovered):
        if p1 == p2:
            print("You chose the same positions")
        elif not (1 <= p1 <= length) or not(1 <= p2 <= length):
            print("One or both of your chosen positions is out of the range [1,", str(length)
                  + "]")
        else:
            print("One or both of your chosen positions has already been paired.")

        print(doesnotcount)

        print_blank_lines(1)
        print(prompt)
        p1 = int(input("Enter position 1: "))
        p2 = int(input("Enter position 2: "))
        
    print_revealed(discovered, p1, p2, board)
    check_if_discovered(discovered, p1, p2, current_board, board)
    guess += 1
    clear_screen()
    return guess

def check_if_discovered(discovered, p1, p2, current_board, original_board):
    '''(list of str, int, int, list of str, list of str)->None
    Checks for discovery of a pair, updates discovered with
    the indicies if so, and also updates current_board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    if original_board[p1-1] == original_board[p2-1]:
        discovered.append(str(p1-1))
        discovered.append(str(p2-1))
        current_board[p1-1] = original_board[p1-1]
        current_board[p2-1] = original_board[p2-1]

def display_game_end_message(optimal, expected, guess):
    """(int, int, int) -> None
    Displays the end message congratulating the user, and giving how many guesses they did above the optimal and
    how many guesses they had above or below the expected.
    """
    turns = guess - expected
    print("Congratulations! You completed the game with", guess, "guess(es),",
          "that is", guess-optimal, "more than the best possible.",
          "\nIt is also " + str(abs(turns)) * (turns != 0) +
          " less than" * (turns < 0) + " more than" * (turns > 0) +
          " the expected number of turns")

#main
ascii_name_plaque("Welcome to my Concentration game")
print_blank_lines(2)
# YOUR CODE TO GET A CHOICE 1 or CHOCE 2 from a player GOES HERE
print("Would you like (enter 1 or 2 to indicate your choice):",
      "\n(1) me to generate a rigorous deck of cards for you",
      "\n(2) or, would you like me to read a deck from a file?")

choice = input("")

while "1" != choice != "2":
    choice = input(choice + " is not an existing option. Please try again. Enter 1 or 2 to indicate your choice\n")
# YOUR CODE FOR OPTION 1 GOES HERE
# In option 1 somewhere you need to and MUST have a call like this:
# board=create_board(size)
if choice == "1":
    print("You chose to have a rigorous deck generated for you")

    print_blank_lines(1)

    prompt = "How many cards do you want to play with?\nEnter an even" + \
             " number between 2 and 52: "

    size = int(input(prompt))
    
    while size not in range(2, 53, 2):
        print_blank_lines(1)
        size = int(input(prompt))
        
    board = create_board(size)
    shuffle_deck(board)
    print_blank_lines(1)
    clear_screen()
    play_game(board)
# YOUR CODE FOR OPTION 2 GOES HERE    
# In option 2 somewhere you need to and MUST have the following 4 lines of code one after another
#
#print("You chose to load a deck of cards from a file")
#file=input("Enter the name of the file: ")
#file=file.strip()
#board=read_raw_board(file)
#board=clean_up_board(board)
else:
    print("You chose to load a deck of cards from a file")
    file=input("Enter the name of the file: ")
    file=file.strip()
    board=read_raw_board(file)
    board=clean_up_board(board)
    rigorous = is_rigorous(board)
    size = len(board)
    ascii_name_plaque("This deck is now playable" + " and rigorous" * rigorous
                      + " but not rigorous" * (not(rigorous)) + " and it has " +
                      str(size) + " cards.")
    clear_screen()
    shuffle_deck(board)
    clear_screen()
    if size == 0:
        print("The resulting board is empty.",
              "\nPlaying the Concentration game with an empty board is impossible.",
              "\nGood bye.")
    else:
        play_game(board)
        
