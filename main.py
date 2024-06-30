def board(xchance, zchance):
    symbols = ['X' if xchance[i] else 'O' if zchance[i] else str(i) for i in range(9)]
    for i in range(0, 9, 3):
        print(f"{symbols[i]} | {symbols[i+1]} | {symbols[i+2]}")
        if i < 6:
            print("--|---|--")

def checkWin(xchance, zchance):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xchance[i] for i in win) == 3:
            print("X won the match")
            return 1
        if sum(zchance[i] for i in win) == 3:
            print("O won the match")
            return 0
    return -1

def is_draw(xchance, zchance):
    return all(xchance[i] or zchance[i] for i in range(9))

print("Welcome to Tic Tac Toe")
if __name__ == "__main__":
    xchance = [0] * 9
    zchance = [0] * 9
    turn = 1 

    while True:
        board(xchance, zchance)
        print("X's chance" if turn == 1 else "O's chance")
        
        try:
            value = int(input("Please enter your move (0-8): "))
            if value < 0 or value > 8 or xchance[value] or zchance[value]:
                print("Invalid move! Please try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 8.")
            continue
        
        if turn == 1:
            xchance[value] = 1
        else:
            zchance[value] = 1
        
        cwin = checkWin(xchance, zchance)
        if cwin != -1:
            board(xchance, zchance)
            print("Match Over")
            break

        if is_draw(xchance, zchance):
            board(xchance, zchance)
            print("The game is a draw!")
            break

        turn = 1 - turn
