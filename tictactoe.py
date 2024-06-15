board = [["-" for _ in range(3)] for _ in range(3)]

player, opponent = 'X', 'O'
winner = False
game_over = False

for move in range(9):
    while True:
        for row in board:
            print(" ".join(row))
        print() 

        row = int(input("Enter row (0, 1, 2): "))
        column = int(input("Enter column (0, 1, 2): "))

        if row not in range(3) or column not in range(3):
            print(f"Invalid input, valid row 0, 1, 2")
            continue
        if board[row][column] not in ['X', 'O']:
            board[row][column] = player
        else:
            print("This place is already taken. try again")
            continue

        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
                print(f"Congratulations {player} you won!")
                winner = True
                game_over = True

        if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
            print(f"Congratulations {player}, you won!")
            winner = True
            game_over = True
            
        if game_over:
            break

        player = 'O' if player == 'X' else 'X'
        break

    if game_over:
        break
        
for row in board:
    print(" ".join(row))

if not winner:
    print("It's a tie!")