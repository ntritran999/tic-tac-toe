board = ['-' for _ in range(9)]
game_over = False
current_player = 'X'

def display_board():
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print(f'{board[6]}|{board[7]}|{board[8]}')

def handle_turn(player):
    position = int(input('Enter a number 1-9: '))-1
    if board[position]=='-':
        board[position]= current_player
    else: print('Invalid move! You lost your turn.\n')
    display_board()

def flip():
    global current_player
    current_player = 'O' if current_player=='X' else 'X'

def game_state():
    tie()
    win()

def tie():
    global game_over
    if '-' not in board: game_over = True

def win():
    global winner
    if row_win(): winner = row_win()
    elif col_win(): winner = col_win()
    elif diag_win(): winner = diag_win()
    else: winner = None

def row_win():
    global game_over
    row1 = board[0]==board[1]==board[2]!='-'
    row2 = board[3]==board[4]==board[5]!='-'
    row3 = board[6]==board[7]==board[8]!='-'
    if row1 or row2 or row3: game_over = True
    if row1: return board[0]
    if row2: return board[3]
    if row2: return board[6]

def col_win():
    global game_over
    col1 = board[0]==board[3]==board[6]!='-'
    col2 = board[1]==board[4]==board[7]!='-'
    col3 = board[2]==board[5]==board[8]!='-'
    if col1 or col2 or col3: game_over = True
    if col1: return board[0]
    if col2: return board[1]
    if col3: return board[2]

def diag_win():
    global game_over
    diag1 = board[0]==board[4]==board[8]!='-'
    diag2 = board[2]==board[4]==board[6]!='-'
    if diag1 or diag2: game_over = True
    if diag1: return board[0]
    if diag2: return board[2]

'''Main Loop'''
def main():
    print("WELCOME TO 2-PLAYER TIC TAC TOE. X ALWAYS GO FIRST!")
    display_board()
    while not game_over:
        handle_turn(current_player)

        game_state()

        flip()

    if winner in ('X','O'):
        print(f'{winner} WON!')
    else: print('TIE!')
if __name__=='__main__':
    main()
