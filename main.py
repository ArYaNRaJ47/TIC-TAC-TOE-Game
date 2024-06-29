def sum(a,b,c):
    return a+b+c
def board(xchance,zchance):
    zero = 'X' if xchance[0] else('O' if zchance[0] else '0')
    one = 'X' if xchance[1] else('O' if zchance[1] else '1')
    two = 'X' if xchance[2] else('O' if zchance[2] else '2')
    three = 'X' if xchance[3] else('O' if zchance[3] else '3')
    four = 'X' if xchance[4] else('O' if zchance[4] else '4')
    five = 'X' if xchance[5] else('O' if zchance[5] else '5')
    six = 'X' if xchance[6] else('O' if zchance[6] else '6')
    seven = 'X' if xchance[7] else('O' if zchance[7] else '7')
    eight = 'X' if xchance[8] else('O' if zchance[8] else '8')                             
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")


def checkWin(xchance,zchance):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (sum(xchance[win[0]],xchance[win[1]],xchance[win[2]]) == 3):
            print("X won the match")
            board(xchance,zchance)
            return 1
        if (sum(zchance[win[0]],zchance[win[1]],zchance[win[2]]) == 3):
            print("O won the match")
            board(xchance,zchance)
            return 0
    return -1



print("Welcome to Tic Tac Toe")
if __name__ == "__main__": 
    xchance = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
    zchance = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
    turn = 1 # for X chance is 1 and for 0 it's o

    while(True):
        board(xchance,zchance)
        if(turn==1):
            print("X's chance")
            value = int(input("Please enter your move: "))
            xchance[value] = 1
        else:
            print("O's chance")
            value = int(input("Please enter your move: "))
            zchance[value] = 1
        cwin = checkWin(xchance,zchance)
        if(cwin != -1):
            print("Match Over")
            break

    
        turn = 1 - turn
    