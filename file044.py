board = []
for i in range(5):
  board.append(['O'] * 5)
def print_board(board_in):
  for row in board:
    print (row)

#NEXT

board = []
for i in range(5):
  board.append(['O'] * 5)
def print_board(board_in):
  for row in board:
    print(" ".join(row))

#NEXT

from random import randint 

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board_in):
  for row in board_in:
    print (" ".join(row))

# Add your code below!

def random_row(board_in):
  return randint(0, len(board_in) - 1)
    
def random_col(board_in):
  return randint(0, len(board_in) - 1)

random_row(board)
random_col(board)

#NEXT

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# Add your code below!


guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

#NEXT

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# Add your code below!

print (ship_row)
print (ship_col)
guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

#NEXT

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))
print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
  print ("Congratulations! You sank my battleship!")

#NEXT

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
  print ("Congratulations! You sank my battleship!")
else:
  print ("You missed my battleship!")
  board[guess_row][guess_col] = "X"
  print (print_board(board))

#NEXT

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)
guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
  print ("Congratulations! You sank my battleship!")
else:
  if guess_row not in range(5) or \
    guess_col not in range(5):
    print ("Oops, that's not even in the ocean.")
  else:
    print ("You missed my battleship!")
    board[guess_row][guess_col] = "X"
  print_board(board)

#NEXT

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)
guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
  print ("Congratulations! You sank my battleship!")   
else:
  if guess_row not in range(5) or \
    guess_col not in range(5):
    print ("Oops, that's not even in the ocean.")
  elif guess_row == "X" and guess_col == "X":
    print ("You guessed that one already.")
  else:
    print ("You missed my battleship!")
    board[guess_row][guess_col] = "X"
  print_board(board)

#NEXT

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print ("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!")   
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    print_board(board)
  
    if turn ==3:
      print ("Game Over")

#NEXT

from random import randint
print ("The indexes of rows and columns are 0-4.")
board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print ("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!") 
    break  
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    print_board(board)
  
    if turn ==3:
      print ("Game Over")