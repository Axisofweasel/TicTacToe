from time import sleep
from collections import Counter

def wincheck(token):
    gameList = ['X',1,2,3,'X',5,6,7,'X']
    whoMove = 'A'
    winList = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    token = token
    score = [i for i, j in enumerate(gameList) if str(j) == str(token)]
    for x in winList:
        if Counter(x) == Counter(score):
            return print('win')
    return print('loss')

if __name__ == "__main__":
    wincheck('X')