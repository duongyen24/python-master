board = ["-","-","-",
        "-","-","-",
        "-","-","-",]
def display_board():
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[5],board[6],board[7])    
display_board()

def play_game():
    display_board()

    handle_turn()

def handle_turn():
    position= input("choose from 1 to 9")


#board
#display board
#play
#handle return
#check win
    #check row
    #check columns
    #check diagonals
#check tie
#flip player
