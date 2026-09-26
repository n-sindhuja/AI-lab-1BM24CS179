import random
board = [['-' for _ in range(3)] for _ in range(3)]
def show_board():
    for row in board:
        print(" ".join(row))
def is_full():
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False
    return True
def has_won(player):
    for i in range(3):
        if (board[i][0] == player and
            board[i][1] == player and
            board[i][2] == player):
            return True
    for j in range(3):
        if (board[0][j] == player and
            board[1][j] == player and
            board[2][j] == player):
            return True
    if (board[0][0] == player and
        board[1][1] == player and
        board[2][2] == player):
        return True
    if (board[0][2] == player and
        board[1][1] == player and
        board[2][0] == player):
        return True
    return False
def start_game():
    player = random.choice(['X', 'O'])
    print("Player", player, "starts!")
    while True:
        print("\nCurrent Board:")
        show_board()
        print("\nPlayer", player)
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1
        if row < 0 or row >= 3 or col < 0 or col >= 3:
            print("Invalid position!")
            continue
        if board[row][col] != '-':
            print("Position already occupied!")
            continue
        board[row][col] = player
        if has_won(player):
            show_board()
            print("Player", player, "wins!")
            break
        if is_full():
            show_board()
            print("Game is a draw!")
            break
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
start_game()
