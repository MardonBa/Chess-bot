

def squares_to_edge(squares_list, initial_square, direction, diagonal=None):     # diagonal should be paired with up or down with direction, should be right or left
    # direction should be up, down, left, right
    to_edge = 0

    square_index = squares_list.index(initial_square)
    if diagonal == None:
        if direction == "up":
            while square_index <= 55:
                square_index += 8
                to_edge += 1
                    

        elif direction == "down":
            while square_index >= 8:
                square_index -= 8
                to_edge += 1
                

        elif direction == "right":
            if ((square_index + 1) % 8) != 0:
                to_edge = 8 - ((square_index + 1) % 8)
            else:
                to_edge = 0       # accounts for edge cases

        elif direction == "left":
            to_edge = square_index % 8



    elif diagonal == "right":
        if direction == "up":
            while square_index % 8 <= 6 and square_index <= 55:        # checks is the input square is on the right edge or top edge, then it can't move up right
                square_index += 9
                to_edge += 1


        elif direction == "down":
            while square_index % 8 <= 6 and square_index >= 7:        # checks is the input square is on the right edge or bottom edge, then it can't move down right
                square_index -= 7
                to_edge += 1

    
    elif diagonal == "left":
        if direction == "up":
            while square_index % 8 >= 1 and square_index <= 55:
                square_index += 7
                to_edge += 1

        elif direction == "down":
            while square_index % 8 >= 1 and square_index >= 7:
                square_index -= 9
                to_edge += 1

    return to_edge


    

def move_pawn(color, initial_square, squares_list, board_status, first_move=True, en_passant=False):
    initial_square_index = squares_list.index(initial_square)
    possible_moves = []

    if color == "White":
        while True:
            if squares_to_edge(squares_list, initial_square, "up") != 0:
                if board_status[squares_list[initial_square_index + 8]] == "empty":
                    possible_moves.append(squares_list[initial_square_index + 8])
                    break
                else: break

        square_index = squares_list.index(initial_square)
        moves_up_right = squares_to_edge(squares_list, initial_square, "up", "right")
        if moves_up_right > 0:
            while True:
                square_index += 9
                new_square = squares_list[square_index]
                if board_status[new_square] == "empty":
                    break
                elif board_status[new_square] != "empty":
                    if color in board_status[new_square]:
                        break
                    else:
                        possible_moves.append(new_square)
                        break
        square_index = squares_list.index(initial_square)
        moves_up_left = squares_to_edge(squares_list, initial_square, "up", "left")
        if moves_up_left > 0:
            while True:
                square_index += 7
                new_square = squares_list[square_index]
                if board_status[new_square] == "empty":
                    break
                elif board_status[new_square] != "empty":
                    if color in board_status[new_square]:
                        break
                    else:
                        possible_moves.append(new_square)
                        break

        if first_move == True:
            possible_moves.append(squares_list[initial_square_index + 16])


    elif color == "Black":
        while True:
            if squares_to_edge(squares_list, initial_square, "up") != 0:
                if board_status[squares_list[initial_square_index - 8]] == "empty":
                    possible_moves.append(squares_list[initial_square_index - 8])
                    break
                else: break

        square_index = squares_list.index(initial_square)
        moves_down_right = squares_to_edge(squares_list, initial_square, "up", "right")
        if moves_down_right > 0:
            while True:
                square_index -= 7
                new_square = squares_list[square_index]
                if board_status[new_square] == "empty":
                    break
                elif board_status[new_square] != "empty":
                    if color in board_status[new_square]:
                        break
                    else:
                        possible_moves.append(new_square)
                        break
        square_index = squares_list.index(initial_square)
        moves_down_left = squares_to_edge(squares_list, initial_square, "up", "left")
        if moves_down_left > 0:
            while True:
                square_index -= 9
                new_square = squares_list[square_index]
                if board_status[new_square] == "empty":
                    break
                elif board_status[new_square] != "empty":
                    if color in board_status[new_square]:
                        break
                    else:
                        possible_moves.append(new_square)
                        break

        if first_move == True:
            possible_moves.append(squares_list[initial_square_index - 16])


    promote = False         # add code for determining if promotion is true.        squares_to_edge(top) = 1
    if promote == True:
        pass


    return possible_moves
        


