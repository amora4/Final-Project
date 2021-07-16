from TicTacClasses import Game, Player, Board

print('Welcome to Tic Tac Toe!')
print('')
player1 = Player('1')
player2 = Player('2')
game = Game(player1, player2)
game.play()
