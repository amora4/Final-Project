import random
import time
import libs

class Player:
    def __init__(self, playernumber):
        self.playernumber = playernumber

    def letterSelection(self, letterSelection):
           self.letterSelection = letterSelection

    def playerMove(self,board):
        # Let the player type in his move.
        move = ' '
        #while move not in '1 2 3 4 5 6 7 8 9'.split()  or not isSpaceFree(board, int(move)):
        while move not in '1 2 3 4 5 6 7 8 9'.split():
            print('')
            print('player ' + self.playernumber + ' what is your next move? (1-9)')
            move = input()
        return int(move)

class Board:
    def __init__(self):
        self.theBoard = [' '] * 10

    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        # top left corner has each number for the play
        print('7  |8  |9')
        print(' ' +  self.theBoard[7] + ' | ' +  self.theBoard[8] + ' | ' +  self.theBoard[9])
        print('   |   |')
        print('-----------')
        print('4  |5  |6')
        print(' ' +  self.theBoard[4] + ' | ' +  self.theBoard[5] + ' | ' +  self.theBoard[6])
        print('   |   |')
        print('-----------')
        print('1  |2  |3')
        print(' ' +  self.theBoard[1] + ' | ' +  self.theBoard[2] + ' | ' +  self.theBoard[3])
        print('   |   |')

    def makeMove(self, letter, move):
        self.theBoard[move] = letter

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True

    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.theBoard[move] == ' '

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.firstPlayer=[]

    def showInstructions(self):
        print('''Instructions:
        This is played with 2 people''')
        time.sleep(2)
        print('''You choose to be X or O''')
        time.sleep(2)
        print('''You can tie in this game \n
        Press enter to continue...''')

    def inputPlayerLetter(self):

        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('player1 choose X or O?')
            letter = input().upper()
        if letter == 'O':
            print('player1 is O')
            print('player2 is X')
            print('')
            # return ['O', 'X']
            self.player1.letterSelection('O')
            self.player2.letterSelection('X')
        elif letter == 'X':
            print('player1 is X')
            print('player2 will be O')
            print('')
            # return ['X', 'O']
            self.player1.letterSelection('X')
            self.player2.letterSelection('O')


    def whoGoesFirst(self):
    # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            print('player2 will go first.')
            self.firstPlayer = self.player2
            return self.player2
        else:
            print('player1 will go first.')
            self.firstPlayer = self.player1
            return self.player1

    def showBoard(self):
            self.board.drawBoard()

    def whoWasFirst(self):
        if self.firstPlayer == self.player1:
            print('player1 was first')
            return self.player1
        else:
            print('player2 was first')
            return self.player2

    def isWinner(self, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board.theBoard[7] == le and self.board.theBoard[8] == le and self.board.theBoard[9] == le) or  # across the top
                (self.board.theBoard[4] == le and self.board.theBoard[5] == le and self.board.theBoard[6] == le) or  # across the middle
                (self.board.theBoard[1] == le and self.board.theBoard[2] == le and self.board.theBoard[3] == le) or  # across the bottom
                (self.board.theBoard[7] == le and self.board.theBoard[4] == le and self.board.theBoard[1] == le) or  # down the left side
                (self.board.theBoard[8] == le and self.board.theBoard[5] == le and self.board.theBoard[2] == le) or  # down the middle
                (self.board.theBoard[9] == le and self.board.theBoard[6] == le and self.board.theBoard[3] == le) or  # down the right side
                (self.board.theBoard[7] == le and self.board.theBoard[5] == le and self.board.theBoard[3] == le) or  # diagonal
                (self.board.theBoard[9] == le and self.board.theBoard[5] == le and self.board.theBoard[1] == le))  # diagonal

    def play(self):
        print('Would you like to view the instructions? (yes/no)')
        if input().lower().startswith('y'):
         self.showInstructions()

        self.inputPlayerLetter()
        #self.showBoard()
        turn = self.whoGoesFirst()

        gameIsPlaying = True
        while gameIsPlaying:
            #print('Inside gameIsPlaying loop')
            if turn == self.player1:
                # Player1s turn.
                #print('Player1s turn')
                self.showBoard() #drawBoard(theBoard)
                move = self.player1.playerMove(self.board) #getPlayer1Move(theBoard)
                #makeMove(theBoard, player1Letter, move)
                #print('player1.letterSelection=',self.player1.letterSelection)
                self.board.makeMove(self.player1.letterSelection,move)

                if self.isWinner(self.player1.letterSelection):
                    self.showBoard()
                    print('Hooray! player1 has won the game!')
                    gameIsPlaying = False
                else:
                    if self.board.isBoardFull():
                        self.showBoard()
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player2'
                turn = self.player2

            elif turn ==  self.player2:
                # Player1s turn.
                #print('Player2s turn')
                self.showBoard() #drawBoard(theBoard)
                move = self.player2.playerMove(self.board) #getPlayer1Move(theBoard)
                #makeMove(theBoard, player1Letter, move)
                #print('player2.letterSelection=',self.player2.letterSelection)
                self.board.makeMove(self.player2.letterSelection,move)

                if self.isWinner(self.player2.letterSelection):
                     self.showBoard()
                     print('Hooray! player2 has won the game!')
                     gameIsPlaying = False
                else:
                     if self.board.isBoardFull():
                         self.showBoard()
                         print('The game is a tie!')
                         break
                     else:
                         turn = 'player1'
                turn = self.player1