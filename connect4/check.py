import sys
#vertical check
def ver_check(x,y,board,game):
    flag=1
    for i in range(x):
        if flag==1:
            count=0
            var=board[0][i]
            for j in range(y):
                if board[j][i]!=var:
                    var=board[j][i]
                    count=1
                elif board[j][i]==var and var!="[ ]":
                    count+=1
                if count>3:
                    flag=0
                    break
            if flag==0:
                game=False
    if game==False:
        print(var,"won")
        sys.exit()
#horizontal check
def hor_check(x,y,board,game):
    flag=1
    for i in range(y):
        if flag==1:
            var=board[i][0]
            count=0
            for j in range(x):
                if board[i][j]!=var:
                    var=board[i][j]
                    count=1
                elif board[i][j]==var and var!="[ ]":
                    count+=1
                if count>3:
                    flag=0
                    break
            if flag==0:
                game=False
    if game==False:
        print(var,"won")
        sys.exit()
     

#diagonal check
def diag_check(x,y,board,game):
    flag=1
    for i in range(3,y):
        if flag==1:
            for j in range(0,4):
                if board[i][j]==board[i-1][j+1]==board[i-2][j+2]==board[i-3][j+3] and board[i][j]!="[ ]" :
                    game=False
                    var=board[i][j]
                    flag=0

    for i in range(3,y):
        if flag==1:
            for j in range(6,2,-1):
                if board[i][j]==board[i-1][j-1]==board[i-2][j-2]==board[i-3][j-3] and board[i][j]!="[ ]":
                    game=False
                    var=board[i][j]
                    flag=0

    if game==False:
        print(var,"won")
        sys.exit()
        
