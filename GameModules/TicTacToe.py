from time import sleep
from collections import Counter


class game():
    
    def __init__(self):
        
        self.playOn = 'Y'
        self.gameStatus = 4
        self.PlayerAToken = ''
        self.PlayerBToken = ''
        self.gameList = [1,2,3,4,5,6,7,8,9]
        self.whoMove = 'A'
        self.winList = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]

    def createGrid(self):
        """Takes the gameList and creates a TicTacToe board from current positions and inputs
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
            
            
    def move(self):
        whoMove = self.whoMove
        gamelist = self.gameList
        PlayerAToken = self.PlayerAToken
        PlayerBToken = self.PlayerBToken
        while True:
            try:
                print(f"Player {self.whoMove}: Select your move")
                playermove = int(input("->"))
                if playermove < 1 or playermove > 9:
                    raise ValueError("Please submit valid move between 1 - 9")
            except ValueError as e:
                print(e)
            else:
                if gamelist[playermove - 1] != playermove:
                    print("Someone already has a token here. Try again")
                if self.whoMove == 'A':
                    gamelist[playermove - 1] = PlayerAToken
                    self.whoMove = 'B'
                else:
                    gamelist[playermove - 1] = PlayerBToken
                    self.whoMove = 'A'
            game.status(self)
            game.createGrid(self)
            if self.gameStatus != 4:
                break
            print(f"Player {self.whoMove}: Your Turn")
        return
    
    def status(self):

        gameList = self.gameList
        winList = self.winList
        playerAToken = self.PlayerAToken
        playerBToken = self.PlayerBToken
        
        def wincheck(token):
            token = token
            score = [i for i, j in enumerate(gameList) if str(j) == str(token)]
            for x in winList:
                if Counter(x) == Counter(score):
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
        
        outcomes = {
            1 : 'Player A has won the game',
            2 : 'Player B has won the game',
            3 : 'A Strange game, the only way of winning is not to play'
        }
        
        print(outcomes.get(self.gameStatus))
        return
    
    def continuePlay(self):
        
        playOn = self.playOn
        
        print('Would you like to play another game? Y/N')
        while True:
            try:
                playOn = str(input('->'))
                if playOn not in ['Y', 'N']:
                    raise ValueError('Please only return Y or N')
            except ValueError as e:
                print(e)
            else:
                break
            self.playOn = playOn
        return playOn