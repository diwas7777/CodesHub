board=[" " for i in range(9)]



def print_board():
    row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def move(icon):
    if icon=="X":
        number=1
    elif icon=="O":
        number=2
    print(("your turn player {} ").format(number))
    choice=int(input("Enter the move number 1-9 ").strip())
    if board[choice-1]==" ":
        board[choice-1]=icon
    else:
        print()
        print("Block already occupied ")


def will_win(icon):
    if(board[0]==icon and board[1]==icon and board[2]==icon) or\
      (board[4]==icon and board[5]==icon and board[6]==icon) or\
      (board[7]==icon and board[8]==icon and board[9]==icon) or\
      (board[0]==icon and board[3]==icon and board[6]==icon) or\
      (board[1]==icon and board[4]==icon and board[7]==icon) or\
      (board[2]==icon and board[5]==icon and board[8]==icon) or\
      (board[0]==icon and board[4]==icon and board[8]==icon) or\
      (board[2]==icon and board[4]==icon and board[6]==icon):
      return True
    else:
        return False 

def is_draw(icon):
    if " " not in board:
        return True
    else:
        return False    


while True:
    print_board()
    move("X")
    print_board()
    if will_win("X"):
        print_board()
        print("Player 1 won ! congratulations")
        break
    elif is_draw("X"):
        print("the match is a draw ! ! ")
        break
    move("O")
    print_board()
    if will_win("O"):
        print_board()
        print("Player 2 won ! congratulations")
        break
    elif is_draw("O"):
        print("the match is a draw ! ! ")
        break

