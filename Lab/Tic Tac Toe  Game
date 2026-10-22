board = [" "] * 9

def show():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")

def winner(p):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    return any(all(board[i] == p for i in w) for w in wins)

for turn in range(9):
    show()
    p = "X" if turn % 2 == 0 else "O"
    pos = int(input(f"Player {p}, enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid position! Try again.")
        continue

    board[pos] = p

    if winner(p):
        show()
        print("Player", p, "wins!")
        break
else:
    show()
    print("Draw!")
