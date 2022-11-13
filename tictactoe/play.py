import random
def player1(token1,y,board):
    while True:
        a=random.randint(0,2)
        b=random.randint(0,2)
        if board[a][b]=="[ ]":
            board[a][b]="["+token1+"]"
            break
        
def player2(token2,y,board):
    while True:
        a=random.randint(0,2)
        b=random.randint(0,2)
        if board[a][b]=="[ ]":
            board[a][b]="["+token2+"]"
            break
