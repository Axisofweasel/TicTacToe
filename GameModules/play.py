from TicTacToe import game
import Welcome


while True:

    current_game = game()
    
    current_game.welcome()
    
    current_game.gamemode()
    
    current_game.howabout()

    current_game.settoken()

    status = 4

    current_game.createGrid()
    
    current_game.move()

    current_game.gameResults()

    if current_game.continuePlay() != 'Y':
        break
    