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

#winner/tie checking function
def check_win():
    for player in [1,2]:
        #horizontal/vertical
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == player or board[0][i] == board[1][i] == board[2][i] == player:
                return player
        #diagonals
        if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
            return player
        #tie
        if all(board[i][j] != 0 for i in range(3) for j in range(3)):
            return "Tie"
    return None

#play function
def play():
    print("tic tac toe")
    display_board()
    game = True
    turn = 1
    
    while game:
        if turn % 2 == 0:
            player = "O's"
        else:
            player = "X's"
        
        player_input(player)
        display_board()
        
        result = check_win()
        if result:
            if result == "Tie":
               print("It's a Tie!")
            else:
               print(f"Player {result} wins!")
            game = False
        
        turn +=1
        
play()