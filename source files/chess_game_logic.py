

def squares_to_edge(squares_list, initial_square, direction, diagonal=None):     # diagonal should be paired with up or down with direction, should be right or left
    # direction should be up, down, left, right
    to_edge = 0

    square_index = squares_list.index(initial_square)
    if diagonal == None:
        if direction == "up":
            while square_index <= 55:
                square_index += 8
                to_edge += 1
                    
            to_edge = square_index

        elif direction == "down":
            while square_index >= 8:
                square_index -= 8
                to_edge += 1
                
            to_edge = square_index

        elif direction == "right":
            to_edge = (square_index + 1) % 8

        elif direction == "left":
            to_edge = square_index % 8



    elif diagonal == "right":
        if direction == "up":
            while square_index % 8 <= 6 & square_index <= 55:        # checks is the input square is on the right edge or top edge, then it can't move up right
                square_index += 9
                to_edge += 1


        elif direction == "down":
            while square_index % 8 <= 6 & square_index >= 7:        # checks is the input square is on the right edge or bottom edge, then it can't move down right
                square_index -= 7
                to_edge += 1

    
    elif diagonal == "left":
        if direction == "up":
            while square_index % 8 >= 1 & square_index <= 55:
                square_index += 7
                to_edge += 1

        elif direction == "down":
            while square_index % 8 >= 1 & square_index >= 7:
                square_index -= 9
                to_edge += 1


    

def move_pawn(color, initial_square, squares_list, first_move=False, can_capture_right=False, can_capture_left=False, en_passant=False):
    initial_square_index = squares_list.index(initial_square)
    possible_moves = []

    if color == "white":
        if squares_to_edge(squares_list, initial_square, "up") != 0:
            possible_moves.append(squares_list[initial_square_index + 8])

            if can_capture_right == True & squares_to_edge(squares_list, initial_square, "right") != 0:
                possible_moves.append(squares_list[initial_square_index + 9])

            elif can_capture_left == True & squares_to_edge(squares_list, initial_square, "left") != 0:
                possible_moves.append(squares_list[initial_square_index + 7])

            elif first_move == True:
                possible_moves.append(squares_list[initial_square_index + 16])


    elif color == "black":
        if squares_to_edge(squares_list, initial_square, "down") != 0:
            possible_moves.append(squares_list[initial_square_index - 8])

            if can_capture_right == True & squares_to_edge(squares_list, initial_square, "right") != 0:
                possible_moves.append(squares_list[initial_square_index - 7])

            elif can_capture_left == True & squares_to_edge(squares_list, initial_square, "left") != 0:
                possible_moves.append(squares_list[initial_square_index - 9])

            elif first_move == True:
                possible_moves.append(squares_list[initial_square_index - 16])


    promote = False         # add code for determining if promotion is true.        squares_to_edge(top) = 1
    if promote == True:
        pass


    return possible_moves
        


def move_rook(initial_square, squares_list, first_move=True):
    possible_moves = []

    square_index = squares_list.index(initial_square)
    moves_up = squares_to_edge(squares_list, initial_square, "top")
    while moves_up > 0:
        square_index += 8
        possible_moves.append(squares_list[square_index])
        moves_up -= 1


    square_index = squares_list.index(initial_square)
    moves_down = squares_to_edge(squares_list, initial_square, "down")
    while moves_down > 0:
        square_index -= 8
        possible_moves.append(squares_list[square_index])
        moves_down -= 1


    square_index = squares_list.index(initial_square)
    moves_right = squares_to_edge(squares_list, initial_square, "right")
    while moves_right > 0:
        square_index += 1
        possible_moves.append(squares_list[square_index])
        moves_right -= 1


    square_index = squares_list.index(initial_square)
    moves_left = squares_list(squares_list, initial_square, "left")
    while moves_left > 0:   
        square_index -= 1
        possible_moves.append(squares_list[square_index])
        moves_left -= 1


    # add code for castling

    return possible_moves



def move_knight(initial_square, squares_list):
    possible_moves = []

    square_index = squares_list.index(initial_square)
    new_square_index = 0
    squares_up = squares_to_edge("up")
    squares_right = squares_to_edge("right")
    squares_down = squares_to_edge("down")
    squares_left = squares_to_edge("left")

    if squares_up >= 2 and squares_right >= 1:
        new_square_index = square_index + 17
        possible_moves.append(squares_list[new_square_index])

    elif squares_right >= 2 and squares_up >= 1:
        new_square_index = square_index + 10
        possible_moves.append(squares_list[new_square_index])

    elif squares_right >= 2 and squares_down >= 1:
        new_square_index = square_index - 6
        possible_moves.append(squares_list[new_square_index])

    elif squares_down >= 2 and squares_right >= 1:
        new_square_index = square_index - 15
        possible_moves.append(squares_list[new_square_index])

    elif squares_down >= 2 and squares_left >= 1:
        new_square_index = square_index - 17
        possible_moves.append(squares_list[new_square_index])
    
    elif squares_left >= 2 and squares_down >= 1:
        new_square_index = square_index - 10
        possible_moves.append(squares_list[new_square_index])

    elif squares_left >= 2 and squares_up >= 1:
        new_square_index = square_index + 6
        possible_moves.append(squares_list[new_square_index])

    elif squares_up >= 2 and squares_left >= 1:
        new_square_index = square_index + 15
        possible_moves.append(squares_list[new_square_index])

    
    return possible_moves
    
        

