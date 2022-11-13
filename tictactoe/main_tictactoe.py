import display_board
import check
import play

game=True

board=[["[ ]","[ ]","[ ]"],
       ["[ ]","[ ]","[ ]"],
       ["[ ]","[ ]","[ ]"],]

y=len(board)
x=len(board[0])

token1="#"
token2="$"
       
    
def gameloop():
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

gameloop()
