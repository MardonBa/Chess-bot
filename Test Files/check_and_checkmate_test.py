from copy import deepcopy

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
            while square_index % 8 <= 6 and square_index < 55:        # checks is the input square is on the right edge or top edge, then it can't move up right
                square_index += 9
                to_edge += 1


        elif direction == "down":
            while square_index % 8 <= 6 and square_index > 7:        # checks is the input square is on the right edge or bottom edge, then it can't move down right
                square_index -= 7
                to_edge += 1

    
    elif diagonal == "left":
        if direction == "up":
            while square_index % 8 >= 1 and square_index <= 55:
                square_index += 7
                to_edge += 1

        elif direction == "down":
            while square_index % 8 >= 1 and square_index > 7:
                square_index -= 9
                to_edge += 1

    return to_edge


    

def move_pawn(color, initial_square, squares_list, board_status, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved, first_move=True):
    initial_square_index = squares_list.index(initial_square)
    possible_moves = []
    en_passant = None
    potential_board_status = deepcopy(board_status)

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

            if "5" in initial_square:
                if board_status[squares_list[square_index - 8]] == "Black_Pawn":
                    if previous_board_status[squares_list[square_index + 8]] == "Black_Pawn":
                        if board_status[squares_list[square_index + 8]] == "empty":
                            possible_moves.append(new_square)
                            en_passant = "right"
                            
                            

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

            if "5" in initial_square:
                if board_status[squares_list[square_index - 8]] == "Black_Pawn":
                    if previous_board_status[squares_list[square_index + 8]] == "Black_Pawn":
                        if board_status[squares_list[square_index + 8]] == "empty":
                            possible_moves.append(new_square)
                            en_passant = "left"
                
        square_index = squares_list.index(initial_square)
        if first_move == True and board_status[squares_list[square_index + 8]] == "empty":
            if board_status[squares_list[initial_square_index + 16]] == "empty":
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
            if "4" in initial_square:
                if board_status[squares_list[square_index + 8]] == "White_Pawn":
                    if previous_board_status[squares_list[square_index - 8]] == "White_Pawn":
                        if board_status[squares_list[square_index - 8]] == "empty":
                            possible_moves.append(new_square)
                            en_passant = "right"

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
            
            if "4" in initial_square:
                if board_status[squares_list[square_index + 8]] == "White_Pawn":
                    if previous_board_status[squares_list[square_index - 8]] == "White_Pawn":
                        if board_status[squares_list[square_index - 8]] == "empty":
                            possible_moves.append(new_square)
                            en_passant = "left"

        square_index = squares_list.index(initial_square)
        if first_move == True and board_status[squares_list[square_index - 8]] == "empty":
            if board_status[squares_list[initial_square_index - 16]] == "empty":
                possible_moves.append(squares_list[initial_square_index - 16])


    promote = False         # add code for determining if promotion is true.        squares_to_edge(top) = 1
    if promote == True:
        pass
    
    return possible_moves, en_passant
        


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


def move_king(color, initial_square, squares_list, board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved):
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
    
    white_can_castle_right = False
    white_can_castle_left = False
    black_can_castle_right = False
    black_can_castle_left = False

    if color == "White":
        if king_has_moved == False & h_file_rook_has_moved == False:
            if board_status["F1"] == "empty" and board_status["G1"] == "empty":
                    white_can_castle_right = True

            if king_has_moved == False and a_file_rook_has_moved == False:
                if board_status["D1"] == "empty" and board_status["C1"] == "empty" and board_status["B1"] == "empty":
                    white_can_castle_left = True

    elif color == "Black":
        if king_has_moved == False & h_file_rook_has_moved == False:
            if board_status["F8"] == "empty" and board_status["G8"] == "empty":
                    black_can_castle_right = True

            if king_has_moved == False and a_file_rook_has_moved == False:
                if board_status["D8"] == "empty" and board_status["C8"] == "empty" and board_status["B8"] == "empty":
                    black_can_castle_left = True


    if white_can_castle_right == True:
        possible_moves.append(squares_list[square_index + 2])
    if white_can_castle_left == True:
        possible_moves.append(squares_list[square_index - 2])
    if black_can_castle_right == True:
        possible_moves.append(squares_list[square_index + 2])
    if black_can_castle_left == True:
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




def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key
 
    return "key doesn't exist"


def look_for_check (board_status, color_to_move, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved):
    opposite_color = 'White' if color_to_move == 'Black' else 'Black'
    king = 'White_King' if color_to_move == 'White' else 'Black_King'

    king_square = get_key(king, board_status)

    def find_pieces_opposite_color(piece, board_status):
        squares = []
        for key, value in board_status.items():
            if value == piece:
                squares.append(key)
        return squares
    
    ## Code to find possible moves for each piece of the opposite color. If the king_square is in the returned list for any piece, return true, ending the function
    ## Start with pieces with higher probabilities of giving checks first
    queen_squares = find_pieces_opposite_color(f"{opposite_color}_Queen", board_status)
    for square in queen_squares:        ## In case there are queens added to the board via promotion
        queen_moves = move_queen(opposite_color, square, squares_list, board_status)
        for move in queen_moves:
            if king_square == move:
                return True
        
    rook_squares = find_pieces_opposite_color(f"{opposite_color}_Rook", board_status)
    for square in rook_squares:
        rook_moves = move_rook(opposite_color, square, squares_list, board_status)
        for move in rook_moves:
            if king_square == move:
                return True
            
    bishop_squares = find_pieces_opposite_color(f"{opposite_color}_Bishop", board_status)
    for square in bishop_squares:
        bishop_moves = move_bishop(opposite_color, square, squares_list, board_status)
        for move in bishop_moves:
            if king_square == move:
                return True
            
    knight_squares = find_pieces_opposite_color(f"{opposite_color}_Knight", board_status)
    for square in knight_squares:
        knight_moves = move_knight(opposite_color, square, squares_list, board_status)
        for move in knight_moves:
            if king_square == move:
                return True
            
    pawn_squares = find_pieces_opposite_color(f"{opposite_color}_Pawn", board_status)
    for square in pawn_squares:
        if opposite_color == 'Black':
            is_first_move = True if '7' in square else False
        elif opposite_color == 'White':
            is_first_move = True if '2' in square else False
        pawn_moves, en_passant = move_pawn(opposite_color, square, squares_list, board_status, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved,first_move=is_first_move)
        for move in pawn_moves:
            if king_square == move:
                return True
            
    king_squares = find_pieces_opposite_color(f"{opposite_color}_King", board_status)
    for square in king_squares:
        king_moves = move_king(opposite_color, square, squares_list, board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
        for move in king_moves:
            if king_square == move:
                return True
            
    return False        ## Only returns False if none of the previous checks return True
    
    

    