def move_bishop(initial_square, squares_list):
    possible_moves = []

    square_index = squares_list.index(initial_square)
    moves_up_right = squares_to_edge(squares_list, initial_square, "up", "right")
    while moves_up_right > 0:
        square_index += 9
        possible_moves.append(squares_list[square_index])
        moves_up_right -= 1

    
    square_index = squares_list.index(initial_square)
    moves_up_left = squares_to_edge(squares_list, initial_square, "up", "left")
    while moves_up_left > 0:
        square_index += 7
        possible_moves.append(squares_list[square_index])
        move_up_left -= 1


    square_index = squares_list.index(initial_square)
    moves_down_right = squares_to_edge(squares_list, initial_square, "down", "right")
    while moves_down_right > 0:
        square_index -= 7
        possible_moves.append(squares_list, initial_square, "down", "right")
        moves_down_right -= 1


    square_index = squares_list.index(initial_square)
    moves_down_left = squares_to_edge(squares_list, initial_square, "down", "left")
    while moves_down_left > 0:
        square_index -= 9
        possible_moves.append(squares_list[square_index])
        moves_down_left -= 1


    return possible_moves


def move_king(initial_square, squares_list, first_move=True):
    possible_moves = []

    # horizontal and vertical king moves
    square_index = squares_list.index(initial_square)
    moves_up = squares_to_edge(squares_list, initial_square, "top")
    if moves_up != 0:
        square_index += 8
        possible_moves.append(squares_list[square_index])


    square_index = squares_list.index(initial_square)
    moves_down = squares_to_edge(squares_list, initial_square, "down")
    if moves_down != 0:
        square_index -= 8
        possible_moves.append(squares_list[square_index])


    square_index = squares_list.index(initial_square)
    moves_right = squares_to_edge(squares_list, initial_square, "right")
    if moves_right != 0:
        square_index += 1
        possible_moves.append(squares_list[square_index])


    square_index = squares_list.index(initial_square)
    moves_left = squares_list(squares_list, initial_square, "left")
    if moves_left != 0:   
        square_index -= 1
        possible_moves.append(squares_list[square_index])


    # diagonal king moves
    square_index = squares_list.index(initial_square)
    moves_up_right = squares_to_edge(squares_list, initial_square, "up", "right")
    if moves_up_right != 0:
        square_index += 9
        possible_moves.append(squares_list[square_index])

    
    square_index = squares_list.index(initial_square)
    moves_up_left = squares_to_edge(squares_list, initial_square, "up", "left")
    if moves_up_left != 0:
        square_index += 7
        possible_moves.append(squares_list[square_index])


    square_index = squares_list.index(initial_square)
    moves_down_right = squares_to_edge(squares_list, initial_square, "down", "right")
    if moves_down_right != 0:
        square_index -= 7
        possible_moves.append(squares_list, initial_square, "down", "right")


    square_index = squares_list.index(initial_square)
    moves_down_left = squares_to_edge(squares_list, initial_square, "down", "left")
    if moves_down_left != 0:
        square_index -= 9
        possible_moves.append(squares_list[square_index])

    # add code for castling
    # add code for check/checkmate (after all code for move restrictions, call each function for all pieces on the possible_moves list, and remove any squares returned by the other functions from possible_moves. If none remain, checkmate = True)

    return possible_moves

def move_queen(initial_square, squares_list):
    possible_moves = []

    # horizontal and vertical queen moves
    square_index = squares_list.index(initial_square)
    moves_up = squares_to_edge(squares_list, initial_square, "top")
    while moves_up > 0:
        square_index += 8
        possible_moves.append(squares_list[square_index])
        moves_up -= 1


    square_index = squares_list.index(initial_square)
    moves_down = squares_to_edge(squares_list, initial_square, "down")
    while moves_down > 0:
        square_index -= 8
        possible_moves.append(squares_list[square_index])
        moves_down -= 1


    square_index = squares_list.index(initial_square)
    moves_right = squares_to_edge(squares_list, initial_square, "right")
    while moves_right > 0:
        square_index += 1
        possible_moves.append(squares_list[square_index])
        moves_right -= 1


    square_index = squares_list.index(initial_square)
    moves_left = squares_list(squares_list, initial_square, "left")
    while moves_left > 0:   
        square_index -= 1
        possible_moves.append(squares_list[square_index])
        moves_left -= 1

    # diagonal queen moves
    square_index = squares_list.index(initial_square)
    moves_up_right = squares_to_edge(squares_list, initial_square, "up", "right")
    while moves_up_right > 0:
        square_index += 9
        possible_moves.append(squares_list[square_index])
        moves_up_right -= 1

    
    square_index = squares_list.index(initial_square)
    moves_up_left = squares_to_edge(squares_list, initial_square, "up", "left")
    while moves_up_left > 0:
        square_index += 7
        possible_moves.append(squares_list[square_index])
        move_up_left -= 1


    square_index = squares_list.index(initial_square)
    moves_down_right = squares_to_edge(squares_list, initial_square, "down", "right")
    while moves_down_right > 0:
        square_index -= 7
        possible_moves.append(squares_list, initial_square, "down", "right")
        moves_down_right -= 1


    square_index = squares_list.index(initial_square)
    moves_down_left = squares_to_edge(squares_list, initial_square, "down", "left")
    while moves_down_left > 0:
        square_index -= 9
        possible_moves.append(squares_list[square_index])
        moves_down_left -= 1


    return possible_moves