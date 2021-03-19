from random import randrange

global board
board = [[(j + 1) + i * 3 for j in range(3)] for i in range(3)]

def DisplayBoard(board):
    '''
    the function accepts one parameter containing the board's current status
    and prints it out to the console
    '''
    for rows in board:

        print('+','-'*7,'+','-'*7,'+','-'*7,'+',sep='')
        print('|',' '*3,rows[0],' '*3,sep='',end='')
        print('|', ' ' * 3, rows[1], ' ' * 3, sep='', end='')
        print('|', ' ' * 3, rows[2], ' ' * 3,'|', sep='')
    print('+', '-' * 7, '+', '-' * 7, '+', '-' * 7, '+', sep='')

def EnterMove(board):
    '''
    the function accepts the board current status, asks the user about their move,
    checks the input and updates the board according to the user's decision
    '''
    while True:
        number = int(input('Enter your move: '))
        if number == -1:
            break
        if number < 1 or number > 9:
            print(number,'is not a valid option')
            continue
        if board[(number-1)//3][(number-1)%3] == 'X' or board[(number-1)//3][(number-1)%3] == 'O':
            print(number,'is already taken')
            continue
        board[(number-1)//3][(number-1)%3] = 'O'
        break


def MakeListOfFreeFields(board):
    '''
    the function browses the board and builds a list of all the free squares;
    the list consists of tuples, while each tuple is a pair of row and column numbers
    '''
    list = []
    for rows in board:
        for value in rows:
            if value == 'X' or value == 'O':
                continue
            list.append((board.index(rows),rows.index(value)))
    #if len(list) == 0: return None
    return list

def VictoryFor(board, sign):
    '''
    the function analyzes the board status in order to check if
    the player using 'O's or 'X's has won the game
    '''
    for rows in board:
        for i in rows:
            if i == sign:
                continue
            break
        else:
            return True
    for column in range(3):
        for row in range(3):
            if board[column][row] == sign:
                continue
            break
        else:
            return True
    for i in range(3):
        if board[i][i] == sign:
            continue
        break
    else:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    return None

def DrawMove(board):
    '''
    the function draws the computer's move and updates the board
    '''
    print('Computers turn:')
    freefields = MakeListOfFreeFields(board)
    number = randrange(len(freefields))
    position= freefields[number]
    board[position[0]][position[1]] = 'X'
    DisplayBoard(board)

if __name__ == '__main__':

    while (VictoryFor(board,'X') or VictoryFor(board,'O')) is not True:
        DrawMove(board)
        if VictoryFor(board,'X'): break
        EnterMove(board)
        DisplayBoard(board)
    else:
        if VictoryFor(board,'X'):
            print('Computer Won')
        if VictoryFor(board,'O'):
            print('You Won!')