def move_rook(color, initial_square, squares_list, board_status):
    possible_moves = []

    square_index = squares_list.index(initial_square)
    moves_up = squares_to_edge(squares_list, initial_square, "up")
    while moves_up > 0:
        square_index += 8
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_up -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break



    square_index = squares_list.index(initial_square)
    moves_down = squares_to_edge(squares_list, initial_square, "down")
    while moves_down > 0:
        square_index -= 8
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_down -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break


    square_index = squares_list.index(initial_square)
    moves_right = squares_to_edge(squares_list, initial_square, "right")
    while moves_right > 0:
        square_index += 1
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_right -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break



    square_index = squares_list.index(initial_square)
    moves_left = squares_to_edge(squares_list, initial_square, "left")
    while moves_left > 0:   
        square_index -= 1
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_left -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break


    # add code for castling

    return possible_moves



def move_knight(color, initial_square, squares_list, board_status):
    possible_moves = []

    square_index = squares_list.index(initial_square)
    new_square_index = 0
    squares_up = squares_to_edge(squares_list, initial_square, "up")
    squares_right = squares_to_edge(squares_list, initial_square, "right")
    squares_down = squares_to_edge(squares_list, initial_square, "down")
    squares_left = squares_to_edge(squares_list, initial_square, "left")

    while True:
        if squares_up >= 2 and squares_right >= 1:
            new_square_index = square_index + 17
            new_square = squares_list[new_square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break

    while True:
        if squares_right >= 2 and squares_up >= 1:
            new_square_index = square_index + 10
            new_square = squares_list[new_square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break

    while True:
        if squares_right >= 2 and squares_down >= 1:
            new_square_index = square_index - 6
            new_square = squares_list[new_square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break

    while True:
        if squares_down >= 2 and squares_right >= 1:
            new_square_index = square_index - 15
            new_square = squares_list[new_square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break

    while True:
        if squares_down >= 2 and squares_left >= 1:
            new_square_index = square_index - 17
            new_square = squares_list[new_square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break

    while True:
        if squares_left >= 2 and squares_down >= 1:
            new_square_index = square_index - 10
            new_square = squares_list[new_square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break

    while True:
        if squares_left >= 2 and squares_up >= 1:
            new_square_index = square_index + 6
            new_square = squares_list[new_square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break

    while True:
        if squares_up >= 2 and squares_left >= 1:
            new_square_index = square_index + 15
            new_square = squares_list[new_square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break

    
    return possible_moves
    
        

def move_bishop(color, initial_square, squares_list, board_status):
    possible_moves = []

    square_index = squares_list.index(initial_square)
    moves_up_right = squares_to_edge(squares_list, initial_square, "up", "right")
    while moves_up_right > 0:
        square_index += 9
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_up_right -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break

    
    square_index = squares_list.index(initial_square)
    moves_up_left = squares_to_edge(squares_list, initial_square, "up", "left")
    while moves_up_left > 0:
        square_index += 7
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_up_left -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break


    square_index = squares_list.index(initial_square)
    moves_down_right = squares_to_edge(squares_list, initial_square, "down", "right")
    while moves_down_right > 0:
        square_index -= 7
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_down_right -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break


    square_index = squares_list.index(initial_square)
    moves_down_left = squares_to_edge(squares_list, initial_square, "down", "left")
    while moves_down_left > 0:
        square_index -= 9
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_down_left -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break


    return possible_moves


def move_king(color, initial_square, squares_list, board_status, can_castle_right=False, can_castle_left=False):
    possible_moves = []

    # horizontal and vertical king moves
    square_index = squares_list.index(initial_square)
    moves_up = squares_to_edge(squares_list, initial_square, "up")
    while True:
        if moves_up != 0:
            square_index += 8
            new_square = squares_list[square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break


    square_index = squares_list.index(initial_square)
    moves_down = squares_to_edge(squares_list, initial_square, "down")
    while True:
        if moves_down != 0:
            square_index -= 8
            new_square = squares_list[square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break


    square_index = squares_list.index(initial_square)
    moves_right = squares_to_edge(squares_list, initial_square, "right")
    while True:
        if moves_right != 0:
            square_index += 1
            new_square = squares_list[square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break


    square_index = squares_list.index(initial_square)
    moves_left = squares_to_edge(squares_list, initial_square, "left")
    while True:
        if moves_left != 0:   
            square_index -= 1
            new_square = squares_list[square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break


    # diagonal king moves
    square_index = squares_list.index(initial_square)
    moves_up_right = squares_to_edge(squares_list, initial_square, "up", "right")
    while True:
        if moves_up_right != 0:
            square_index += 9
            new_square = squares_list[square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break

    
    square_index = squares_list.index(initial_square)
    moves_up_left = squares_to_edge(squares_list, initial_square, "up", "left")
    while True:
        if moves_up_left != 0:
            square_index += 7
            new_square = squares_list[square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break


    square_index = squares_list.index(initial_square)
    moves_down_right = squares_to_edge(squares_list, initial_square, "down", "right")
    while True:
        if moves_down_right != 0:
            square_index -= 7
            new_square = squares_list[square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break


    square_index = squares_list.index(initial_square)
    moves_down_left = squares_to_edge(squares_list, initial_square, "down", "left")
    while True:
        if moves_down_left != 0:
            square_index -= 9
            new_square = squares_list[square_index]
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break
        else: break

    square_index = squares_list.index(initial_square)
    if can_castle_right == True:
        possible_moves.append(squares_list[square_index + 2])
    if can_castle_left == True:
        possible_moves.append(squares_list[square_index - 2])
    
            
    return possible_moves

    # add code for check/checkmate (after all code for move restrictions, call each function for all pieces on the possible_moves list, and remove any squares returned by the other functions from possible_moves. If none remain, checkmate = True)



def move_queen(color, initial_square, squares_list, board_status):
    possible_moves = []

    # horizontal and vertical queen moves
    square_index = squares_list.index(initial_square)
    moves_up = squares_to_edge(squares_list, initial_square, "up")
    while moves_up > 0:
        square_index += 8
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_up -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break


    square_index = squares_list.index(initial_square)
    moves_down = squares_to_edge(squares_list, initial_square, "down")
    while moves_down > 0:
        square_index -= 8
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_down -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break


    square_index = squares_list.index(initial_square)
    moves_right = squares_to_edge(squares_list, initial_square, "right")
    while moves_right > 0:
        square_index += 1
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_right -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break


    square_index = squares_list.index(initial_square)
    moves_left = squares_to_edge(squares_list, initial_square, "left")
    while moves_left > 0:   
        square_index -= 1
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_left -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break

    # diagonal queen moves
    square_index = squares_list.index(initial_square)
    moves_up_right = squares_to_edge(squares_list, initial_square, "up", "right")
    while moves_up_right > 0:
        square_index += 9
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_up_right -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break

    
    square_index = squares_list.index(initial_square)
    moves_up_left = squares_to_edge(squares_list, initial_square, "up", "left")
    while moves_up_left > 0:
        square_index += 7
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_up_left -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break


    square_index = squares_list.index(initial_square)
    moves_down_right = squares_to_edge(squares_list, initial_square, "down", "right")
    while moves_down_right > 0:
        square_index -= 7
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_down_right -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break


    square_index = squares_list.index(initial_square)
    moves_down_left = squares_to_edge(squares_list, initial_square, "down", "left")
    while moves_down_left > 0:
        square_index -= 9
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            possible_moves.append(new_square)
            moves_down_left -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                possible_moves.append(new_square)
                break


    return possible_moves