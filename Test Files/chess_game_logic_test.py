

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
        possible_moves.append(initial_square_index + 8)
        if can_capture_right == True:
            possible_moves.append(initial_square_index + 9)
        elif can_capture_left == True:
            possible_moves.append(initial_square_index + 7)
        elif first_move == True:
            possible_moves.append(initial_square_index + 16)

    else:
        possible_moves.append(initial_square_index - 8)
        if can_capture_right == True:
            possible_moves.append(initial_square_index - 7)
        elif can_capture_left == True:
            possible_moves.append(initial_square_index - 9)
        elif first_move == True:
            possible_moves.append(initial_square_index - 16)

    promote = False         # add code for determining if promotion is true.        squares_to_edge(top) = 1
    if promote == True:
        pass
        
    squares_to_move_to = []
    for move in possible_moves:
        squares_to_move_to.append(squares_list[move])


    return squares_to_move_to
        


def move_rook():
    pass

def move_knight():
    pass

def move_bishop():
    pass

def move_king():
    pass

def move_queen():
    pass