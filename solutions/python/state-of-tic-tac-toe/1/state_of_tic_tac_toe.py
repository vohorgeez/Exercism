def gamestate(board):
    count_X = 0
    count_O = 0
    draw = True
    for line in board:
        for case in line:
            if case == 'X':
                count_X += 1
            elif case == 'O':
                count_O +=1
            elif case == ' ':
                draw = False
    
    wrong_turn_order_X = ((count_X - count_O) >= 2)
    wrong_turn_order_O = (count_O > count_X)

    wins = [(board[0][0] == board[0][1] == board[0][2] != " "), #ligne 1
            (board[1][0] == board[1][1] == board[1][2] != " "), #ligne 2
            (board[2][0] == board[2][1] == board[2][2] != " "), #ligne 3
            (board[0][0] == board[1][0] == board[2][0] != " "), #colonne 1
            (board[0][1] == board[1][1] == board[2][1] != " "), #colonne 2
            (board[0][2] == board[1][2] == board[2][2] != " "), #colonne 3
            (board[0][0] == board[1][1] == board[2][2] != " "), #diagonale 1
            (board[0][2] == board[1][1] == board[2][0] != " ")] #diagonale 2
    
    win = False

    for position in wins:
        if position:
            win = True
    
    impossible = True if (wins.count(True) > 1) else False
    
    if impossible:
        indices = [i for i, x in enumerate(wins) if x == True]
        for cursor in indices:
            if cursor in range(0, 3):
                for checked in indices:
                    if checked == cursor:
                        pass
                    elif checked not in range(0, 3):
                        impossible = False
                    else:
                        impossible = True
                        break
            elif cursor in range(3,6):
                for checked in indices:
                    if checked == cursor:
                        pass
                    elif checked not in range(3, 6):
                        impossible = False
                    else:
                        impossible = True
                        break
            elif cursor in range(6, 8):
                for checked in indices:
                    if checked == cursor:
                        pass
                    elif checked in range(6,8):
                        impossible = False


    ongoing = (not win) and (not draw) and (not wrong_turn_order_X) and (not wrong_turn_order_O)
    
    if wrong_turn_order_X:
        raise ValueError("Wrong turn order: X went twice")
    elif wrong_turn_order_O:
        raise ValueError("Wrong turn order: O started")
    elif impossible:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if win:
        return "win"
    elif draw:
        return "draw"
    elif ongoing:
        return "ongoing"