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
                if count>2:
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
                if count>2:
                    flag=0
                    break
            if flag==0:
                game=False
    if game==False:
        print(var,"won")
        sys.exit()
     

#diagonal check
def diag_check(x,y,board,game):
    if (board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0]) and board[1][1]!="[ ]":
        var=board[1][1]
        game=False

    if game==False:
        print(var,"won")
        sys.exit()
