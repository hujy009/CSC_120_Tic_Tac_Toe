board = [ ["-" for i in range(3)] for j in range(3)]


def print_board():
    print("Printing board now ...")
    
    for e in board:
        print(e)



def isValid(row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        print(f"the row or col is out of the range. Pleae select in [0, 1, 2]")
        return False
    if board[row][col] != '-':
        print(f"---board[{row}][{col}] has been selected. Please reselect somewhere else on the board---")
        return False
    return True


def mark_board(player, row, col):
    if player ==  1:
        board[row][col] = 'X'
    if player == 2:
        board[row][col] = 'O'

    for e in board:
        if '-' in e:
            return -1
    
    return player
    

  
if __name__ == "__main__":
    num = 0      
player = 1
while True:
    if num % 2 == 0:
        player = 1
    else:
        player = 2
    print_board()
    
    print(f"\nPlayer {player}, place a mark on the board")
    row = int(input("Enter row number between 0 (inclusive), 2(inclusive)"))
    col = int(input("Enter col number between 0 (inclusive), 2(inclusive)"))

    if not isValid(row, col):
        print("---Invalid input choice. Please mark again!---")
        continue
    
    whoWin = mark_board(player, row, col)
    if whoWin == 1:
        print(" Player 1 wins! Game Over!")
        break
    elif whoWin == 2:
        print(" Player 2 wins! Game Over!")
        break

    num = num + 1