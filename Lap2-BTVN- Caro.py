def print_board(board):
    for row in board:
        print(" | ".join(str(cell) for cell in row))
    print("-" * 10)
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
board = [[99, 99, 99] for _ in range(3)]
players = ["X", "O"]
turn = 0
while True:
    print_board(board)
    player = players[turn % 2]
    while True:
        try:
            row, col = map(int, input(f"{player}'s turn (Nhập hàng và cột, cách nhau bởi dấu cách): ").split())
            if board[row][col] != 99:
                print("Ô này đã được chọn, hãy chọn ô khác.")
                continue
            if player == "O" and (row, col) == (0, 0):
                print("Người chơi O không được chọn (0,0), hãy nhập lại.")
                continue
            break
        except (ValueError, IndexError):
            print("Nhập không hợp lệ, hãy nhập lại.")
    board[row][col] = player
    if check_winner(board, player):
        print_board(board)
        print(f"Chúc mừng! {player} đã chiến thắng!")
        break
    if all(board[i][j] != 99 for i in range(3) for j in range(3)):
        print_board(board)
        print("Trò chơi hòa!")
        break
    turn += 1
