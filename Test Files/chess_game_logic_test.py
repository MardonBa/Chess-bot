from check_and_checkmate_test import look_for_check
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


    

def move_pawn(color, initial_square, squares_list, board_status, previous_board_status,  king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved, first_move=True):
    initial_square_index = squares_list.index(initial_square)
    possible_moves = []
    en_passant = None
    potential_board_status = deepcopy(board_status)

    if color == "White":
        while True:
            if squares_to_edge(squares_list, initial_square, "up") != 0:
                if board_status[squares_list[initial_square_index + 8]] == "empty":
                    potential_board_status[initial_square] = "empty"
                    potential_board_status[squares_list[initial_square_index + 8]] = f"{color}_Pawn"
                    move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                    potential_board_status = deepcopy(board_status)         ## resets it to be used again
                    if (move_causes_check == False):
                        possible_moves.append(squares_list[initial_square_index + 8])
                        break
                    else: break ## Does nothing because check is true
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
                        potential_board_status[initial_square] = "empty"
                        potential_board_status[new_square] = f"{color}_Pawn"
                        move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                        potential_board_status = deepcopy(board_status)
                        if (move_causes_check == False):
                            possible_moves.append(new_square)
                            break
                        else: break
                                

            if "5" in initial_square:
                if board_status[squares_list[square_index - 8]] == "Black_Pawn":
                    if previous_board_status[squares_list[square_index + 8]] == "Black_Pawn":
                        if board_status[squares_list[square_index + 8]] == "empty":
                            potential_board_status[initial_square] = "empty"
                            potential_board_status[squares_list[square_index + 8]] = f"{color}_Pawn"
                            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                            potential_board_status = deepcopy(board_status)
                            if (move_causes_check == False):
                                possible_moves.append(new_square)
                                en_passant = "right"
                            ## no need for an else statement (no loop)
                                    
                            

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
                        potential_board_status[initial_square] = "empty"
                        potential_board_status[new_square] = f"{color}_Pawn"
                        move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                        potential_board_status = deepcopy(board_status)
                        if (move_causes_check == False):
                            possible_moves.append(new_square)
                            break
                        else: break

            if "5" in initial_square:
                if board_status[squares_list[square_index - 8]] == "Black_Pawn":
                    if previous_board_status[squares_list[square_index + 8]] == "Black_Pawn":
                        if board_status[squares_list[square_index + 8]] == "empty":
                            potential_board_status[initial_square] = "empty"
                            potential_board_status[squares_list[square_index + 8]] = f"{color}_Pawn"
                            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                            potential_board_status = deepcopy(board_status)
                            if (move_causes_check == False):
                                possible_moves.append(new_square)
                                en_passant = "left"
                            ## no need for an else statement (no loop)
                

        if first_move == True and board_status[squares_list[square_index + 8]] == "empty":
            if board_status[squares_list[initial_square_index + 16]] == "empty":
                potential_board_status[initial_square] = "empty"
                potential_board_status[squares_list[initial_square_index + 16]] = f"{color}_Pawn"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(squares_list[initial_square_index + 16])
                ## no need for an else statement (no loop)


    elif color == "Black":
        while True:
            if squares_to_edge(squares_list, initial_square, "up") != 0:
                if board_status[squares_list[initial_square_index - 8]] == "empty":
                    potential_board_status[initial_square] = "empty"
                    potential_board_status[squares_list[initial_square_index - 8]] = f"{color}_Pawn"
                    move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                    potential_board_status = deepcopy(board_status)
                    if (move_causes_check == False):
                        possible_moves.append(squares_list[initial_square_index - 8])
                        break
                    else: break
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
                        potential_board_status[initial_square] = "empty"
                        potential_board_status[new_square] = f"{color}_Pawn"
                        move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                        potential_board_status = deepcopy(board_status)
                        if (move_causes_check == False):
                            possible_moves.append(new_square)
                            break
                        else: break

            if "4" in initial_square:
                if board_status[squares_list[square_index + 8]] == "White_Pawn":
                    if previous_board_status[squares_list[square_index - 8]] == "White_Pawn":
                        if board_status[squares_list[square_index - 8]] == "empty":
                            potential_board_status = "empty"
                            potential_board_status[squares_list[square_index - 8]] = f"{color}_Pawn"
                            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                            potential_board_status = deepcopy(board_status)
                            if (move_causes_check == False):
                                possible_moves.append(new_square)
                                en_passant = "right"
                            ## no need for an else statement (no loop)

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
                        potential_board_status[initial_square] = "empty"
                        potential_board_status[new_square] = f"{color}_Pawn"
                        move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                        potential_board_status = deepcopy(board_status)
                        if (move_causes_check == False):
                            possible_moves.append(new_square)
                            break
                        else: break
            
            if "4" in initial_square:
                if board_status[squares_list[square_index + 8]] == "White_Pawn":
                    if previous_board_status[squares_list[square_index - 8]] == "White_Pawn":
                        if board_status[squares_list[square_index - 8]] == "empty":
                            move_causes_check = look_for_check(board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                            if (move_causes_check == False):
                                possible_moves.append(new_square)
                                en_passant = "left"
                            

        if first_move == True and board_status[squares_list[square_index - 8]] == "empty":
            if board_status[squares_list[initial_square_index - 16]] == "empty":
                potential_board_status[initial_square] = "empty"
                potential_board_status[squares_list[initial_square_index - 16]] = f"{color}_Pawn"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(squares_list[initial_square_index - 16])
                ## no need for an else statement (no loop)

    
    return possible_moves, en_passant
        


def move_rook(color, initial_square, squares_list, board_status, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved):
    possible_moves = []
    potential_board_status = deepcopy(board_status)

    square_index = squares_list.index(initial_square)
    moves_up = squares_to_edge(squares_list, initial_square, "up")
    while moves_up > 0:
        square_index += 8
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[initial_square] = "empty"
            potential_board_status[new_square] = f"{color}_Rook"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if (move_causes_check == False):
                possible_moves.append(new_square)
                moves_up -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Rook"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break



    square_index = squares_list.index(initial_square)
    moves_down = squares_to_edge(squares_list, initial_square, "down")
    while moves_down > 0:
        square_index -= 8
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[initial_square] = "empty"
            potential_board_status[new_square] = f"{color}_Rook"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if (move_causes_check == False):
                possible_moves.append(new_square)
                moves_down -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Rook"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break



    square_index = squares_list.index(initial_square)
    moves_right = squares_to_edge(squares_list, initial_square, "right")
    while moves_right > 0:
        square_index += 1
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[initial_square] = "empty"
            potential_board_status[new_square] = f"{color}_Rook"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if (move_causes_check == False):
                possible_moves.append(new_square)
                moves_right -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Rook"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break



    square_index = squares_list.index(initial_square)
    moves_left = squares_to_edge(squares_list, initial_square, "left")
    while moves_left > 0:   
        square_index -= 1
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[initial_square] = "empty"
            potential_board_status[new_square] = f"{color}_Rook"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if (move_causes_check == False):
                possible_moves.append(new_square)
                moves_left -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Rook"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break



    return possible_moves



def move_knight(color, initial_square, squares_list, board_status, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved):
    possible_moves = []
    potential_board_status = deepcopy(board_status)

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
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Knight"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break
        else: break

    while True:
        if squares_right >= 2 and squares_up >= 1:
            new_square_index = square_index + 10
            new_square = squares_list[new_square_index]
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Knight"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break
        else: break

    while True:
        if squares_right >= 2 and squares_down >= 1:
            new_square_index = square_index - 6
            new_square = squares_list[new_square_index]
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Knight"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break
        else: break

    while True:
        if squares_down >= 2 and squares_right >= 1:
            new_square_index = square_index - 15
            new_square = squares_list[new_square_index]
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Knight"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break
        else: break

    while True:
        if squares_down >= 2 and squares_left >= 1:
            new_square_index = square_index - 17
            new_square = squares_list[new_square_index]
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Knight"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break
        else: break

    while True:
        if squares_left >= 2 and squares_down >= 1:
            new_square_index = square_index - 10
            new_square = squares_list[new_square_index]
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Knight"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break
        else: break

    while True:
        if squares_left >= 2 and squares_up >= 1:
            new_square_index = square_index + 6
            new_square = squares_list[new_square_index]
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Knight"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break
        else: break

    while True:
        if squares_up >= 2 and squares_left >= 1:
            new_square_index = square_index + 15
            new_square = squares_list[new_square_index]
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Knight"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break
        else: break

    
    return possible_moves
    
        

def move_bishop(color, initial_square, squares_list, board_status, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved):
    possible_moves = []
    potential_board_status = deepcopy(board_status)

    square_index = squares_list.index(initial_square)
    moves_up_right = squares_to_edge(squares_list, initial_square, "up", "right")
    while moves_up_right > 0:
        square_index += 9
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[initial_square] = "empty"
            potential_board_status[new_square] = f"{color}_Bishop"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if (move_causes_check == False):
                possible_moves.append(new_square)
                moves_up_right -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Bishop"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break
    
    square_index = squares_list.index(initial_square)
    moves_up_left = squares_to_edge(squares_list, initial_square, "up", "left")
    while moves_up_left > 0:
        square_index += 7
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[initial_square] = "empty"
            potential_board_status[new_square] = f"{color}_Bishop"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if (move_causes_check == False):
                possible_moves.append(new_square)
                moves_up_left -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Bishop"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break

    square_index = squares_list.index(initial_square)
    moves_down_right = squares_to_edge(squares_list, initial_square, "down", "right")
    while moves_down_right > 0:
        square_index -= 7
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[initial_square] = "empty"
            potential_board_status[new_square] = f"{color}_Bishop"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if (move_causes_check == False):
                possible_moves.append(new_square)
                moves_down_right -= 1

        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Bishop"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break


    square_index = squares_list.index(initial_square)
    moves_down_left = squares_to_edge(squares_list, initial_square, "down", "left")
    while moves_down_left > 0:
        square_index -= 9
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[initial_square] = "empty"
            potential_board_status[new_square] = f"{color}_Bishop"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if (move_causes_check == False):
                possible_moves.append(new_square)
                moves_down_left -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_Bishop"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    break
                else: break


    return possible_moves


def move_king(color, initial_square, squares_list, board_status, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved):
    possible_moves = []
    potential_board_status = deepcopy(board_status)

    # horizontal and vertical king moves
    square_index = squares_list.index(initial_square)
    moves_up = squares_to_edge(squares_list, initial_square, "up")
    while True:
        if moves_up != 0:
            print("moves_up: ", moves_up)
            square_index += 8
            new_square = squares_list[square_index]
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_King"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    print(0)
                    break
                else: break
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
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_King"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    print(1)
                    break
                else: break
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
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_King"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    print(2)
                    break
                else: break
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
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_King"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    print(3)
                    break
                else: break
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
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_King"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    print(4)
                    break
                else: break
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
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_King"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    print(5)
                    break
                else: break
        else: break


    square_index = squares_list.index(initial_square)
    moves_down_right = squares_to_edge(squares_list, initial_square, "down", "right")
    print(moves_down_right, "down_right")
    while True:
        if moves_down_right != 0:
            square_index -= 7
            new_square = squares_list[square_index]
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_King"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    print(6)
                    break
                else: break
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
                potential_board_status[initial_square] = "empty"
                potential_board_status[new_square] = f"{color}_King"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if (move_causes_check == False):
                    possible_moves.append(new_square)
                    print(7)
                    break
                else: break
        else: break

    square_index = squares_list.index(initial_square)
    
    white_can_castle_right = False
    white_can_castle_left = False
    black_can_castle_right = False
    black_can_castle_left = False

    if color == "White":
        if king_has_moved == False & h_file_rook_has_moved == False:
            if board_status["F1"] == "empty" and board_status["G1"] == "empty":
                if look_for_check(board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved) == False:
                    white_can_castle_right = True

            if king_has_moved == False and a_file_rook_has_moved == False:
                if board_status["D1"] == "empty" and board_status["C1"] == "empty" and board_status["B1"] == "empty":
                    if look_for_check(board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved) == False:
                        white_can_castle_left = True

    elif color == "Black":
        if king_has_moved == False & h_file_rook_has_moved == False:
            if board_status["F8"] == "empty" and board_status["G8"] == "empty":
                    if look_for_check(board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved) == False:
                        black_can_castle_right = True

            if king_has_moved == False and a_file_rook_has_moved == False:
                if board_status["D8"] == "empty" and board_status["C8"] == "empty" and board_status["B8"] == "empty":
                    if look_for_check(board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved) == False:
                        black_can_castle_left = True


    if white_can_castle_right == True:
        potential_board_status[initial_square] = "empty"
        potential_board_status[squares_list[square_index + 2]] = f"{color}_King"
        move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
        potential_board_status = deepcopy(board_status)
        if (move_causes_check == False):
            possible_moves.append(squares_list[square_index + 2])
    if white_can_castle_left == True:
        potential_board_status[initial_square] = "empty"
        potential_board_status[squares_list[square_index - 2]] = f"{color}_King"
        move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
        potential_board_status = deepcopy(board_status)
        if (move_causes_check == False):
            possible_moves.append(squares_list[square_index - 2])
    if black_can_castle_right == True:
        potential_board_status[initial_square] = "empty"
        potential_board_status[squares_list[square_index + 2]] = f"{color}_King"
        move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
        potential_board_status = deepcopy(board_status)
        if (move_causes_check == False):
            possible_moves.append(squares_list[square_index + 2])
    if black_can_castle_left == True:
        potential_board_status[initial_square] = "empty"
        potential_board_status[squares_list[square_index - 2]] = f"{color}_King"
        move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
        potential_board_status = deepcopy(board_status)
        if (move_causes_check == False):
            possible_moves.append(squares_list[square_index - 2])
    
            
    return possible_moves

    # add code for check/checkmate (after all code for move restrictions, call each function for all pieces on the possible_moves list, and remove any squares returned by the other functions from possible_moves. If none remain, checkmate = True)



def move_queen(color, initial_square, squares_list, board_status, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved):
    possible_moves = []
    potential_board_status = deepcopy(board_status)

    # horizontal and vertical queen moves
    square_index = squares_list.index(initial_square)
    moves_up = squares_to_edge(squares_list, initial_square, "up")
    while moves_up > 0:
        square_index += 8
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[square_index] = "empty"
            potential_board_status[new_square] = f"{color}_Queen"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if move_causes_check == False:
                possible_moves.append(new_square)
                moves_up -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[square_index] = "empty"
                potential_board_status[new_square] = f"{color}_Queen"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if move_causes_check == False:
                    possible_moves.append(new_square)
                    break
                else: break


    square_index = squares_list.index(initial_square)
    moves_down = squares_to_edge(squares_list, initial_square, "down")
    while moves_down > 0:
        square_index -= 8
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[square_index] = "empty"
            potential_board_status[new_square] = f"{color}_Queen"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if move_causes_check == False:
                possible_moves.append(new_square)
                moves_down -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[square_index] = "empty"
                potential_board_status[new_square] = f"{color}_Queen"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if move_causes_check == False:
                    possible_moves.append(new_square)
                    break
                else: break


    square_index = squares_list.index(initial_square)
    moves_right = squares_to_edge(squares_list, initial_square, "right")
    while moves_right > 0:
        square_index += 1
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[square_index] = "empty"
            potential_board_status[new_square] = f"{color}_Queen"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if move_causes_check == False:
                possible_moves.append(new_square)
                moves_right -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[square_index] = "empty"
                potential_board_status[new_square] = f"{color}_Queen"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if move_causes_check == False:
                    possible_moves.append(new_square)
                    break
                else: break


    square_index = squares_list.index(initial_square)
    moves_left = squares_to_edge(squares_list, initial_square, "left")
    while moves_left > 0:   
        square_index -= 1
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[square_index] = "empty"
            potential_board_status[new_square] = f"{color}_Queen"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if move_causes_check == False:
                possible_moves.append(new_square)
                moves_left -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[square_index] = "empty"
                potential_board_status[new_square] = f"{color}_Queen"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if move_causes_check == False:
                    possible_moves.append(new_square)
                    break
                else: break

    # diagonal queen moves
    square_index = squares_list.index(initial_square)
    moves_up_right = squares_to_edge(squares_list, initial_square, "up", "right")
    while moves_up_right > 0:
        square_index += 9
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[square_index] = "empty"
            potential_board_status[new_square] = f"{color}_Queen"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if move_causes_check == False:
                possible_moves.append(new_square)
                moves_up_right -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[square_index] = "empty"
                potential_board_status[new_square] = f"{color}_Queen"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if move_causes_check == False:
                    possible_moves.append(new_square)
                    break
                else: break

    
    square_index = squares_list.index(initial_square)
    moves_up_left = squares_to_edge(squares_list, initial_square, "up", "left")
    while moves_up_left > 0:
        square_index += 7
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[square_index] = "empty"
            potential_board_status[new_square] = f"{color}_Queen"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if move_causes_check == False:
                possible_moves.append(new_square)
                moves_up_left -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[square_index] = "empty"
                potential_board_status[new_square] = f"{color}_Queen"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if move_causes_check == False:
                    possible_moves.append(new_square)
                    break
                else: break

    square_index = squares_list.index(initial_square)
    moves_down_right = squares_to_edge(squares_list, initial_square, "down", "right")
    while moves_down_right > 0:
        square_index -= 7
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[square_index] = "empty"
            potential_board_status[new_square] = f"{color}_Queen"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if move_causes_check == False:
                possible_moves.append(new_square)
                moves_down_right -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[square_index] = "empty"
                potential_board_status[new_square] = f"{color}_Queen"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if move_causes_check == False:
                    possible_moves.append(new_square)
                    break
                else: break


    square_index = squares_list.index(initial_square)
    moves_down_left = squares_to_edge(squares_list, initial_square, "down", "left")
    while moves_down_left > 0:
        square_index -= 9
        new_square = squares_list[square_index]
        if board_status[new_square] == "empty":
            potential_board_status[square_index] = "empty"
            potential_board_status[new_square] = f"{color}_Queen"
            move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
            potential_board_status = deepcopy(board_status)
            if move_causes_check == False:
                possible_moves.append(new_square)
                moves_down_left -= 1
        elif board_status[new_square] != "empty":
            if color in board_status[new_square]:
                break
            else:
                potential_board_status[square_index] = "empty"
                potential_board_status[new_square] = f"{color}_Queen"
                move_causes_check = look_for_check(potential_board_status, color, squares_list, previous_board_status, king_has_moved, h_file_rook_has_moved, a_file_rook_has_moved)
                potential_board_status = deepcopy(board_status)
                if move_causes_check == False:
                    possible_moves.append(new_square)
                    break
                else: break


    return possible_moves