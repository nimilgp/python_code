#import numpy as np
import sys
#The Hindu Mon 16 Mar 20
#human difficulty level:damn hard
#computer difficulty level:breeze
board=[[0,0,0,0,0,0,2,0,0],
       [2,0,0,0,0,0,0,0,0],
       [6,0,0,0,2,8,0,0,0],
       [3,8,4,6,7,2,0,0,0],
       [7,2,6,1,5,9,4,8,3],
       [0,0,0,8,3,4,0,2,0],
       [0,0,0,2,0,0,0,0,0],
       [0,0,2,0,0,0,0,3,0],
       [0,0,0,0,0,0,0,0,2],]
def playable(y,x,num):
    global board
    for i in range(0,9):
        if board[i][x]==num:
            return False
    for j in range(0,9):
        if board[y][j]==num:
            return False
    x_=(x//3)*3
    y_=(y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if board[y_+i][x_+j]==num:
                return False
    return True
def solve():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x]==0:
                for num in range(1,10):
                    if playable(y,x,num):
                        board[y][x]=num
                        solve()
                        board[y][x]=0
                return
    #print("\n",np.matrix(board))
    for row in board:
        print(row)
    sys.exit()
solve()

                
        


            
    
        
