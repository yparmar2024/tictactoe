import random

def run():
    return multiOrAI()

def multiOrAI():
   """
   Initial message which chooses between playing locally or against an AI.
   """
   # Welcome Message.
   print()
   print("Welcome to Tic Tac Toe!")

   # Check for a proper answer.
   validAnswer = False
   while not validAnswer:
       answer = input("Would you like to play against an AI? (Y/N) --> ")
       answer = answer.lower()
       if answer == "y":
           print()
           ticTacToeAI()
           validAnswer = True
       elif answer == "n":
           print()
           ticTacToeMulti()
           validAnswer = True
       else:
           print()
           print("Invalid answer, please write Y or N.\n")

def ticTacToeMulti(move = 0):
   """
   A local game of Tic Tac Toe.
   """
   # Reset board and set up tutorial board.
   board = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]


   tutorialBoard = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
  
   # Provide instructions for the game.
   print("The slots are numbered from 1-9 on the board as shown below.")
   print()
   displayBoard(tutorialBoard)
   print()


   # Loop next move until there's no winner.
   while not checkWinner(board)[0]:
       if move % 2 == 0:
           print("Player 1's Move: ")
           playerMove(board, "X")
           print()
           displayBoard(board)
           print()
           move = move + 1
       else:
           print("Player 2's Move: ")
           playerMove(board, "O")
           print()
           displayBoard(board)
           print()
           move = move + 1


   # Display who win the game.
   if checkWinner(board)[1] == 0:
       print("The game was a tie.")
       print()
   else:
        print("Player " + str(checkWinner(board)[1]) + " wins.")
        print()
  
   # Ask to play again.
   validResponse = False
   while not validResponse:
       playAgain = input("Would you like to play again? (Y/N) --> ")
       playAgain = playAgain.lower()
       if playAgain == "y":
           multiOrAI()
           validResponse = True
       elif playAgain == "n":
           print("Thanks for playing TicTacToe!")
           print()
           validResponse = True
       else:
           print("Invalid response, please write Y or N.")
           print()

def ticTacToeAI(move = 0):
   """
   An AI game of Tic Tac Toe.
   """
   # Reset board and set up tutorial board.
   board = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]


   tutorialBoard = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
  
   # Provide instructions for the game.
   print("The slots are numbered from 1-9 on the board as shown below.")
   print()
   displayBoard(tutorialBoard)
   print()

   # Loop next move until there's no winner.
   while not checkWinner(board)[0]:
       if move % 2 == 0:
           print("Player 1's Move: ")
           playerMove(board, "X")
           print()
           displayBoard(board)
           print()
           move = move + 1
       else:
           print("AI's Move: ")
           aiMove(board, "O")
           print()
           displayBoard(board)
           print()
           move = move + 1


   # Display who win the game.
   if checkWinner(board)[1] == 0:
       print("The game was a tie.")
       print()
   else:
        print("Player " + str(checkWinner(board)[1]) + " wins.")
        print()
  
   # Ask to play again.
   validResponse = False
   while not validResponse:
       playAgain = input("Would you like to play again? (Y/N) --> ")
       playAgain = playAgain.lower()
       if playAgain == "y":
           multiOrAI()
           validResponse = True
       elif playAgain == "n":
           print("Thanks for playing TicTacToe!")
           print()
           validResponse = True
       else:
           print("Invalid response, please write Y or N.")
           print()

def displayBoard(board):
   """
   Displays the board.
   """
   # Display each element and return an new empty line.
   for row in board:
       print(row)
   return ''


