import display_board
import check
import play

game=True

board=[["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
       ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
       ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
       ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
       ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
       ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],]

y=len(board)
x=len(board[0])
while True:
    token1=input("player 1 enter your choice of Token(only 1 chr):")
    if len(token1)==1:
        break
while True:
    token2=input("player 2 enter your choice of Token(only 1 chr):")
    if len(token2)==1:
        break
display_board.disp_board(board)    
while game==True:
    play.player1(token1,y,board)
    display_board.disp_board(board)
    check.ver_check(x,y,board,game)
    check.hor_check(x,y,board,game)
    check.diag_check(x,y,board,game)
    play.player2(token2,y,board)
    display_board.disp_board(board)
    check.ver_check(x,y,board,game)
    check.hor_check(x,y,board,game)
    check.diag_check(x,y,board,game)


