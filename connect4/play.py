
def player1(token1,y,board):
    flag=1
    while flag==1:
        a=input("player 1 enter the coloumn(1-7):")
        if a.isdigit():
            if a in "1234567":
                a=int(a)
                a=a-1
                for i in reversed(range(y)):
                    if board[i][a]=="[ ]":
                        board[i][a]="["+token1+"]"
                        flag=0
                        break
def player2(token2,y,board):
    flag=1
    while flag==1:
        a=input("player 2 enter the coloumn(1-7):")
        if a.isdigit(): 
            if a in "1234567": 
                a=int(a)
                a=a-1
                for i in reversed(range(y)):
                    if board[i][a]=="[ ]":
                        board[i][a]="["+token2+"]"
                        flag=0
                        break
  
