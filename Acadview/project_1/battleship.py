#importing randint from random
from random import randint
#empty list
board = []
#loop to add elements to the above empty list"board'
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#Create a random ship location in x,y coordinates
ship_row = random_row(board)
ship_col = random_col(board)
ship2_row = random_row(board)
ship2_col = random_row(board)

if ship_row == ship2_row and ship_col == ship2_col:
    ship_row = random_row(board)

print str(ship_row), str(ship_col)
print ship2_row, ship2_col

print_board(board)
# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col or guess_row == ship2_row and guess_col == ship2_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
    if turn == 3:
        print "Game Over"
    print "Turn", turn + 1
    print_board(board)