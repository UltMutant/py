import random

def create_board(n):
    # create a board with n-1 rows and n-1 columns
    board = []
    for i in range(n-1):
        row = []
        for j in range(n-1):
            row.append(".")
        board.append(row)
    return board

def print_board(board):
    # print the board
    for row in board:
        print(" ".join(row))

def get_move():
    # get the move from the user
    move = input("Enter a move (row col): ")
    move = move.split()
    row = int(move[0])
    col = int(move[1])
    return row, col

def is_valid_move(row, col, board):
    # check if the move is valid
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return False
    if board[row][col] != ".":
        return False
    return True

def make_move(row, col, board, player):
    # make the move
    board[row][col] = player
    return board

def is_board_full(board):
    # check if the board is full
    for row in board:
        for col in row:
            if col == ".":
                return False
    return True

def get_winner(board):
    # get the winner
    player1 = 0
    player2 = 0
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            if board[i][j] == ".":
                continue
            elif board[i][j] == "1":
                player1 += 1
            elif board[i][j] == "2":
                player2 += 1
    if player1 > player2:
        return "1"
    elif player2 > player1:
        return "2"
    else:
        return "T"

def play_game():
    # play the game
    n = int(input("Enter the size of the board: "))
    board = create_board(n)
    print_board(board)
    player = "1"
    while not is_board_full(board):
        row, col = get_move()
        if not is_valid_move(row, col, board):
            print("Invalid move. Try again.")
            continue
        board = make_move(row, col, board, player)
        print_board(board)
        if player == "1":
            player = "2"
        else:
            player = "1"
    winner = get_winner(board)
    if winner == "T":
        print("Tie!")
    else:
        print("Player " + winner + " wins!")

play_game()