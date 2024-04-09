
from collections import Counter
from random import choice
from time import sleep


class game():
    
    def __init__(self):
        
        self.playOn = 'Y'
        self.gameStatus = 4
        self.PlayerAToken = ''
        self.PlayerBToken = ''
        self.gameList = [1,2,3,4,5,6,7,8,9]
        self.whoMove = 'A'
        self.winList = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]

    def welcome(self):
        """
        Print out some ASCII art for landing page
        """        
        print(r"""
          ________________   _________   ______   __________  ______
         /_  __/  _/ ____/  /_  __/   | / ____/  /_  __/ __ \/ ____/
          / /  / // /        / / / /| |/ /        / / / / / / __/   
         / / _/ // /___     / / / ___ / /___     / / / /_/ / /___   
        /_/ /___/\____/    /_/ /_/  |_\____/    /_/  \____/_____/   

                                                                """)
        sleep(3)
        return

    def gamemode(self):
        """Gets input for game mode

        Raises:
            ValueError: returns error if the input isn't 1 or 2
        """
        
        print("Please choose a game mode")
        print("1 <- Play against human")
        print("2 <- Play against the machine")
        while True:
            try:
                self.gametype = int(input('->'))
                if self.gametype not in [1,2]:
                    raise ValueError
            except ValueError:
                print('Incorrect Selection, please select 1 or 2')
            else:
                break
        return
        
    def howabout(self):
        """ Just some good old quotes
        """
        hold = ''' 
        ...Wouldn't you prefer a good game of chess?... 
        '''
        response = '''
        ...How about global thermonuclear war...'''
        print(response)
        sleep(1)
        print(hold)
        sleep(1)

        return

    def createGrid(self):
        """
        Create and display game grid with current moves
        """        
        g = self.gameList
        print(rf"""
            {g[0]}|{g[1]}|{g[2]}
            - - -
            {g[3]}|{g[4]}|{g[5]}
            - - -
            {g[6]}|{g[7]}|{g[8]}
            """)
        sleep(2)
        
        return
    
    
    def settoken(self):
        playerAToken = self.PlayerAToken
        playerBToken = self.PlayerBToken
        """Requests input from player A, checks validity and stores token. Automatically sets Player B to be alternate token

        Raises:
            ValueError: 
        """
        token = ['X', 'O']
        while True:
            try:
                AToken = str(input('Player A: Please select token: X or O?')).upper()
                if AToken not in token:
                    raise ValueError("Invalid input. Please select either 'X' or 'O'.")
                else:
                    break
            except ValueError as e:
                print(e)
        
        self.PlayerAToken = AToken
        self.PlayerBToken = 'O' if self.PlayerAToken == 'X' else 'X'
        print(f'Player A Token:{self.PlayerAToken}')
        sleep(1)
        print(f'Player B Token:{self.PlayerBToken}')
        sleep(1)
        return
            
            
    def wopr(self):
        """Function for computer based play. Returns winning move if one exists else returns a random move from remaining moves.

        Returns:
            Integer: Winning move or random move from remaining play list.
        """        
        gameList = self.gameList
        playerBToken = self.PlayerBToken
        playerAToken =self.PlayerAToken
        winList = self.winList
        
        remaining_play= [i for i,j in enumerate(gameList) if isinstance(j, int)]
        token_position = [i for i, j in enumerate(gameList) if j == playerBToken and j != playerAToken]

        for score_list in winList:
            x = set(score_list).intersection(set(token_position))
            if len(x) == 2:
                movelist = list(set(score_list) - set(x))
                if movelist[0] in remaining_play:
                    move = movelist[0]+1
                    break
                else:
                    move = int(choice(remaining_play))+1
            else:
                move = int(choice(remaining_play))+1
        
        return move
        
        
            
    def move(self):
        """Takes input from users if in 2 player mode and validates as integer and in remaining play list. If in 1 player mode it calls WOPR function.
           Calls status function to check if game is win, draw or continuing.
           Displays gamegrid with all current moves.
           Set next play variable to next player

        Raises:
            ValueError: Checks user input is a valid integer move within the game grid.
            ValueError: Checks user has returned a move that has not already been played.
        """        
        gametype = self.gametype
        gamelist = self.gameList
        PlayerAToken = self.PlayerAToken
        PlayerBToken = self.PlayerBToken
        while True:
            while True:
                try:
                    if gametype == 2 and self.whoMove == 'B':
                        playermove = int(game.wopr(self))
                    else:
                        print(f"Player {self.whoMove}: Select your move")
                        playermove = int(input("->"))
                    if playermove < 1 or playermove > 9:
                        raise ValueError("Please submit valid move between 1 - 9")
                except ValueError as e:
                    print(e)
                else:
                    try:
                        if gamelist[playermove - 1] != playermove:
                            raise ValueError("Someone already has a token here. Try again")
                    except ValueError as f:
                        print(f)
                    else:
                        if self.whoMove == 'A':
                            gamelist[playermove - 1] = PlayerAToken
                            self.whoMove = 'B'
                            break
                        else:
                            gamelist[playermove - 1] = PlayerBToken
                            self.whoMove = 'A'
                            break
            game.status(self)
            game.createGrid(self)
            if self.gameStatus != 4:
                break
            print(f"Player {self.whoMove}: Your Turn")
        return
    
    def status(self):
        """Check whether game should be ended or continued.

        Returns:
            Integer: 1 - Player A Win
                     2 - Player B Win
                     3 - Draw
                     4 - Continue Playing
        """        
        gameList = self.gameList
        winList = self.winList
        playerAToken = self.PlayerAToken
        playerBToken = self.PlayerBToken
        
        def wincheck(token):
            """_summary_

            Args:
                token (Str): X or O as current move token

            Returns:
                Integer: 1 - WIn
                         0 - Lose
            """            
            token = token
            score = [i for i, j in enumerate(gameList) if str(j) == str(token)]
            for x in winList:
                if set(x).issubset(score):
                    return 1
            return 0
        
        def has_integer(lst):
            return any(isinstance(x, int) for x in lst)
        
        a_score = wincheck(playerAToken)
        b_score = wincheck(playerBToken)
        
        if a_score == 1:
            self.gameStatus = 1
        elif b_score == 1:
            self.gameStatus = 2
        elif has_integer(gameList) is False:
            self.gameStatus = 3
        else:
            self.gameStatus = 4
        return
        
    def gameResults(self):
        """
        Prints out the outcome based on status function output
        """        
        outcomes = {
            1 : 'Player A has won the game',
            2 : 'Player B has won the game',
            3 : 'A Strange game, the only way of winning is not to play'
        }
        
        print(outcomes.get(self.gameStatus))
        return
    
    def continuePlay(self):
        """Checks whether user would like to continue playing

        Raises:
            ValueError: Validates that user input is only Y or N

        Returns:
            playOn: Y or N 
        """        
        playOn = self.playOn
        
        print('Would you like to play another game? Y/N')
        while True:
            try:
                playOn = str(input('->')).upper()
                if playOn not in ['Y', 'N']:
                    raise ValueError('Please only return Y or N')
            except ValueError as e:
                print(e)
            else:
                break
            self.playOn = playOn
        return playOn