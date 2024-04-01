from time import sleep


def welcome():
    print(r"""
  ________________   _________   ______   __________  ______
 /_  __/  _/ ____/  /_  __/   | / ____/  /_  __/ __ \/ ____/
  / /  / // /        / / / /| |/ /        / / / / / / __/   
 / / _/ // /___     / / / ___ / /___     / / / /_/ / /___   
/_/ /___/\____/    /_/ /_/  |_\____/    /_/  \____/_____/   
                                                            """)
    sleep(3)
    return


def gamemode():
    """Gets input for game mode

    Raises:
        ValueError: returns error if the input isn't 1 or 2
    """
    print("Please choose a game mode")
    print("1 <- Play against human")
    print("2 <- Play against the machine")
    while True:
        try:
            result = int(input('->'))
            if result not in [1,2]:
                raise ValueError
        except ValueError:
            print('Incorrect Selection, please select 1 or 2')
        else:
            break
    return
    result
    

def howabout():
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


if __name__ == "__main__":
    howabout()
