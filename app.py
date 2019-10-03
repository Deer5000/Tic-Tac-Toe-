def tic_tac_toe():
    board = [1,2,3,4,5,6,7,8,9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    ##win_combinations = (1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))

    def draw():
        print (board[0], board[1], board[2])
        print (board[3], board[4], board[5])
        print (board[6], board[7], board[8])
        print()

    def p1():
        n = choose_number()
        if board[n] == "x" or "X" or board[n]== "o" or "O":
            print("You can't go there. Try again")
            p1()
        else:
            board[n] = "X"

    def p2():
