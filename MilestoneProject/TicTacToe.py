import random
board = [['#','#','#'],['#','#','#'],['#','#','#']]
player1 = '#'
player2 = '#'
marker = {'X':'O', 'O':'X'}

def print_board():
    '''
    This function prints the board in the console.
    '''
    global board
    print(board[0])
    print(board[1])
    print(board[2])

def player_marker():
    """
    This is function let's Player 1 choose the marker he wants
    :return:
    """
    global player1, player2

    while player1 != 'X' and player1 != 'O':
        player1 = input('Enter the marker ("X","O") for Player 1: ').upper()

    player2 = marker[player1]
    print('Marker for Player 1 is "%s" and marker for Player 2 is "%s"' %(player1,player2))

def choose_first():
    '''
    This function randomly chooses a player to play the first move
    '''
    return random.choice(['Player 1', 'Player 2'])

def place_marker(marker, position):
    '''
    This function places the marker in the mentioned position on the board
    :param marker: Marker of the current player
    :param position: Position choosen by the player to place the marker
    :return: Returns nothing
    '''
    if 0 < position < 4:
        board[0][position-1] = marker
    elif 3 < position < 7:
        board[1][position-4]=marker
    elif 6 < position < 10:
        board[2][position - 7] = marker

def player_choice():
    '''
    This function lets the player input the position where he wants to place the marker
    :return:
    '''
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(int(position)):
        position = input('Choose your next position (1-9): ')
    return int(position)

def win_check(marker):
    '''
    This function checks if the game has been won by the specified marker
    :param marker: Marker against which game win is to be checked
    :return: Returns True if the game is won for the specified marker
    '''
    global board
    return ((board[0][0]==marker and board[0][1]==marker and board[0][2]==marker ) or #top row
    (board[1][0] == marker and board[1][1] == marker and board[1][2] == marker) or  # middle row
    (board[2][0]==marker and board[2][1]==marker and board[2][2]==marker ) or #bottom row
    (board[0][0] == marker and board[1][0] == marker and board[2][0] == marker) or  # first col
    (board[0][1] == marker and board[1][1] == marker and board[2][1] == marker) or  # second col
    (board[0][2] == marker and board[1][2] == marker and board[2][2] == marker) or  # third col
    (board[0][0] == marker and board[1][1] == marker and board[2][2] == marker) or  # diagonal row
    (board[0][2] == marker and board[1][1] == marker and board[2][0] == marker))  # middle row

def full_board_check():
    for i in range(1,9):
        if space_check(i):
            return False
    return True

def space_check(position):
    global board
    if 0 < position < 4:
        return board[0][position-1] == '#'
    elif 3 < position < 7:
        return board[1][position-4] == '#'
    elif 6 < position < 10:
        return board[2][position - 7] == '#'

def play_game():
    global player1, player2
    print('Welcome to Tic Tac Toe game using Python')
    print_board()
    player_marker()
    turn = choose_first()
    print('First player to place the marker is "%s"' %(turn))
    game_on = True
    while game_on:
        if turn == 'Player 1':
            print_board()
            position = player_choice()
            place_marker(player1,position)
            if win_check(player1):
                print('Player 1 has won')
                game_on = False
            else:
                if full_board_check():
                    print_board()
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 2'

        elif turn == 'Player 2':
            print_board()
            position = player_choice()
            place_marker(player2,position)
            if win_check(player2):

                print('Player 2 has won')
                game_on = False
            else:
                if full_board_check():
                    print_board()
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 1'


play_game()
