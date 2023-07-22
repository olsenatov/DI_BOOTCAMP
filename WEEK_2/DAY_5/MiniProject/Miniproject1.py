#second attempt, rewriting the code completely - zooming out of pixels in a matrix and making it 3x3 board

#board definition as 3x3 cubes - as a 2D list
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

#displaying function
def display_board():
    for row in board:
        for cell in row:
            if cell == 0:
                print(" ", end='')
            elif cell == 1:
                print("X", end='')
            elif cell == 2:
                print("O", end='')
            print(" | ", end='')
        print("\n" + "-" * 9)

#player input function
def player_input(player):
    while True:
        row = input(f"Player {player}, enter a row(1-3): ")
        column = input(f"Player {player}, enter a column: ")
         
        if row.isdigit() and column.isdigit():
           row, column = int(row), int(column)   
           if 1 <= row <= 3 and 1 <= column <= 3 and board[row - 1][column - 1] == 0:
               board[row - 1][column - 1] = 1 if player == "X's" else 2 
               break
           else: print("invalid. or cell is occupied. try again")
        else:
            print("please, enter a valid number")
            

            