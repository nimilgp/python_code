
def disp_board(board):
    a=len(board)
    for i in board:
        a=a-1
        print("")
        print(a+1,end="")
        for j in i:
            print(j,end="")
    print("")
    for j in range(len(board[0])):
        print(" ",j+1,end="")
    print("\n")
