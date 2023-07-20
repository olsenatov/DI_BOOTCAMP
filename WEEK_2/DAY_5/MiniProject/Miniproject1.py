


print("TIC TAC TOE")

board = [
    [3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,3],
    [3,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,3],    
    [3,0,2,0,2,0,2,0,1,0,2,0,2,0,2,0,1,0,2,0,2,0,2,0,3],
    [3,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,3],    
    [3,0,2,0,2,0,2,0,1,0,2,0,2,0,2,0,1,0,2,0,2,0,2,0,3],
    [3,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,3],    
    [3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,3] 
       
       
]

def display_board():
  for row in board:
    for pixel in row:
        if pixel == 0:
            print(" ", end='')
        elif pixel == 1:
            print("|", end='')
        elif pixel == 2:
            print("-", end='')
        elif pixel == 3:
            print("*", end='')
        elif pixel == "X":
             print("X", end='')
        elif pixel == "O":
             print("0", end='')
            
        # elif pixel == 4:
        #     print(" ", end='')
        
    print("")
    
display_board()
game = True
turn = 1

def player_input(player, char):
    row = int(input(f"Player {player} enter a row: "))
    column = int(input(f"Player {player} enter a column:"))   
    row_index = 1 + (row - 1) * 2
    column_index = 4 + (column - 1) * 8
    
    if 1 <= row <= 3 and 1 <= column <= 3:
        if board[row_index][column_index] == 0:
            board[row_index][column_index] = char
        else:
            print("Cell is already occupied. Try again.")
            player_input(player, char)
    else:
        print("Invalid row or column. Try again.")
        player_input(player, char)  


def check_win(row, column):
    if turn >= 5:
    # vertical win
       if column == 1 and row == 1 and row == 2 and row == 3:
          print("You win")
       elif column == 2 and row == 1 and row == 2 and row == 3:
        print("You win")
       elif column == 3 and row == 1 and row == 2 and row == 3:
        print("You win")
    # horizontal win
       elif row == 1 and column == 1 and column == 2 and column == 3:
        print("You win")
       elif row == 2 and column == 1 and column == 2 and column == 3:
        print("You win")
       elif row == 3 and column == 1 and column == 2 and column == 3:
        print("You win")
    # diagonal win
       elif row == 1 and column == 1 and row == 2 and column == 2 and row == 3 and column == 3:
        print("You win")
       elif row == 1 and column == 3 and row == 2 and column == 2 and row == 3 and column == 1:
        print("You win") 
    elif turn >= 8:
        print("This is a tie")
    return 



for i in turn:
        player_input("X's", "X")
        display_board()
        player_input("O's", "O")
        display_board()
        turn += 1
check_win()

# play()
         

#if turn >= 0 and turn <=8:
                 
        
    
# def play():
   
    
            

            
        
        
    