def checkWinner(board):
   """
   Checks to see if the board has any winners.
   """
   # Check for horizontal win.
   if board[0][0] == board[0][1] == board[0][2] and board[0][0] == "X":
       return [True, 1]
   elif board[0][0] == board[0][1] == board[0][2] and board[0][0] == "O":
       return [True, 2]
   elif board[1][0] == board[1][1] == board[1][2] and board[1][0] == "X":
       return [True, 1]
   elif board[1][0] == board[1][1] == board[1][2] and board[1][0] == "O":
       return [True, 2]
   elif board[2][0] == board[2][1] == board[2][2] and board[2][0] == "X":
       return [True, 1]
   elif board[2][0] == board[2][1] == board[2][2] and board[2][0] == "O":
       return [True, 2]
  
   # Check for vertical win.
   if board[0][0] == board[1][0] == board[2][0] and board[0][0] == "X":
       return [True, 1]
   elif board[0][0] == board[1][0] == board[2][0] and board[0][0] == "O":
       return [True, 2]
   elif board[0][1] == board[1][1] == board[2][1] and board[0][1] == "X":
       return [True, 1]
   elif board[0][1] == board[1][1] == board[2][1] and board[0][1] == "O":
       return [True, 2]
   elif board[0][2] == board[1][2] == board[2][2] and board[0][2] == "X":
       return [True, 1]
   elif board[0][2] == board[1][2] == board[2][2] and board[0][2] == "O":
       return [True, 2]
  
   # Check for diagonal win.
   if board[0][0] == board[1][1] == board[2][2] and board[0][0] == "X":
       return [True, 1]
   elif board[0][0] == board[1][1] == board[2][2] and board[0][0] == "O":
       return [True, 2]
   elif board[0][2] == board[1][1] == board[2][0] and board[0][2] == "X":
       return [True, 1]
   elif board[0][2] == board[1][1] == board[2][0] and board[0][2] == "O":
       return [True, 2]
  
   # Check to see if the board if full or no win.
   if board[0][0] != " " and board[0][1] != " " and board[0][2] != " " and board[1][0] != " " and board[1][1] != " " and board[1][2] != " " and board[2][0] != " " and board[2][1] != " " and board[2][2] != " ":
       return [True, 0]
   else:
       return [False, 0]

def aiMove(board, symbol):
    """
    Generates an random slot to place the next move for an AI.
    """
    # Set initial variable to make sure the number is a valid space on the board.
    validNumber = False

    # Place symbol accordingly on the board.
    while not validNumber:

        # Generate a random integer.
        if str(random.randint(1, 9)) == "1" and board[0][0] == " ":
           board[0][0] = symbol
           validNumber = True
        elif str(random.randint(1, 9)) == "2" and board[0][1] == " ":
           board[0][1] = symbol
           validNumber = True
        elif str(random.randint(1, 9)) == "3" and board[0][2] == " ":
           board[0][2] = symbol
           validNumber = True
        elif str(random.randint(1, 9)) == "4" and board[1][0] == " ":
           board[1][0] = symbol
           validNumber = True
        elif str(random.randint(1, 9)) == "5" and board[1][1] == " ":
           board[1][1] = symbol
           validNumber = True
        elif str(random.randint(1, 9)) == "6" and board[1][2] == " ":
           board[1][2] = symbol
           validNumber = True
        elif str(random.randint(1, 9)) == "7" and board[2][0] == " ":
           board[2][0] = symbol
           validNumber = True
        elif str(random.randint(1, 9)) == "8" and board[2][1] == " ":
           board[2][1] = symbol
           validNumber = True
        elif str(random.randint(1, 9)) == "9" and board[2][2] == " ":
           board[2][2] = symbol
           validNumber = True
        else:
           # print()
           validNumber = False

def playerMove(board, symbol):
   """
   Allows an player to choose his next move.
   """
   # Set initial variable to make sure the number is a valid space on the board.
   validNumber = False
  
   # Place symbol accordingly on the board.
   while not validNumber:
       # Get number from player.
       nextMove = input("Where would you like to place your symbol? --> ")

       if nextMove == "1" and board[0][0] == " ":
           board[0][0] = symbol
           validNumber = True
       elif nextMove == "2" and board[0][1] == " ":
           board[0][1] = symbol
           validNumber = True
       elif nextMove == "3" and board[0][2] == " ":
           board[0][2] = symbol
           validNumber = True
       elif nextMove == "4" and board[1][0] == " ":
           board[1][0] = symbol
           validNumber = True
       elif nextMove == "5" and board[1][1] == " ":
           board[1][1] = symbol
           validNumber = True
       elif nextMove == "6" and board[1][2] == " ":
           board[1][2] = symbol
           validNumber = True
       elif nextMove == "7" and board[2][0] == " ":
           board[2][0] = symbol
           validNumber = True
       elif nextMove == "8" and board[2][1] == " ":
           board[2][1] = symbol
           validNumber = True
       elif nextMove == "9" and board[2][2] == " ":
           board[2][2] = symbol
           validNumber = True
       else:
           print("This slot is either taken or invalid, please enter a number from 1-9 that's not taken.")
           print()
           validNumber = False

      
# Runs Tic Tac Toe.
run()