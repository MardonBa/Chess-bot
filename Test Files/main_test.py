
from datetime import datetime
start = datetime.now()
import board_and_pieces_test as bd_pc
import move_pieces_test as mp
import chess_game_logic_test as cgl
import pygame as p 
from sys import exit
from copy import deepcopy

board = bd_pc.GameState()
board_squares = board.create_board()
print(board_squares)
board_status = board.piece_position(board=board_squares, pieces=board.square_status)
print(board_status)
screen_width = 1400
screen_height = 800
board_width = 73
board_height = 73
max_fps = 30
images_dict = {} 
images_list = []


p.init()        # initializes pygame window
screen = p.display.set_mode((screen_width, screen_height))
screen.fill("gray34")
p.display.set_caption("Chess Bot")
clock = p.time.Clock()
# gamestate was initialized lines 11-22


def square_placement():
    x_y_square_placement = []
    
    for i in range(8):
        for val in range(8):
            x_placement = 80 + ((val + 1) * 73)

            y_placement = 692 - ((i + 1) * 73)

            x_y_square_placement.append((x_placement, y_placement))


    return x_y_square_placement

square_placement = square_placement()



square_placement_dict = {}   
for x in range(len(board_squares)):
    square_placement_dict[board_squares[x]] = square_placement[x]


# function that draws the board (squares). Uses the Board() class and object.draw(surface) to draw each square on the board, with Board() taking inputs of which square to draw(for image files), and the x and y position of each square
def squares_init():
    squares_dict = {}
    for i in range(64):     # board_squares[i] and square_placement[i]
        square_name = board_squares[i]
        square = bd_pc.Board(square_name, square_placement[i])
        squares_dict[square_name] = p.sprite.GroupSingle()
        squares_dict[square_name].add(square)
        squares_dict[square_name].draw(screen)

    return squares_dict

squares_dict = squares_init()

# The following lines initalize and draw the pieces in their starting squares

def pieces_init():
    pieces_dict = {}

    white_rook = bd_pc.White_Rook(square_placement_dict["A1"][0], square_placement_dict["A1"][1], "A1")
    white_rook_group = bd_pc.ExtendedGroupSingle()       # When a piece gets taken, can the group get changed to None, and the piece goes away?
    white_rook_group.add(white_rook)
    pieces_dict["A1"] = white_rook_group

    white_knight = bd_pc.White_Knight(square_placement_dict["B1"][0], square_placement_dict["B1"][1], "B1")
    white_knight_group = bd_pc.ExtendedGroupSingle()
    white_knight_group.add(white_knight)
    pieces_dict["B1"] = white_knight_group

    white_bishop = bd_pc.White_Bishop(square_placement_dict["C1"][0], square_placement_dict["C1"][1], "C1")
    white_bishop_group = bd_pc.ExtendedGroupSingle()
    white_bishop_group.add(white_bishop)
    pieces_dict["C1"] = white_bishop_group

    white_queen = bd_pc.White_Queen(square_placement_dict["D1"][0], square_placement_dict["D1"][1], "D1")
    white_queen_group = bd_pc.ExtendedGroupSingle()
    white_queen_group.add(white_queen)
    pieces_dict["D1"] = white_queen_group

    white_king = bd_pc.White_King(square_placement_dict["E1"][0], square_placement_dict["E1"][1], "E1")
    white_king_group = bd_pc.ExtendedGroupSingle()
    white_king_group.add(white_king)
    pieces_dict["E1"] = white_king_group

    white_bishop = bd_pc.White_Bishop(square_placement_dict["F1"][0], square_placement_dict["F1"][1], "F1")
    white_bishop_group = bd_pc.ExtendedGroupSingle()
    white_bishop_group.add(white_bishop)
    pieces_dict["F1"] = white_bishop_group

    white_knight = bd_pc.White_Knight(square_placement_dict["G1"][0], square_placement_dict["G1"][1], "G1")
    white_knight_group = bd_pc.ExtendedGroupSingle()
    white_knight_group.add(white_knight)
    pieces_dict["G1"] = white_knight_group

    white_rook = bd_pc.White_Rook(square_placement_dict["H1"][0], square_placement_dict["H1"][1], "H1")
    white_rook_group = bd_pc.ExtendedGroupSingle()
    white_rook_group.add(white_rook)
    pieces_dict["H1"] = white_rook_group

    white_pawn = bd_pc.White_Pawn(square_placement_dict["A2"][0], square_placement_dict["A2"][1], "A2")
    white_pawn_group = bd_pc.ExtendedGroupSingle()
    white_pawn_group.add(white_pawn)
    pieces_dict["A2"] = white_pawn_group

    white_pawn = bd_pc.White_Pawn(square_placement_dict["B2"][0], square_placement_dict["B2"][1], "B2")
    white_pawn_group = bd_pc.ExtendedGroupSingle()
    white_pawn_group.add(white_pawn)
    pieces_dict["B2"] = white_pawn_group

    white_pawn = bd_pc.White_Pawn(square_placement_dict["C2"][0], square_placement_dict["C2"][1], "C2")
    white_pawn_group = bd_pc.ExtendedGroupSingle()
    white_pawn_group.add(white_pawn)
    pieces_dict["C2"] = white_pawn_group

    white_pawn = bd_pc.White_Pawn(square_placement_dict["D2"][0], square_placement_dict["D2"][1], "D2")
    white_pawn_group = bd_pc.ExtendedGroupSingle()
    white_pawn_group.add(white_pawn)
    pieces_dict["D2"] = white_pawn_group

    white_pawn = bd_pc.White_Pawn(square_placement_dict["E2"][0], square_placement_dict["E2"][1], "E2")
    white_pawn_group = bd_pc.ExtendedGroupSingle()
    white_pawn_group.add(white_pawn)
    pieces_dict["E2"] = white_pawn_group

    white_pawn = bd_pc.White_Pawn(square_placement_dict["F2"][0], square_placement_dict["F2"][1], "F2")
    white_pawn_group = bd_pc.ExtendedGroupSingle()
    white_pawn_group.add(white_pawn)
    pieces_dict["F2"] = white_pawn_group

    white_pawn = bd_pc.White_Pawn(square_placement_dict["G2"][0], square_placement_dict["G2"][1], "G2")
    white_pawn_group = bd_pc.ExtendedGroupSingle()
    white_pawn_group.add(white_pawn)
    pieces_dict["G2"] = white_pawn_group

    white_pawn = bd_pc.White_Pawn(square_placement_dict["H2"][0], square_placement_dict["H2"][1], "H2")
    white_pawn_group = bd_pc.ExtendedGroupSingle()
    white_pawn_group.add(white_pawn)
    pieces_dict["H2"] = white_pawn_group



    black_rook = bd_pc.Black_Rook(square_placement_dict["A8"][0], square_placement_dict["A8"][1], "A8")
    black_rook_group = bd_pc.ExtendedGroupSingle()       # When a piece gets taken, can the group get changed to None, and the piece goes away?
    black_rook_group.add(black_rook)
    pieces_dict["A8"] = black_rook_group

    black_knight = bd_pc.Black_Knight(square_placement_dict["B8"][0], square_placement_dict["B8"][1], "B8")
    black_knight_group = bd_pc.ExtendedGroupSingle()
    black_knight_group.add(black_knight)
    pieces_dict["B8"] = black_knight_group

    black_bishop = bd_pc.Black_Bishop(square_placement_dict["C8"][0], square_placement_dict["C8"][1], "C8")
    black_bishop_group = bd_pc.ExtendedGroupSingle()
    black_bishop_group.add(black_bishop)
    pieces_dict["C8"] = black_bishop_group

    black_queen = bd_pc.Black_Queen(square_placement_dict["D8"][0], square_placement_dict["D8"][1], "D8")
    black_queen_group = bd_pc.ExtendedGroupSingle()
    black_queen_group.add(black_queen)
    pieces_dict["D8"] = black_queen_group

    black_king = bd_pc.Black_King(square_placement_dict["E8"][0], square_placement_dict["E8"][1], "E8")
    black_king_group = bd_pc.ExtendedGroupSingle()
    black_king_group.add(black_king)
    pieces_dict["E8"] = black_king_group

    black_bishop = bd_pc.Black_Bishop(square_placement_dict["F8"][0], square_placement_dict["F8"][1], "F8")
    black_bishop_group = bd_pc.ExtendedGroupSingle()
    black_bishop_group.add(black_bishop)
    pieces_dict["F8"] = black_bishop_group


    black_knight = bd_pc.Black_Knight(square_placement_dict["G8"][0], square_placement_dict["G8"][1], "G8")
    black_knight_group = bd_pc.ExtendedGroupSingle()
    black_knight_group.add(black_knight)
    pieces_dict["G8"] = black_knight_group

    black_rook = bd_pc.Black_Rook(square_placement_dict["H8"][0], square_placement_dict["H8"][1], "H8")
    black_rook_group = bd_pc.ExtendedGroupSingle()
    black_rook_group.add(black_rook)
    pieces_dict["H8"] = black_rook_group

    black_pawn = bd_pc.Black_Pawn(square_placement_dict["A7"][0], square_placement_dict["A7"][1], "A7")
    black_pawn_group = bd_pc.ExtendedGroupSingle()
    black_pawn_group.add(black_pawn)
    pieces_dict["A7"] = black_pawn_group

    black_pawn = bd_pc.Black_Pawn(square_placement_dict["B7"][0], square_placement_dict["B7"][1], "B7")
    black_pawn_group = bd_pc.ExtendedGroupSingle()
    black_pawn_group.add(black_pawn)
    pieces_dict["B7"] = black_pawn_group

    black_pawn = bd_pc.Black_Pawn(square_placement_dict["C7"][0], square_placement_dict["C7"][1], "C7")
    black_pawn_group = bd_pc.ExtendedGroupSingle()
    black_pawn_group.add(black_pawn)
    pieces_dict["C7"] = black_pawn_group

    black_pawn = bd_pc.Black_Pawn(square_placement_dict["D7"][0], square_placement_dict["D7"][1], "D7")
    black_pawn_group = bd_pc.ExtendedGroupSingle()
    black_pawn_group.add(black_pawn)
    pieces_dict["D7"] = black_pawn_group

    black_pawn = bd_pc.Black_Pawn(square_placement_dict["E7"][0], square_placement_dict["E7"][1], "E7")
    black_pawn_group = bd_pc.ExtendedGroupSingle()
    black_pawn_group.add(black_pawn)
    pieces_dict["E7"] = black_pawn_group

    black_pawn = bd_pc.Black_Pawn(square_placement_dict["F7"][0], square_placement_dict["F7"][1], "F7")
    black_pawn_group = bd_pc.ExtendedGroupSingle()
    black_pawn_group.add(black_pawn)
    pieces_dict["F7"] = black_pawn_group

    black_pawn = bd_pc.Black_Pawn(square_placement_dict["G7"][0], square_placement_dict["G7"][1], "G7")
    black_pawn_group = bd_pc.ExtendedGroupSingle()
    black_pawn_group.add(black_pawn)
    pieces_dict["G7"] = black_pawn_group

    black_pawn = bd_pc.Black_Pawn(square_placement_dict["H7"][0], square_placement_dict["H7"][1], "H7")
    black_pawn_group = bd_pc.ExtendedGroupSingle()
    black_pawn_group.add(black_pawn)
    pieces_dict["H7"] = black_pawn_group

    return pieces_dict

pieces_dict = pieces_init()


def pieces_draw(pieces_dict):
    for val in pieces_dict.values():
        val.draw(screen)

pieces_draw(pieces_dict)

def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key
 
    return "key doesn't exist"

def draw_highlight(squares_to_highlight, squares_list):       # squares_to_highlight should be a list
    square_group = p.sprite.Group()

    for i in range(len(squares_to_highlight)):
        square = squares_to_highlight[i]
        square_index = squares_list.index(square)
        square_to_highlight = bd_pc.Hightlighted_Square(square_placement[square_index][0], square_placement[square_index][1])
        square_group.add(square_to_highlight)
        square_group.draw(screen)

def check_for_check(color, squares_list, board_status, previous_board_status, use_opposite_color_to_check):
    king_to_check = "White_King" if color == "White" else "Black_King"
    if use_opposite_color_to_check == True:
        color_to_check = "White" if color == "Black" else "Black"
    else:
        color_to_check = color
    for square, piece in board_status.items():
        if color_to_check in piece:
            if "Queen" in piece:
                available_moves = cgl.move_queen(color_to_check, square, squares_list, board_status)
                for move in available_moves:
                    if board_status[move] == king_to_check:
                        return True
            if "Rook" in piece:
                available_moves = cgl.move_rook(color_to_check, square, squares_list, board_status)
                for move in available_moves:
                    if board_status[move] == king_to_check:
                        return True
            if "Bishop" in piece:
                available_moves = cgl.move_bishop(color_to_check, square, squares_list, board_status)
                for move in available_moves:
                    if board_status[move] == king_to_check:
                        return True
            if "Knight" in piece:
                available_moves = cgl.move_knight(color_to_check, square, squares_list, board_status)
                for move in available_moves:
                    if board_status[move] == king_to_check:
                        return True
            if "Pawn" in piece:
                available_moves, en_passant = cgl.move_pawn(color_to_check, square, squares_list, board_status, previous_board_status,  first_move=True if "2" in square else False)
                for move in available_moves:    
                    if board_status[move] == king_to_check:
                        return True
                    
    return False    ## This line should only run if there is no check

def check_legal_moves(possible_moves, piece, original_square, color, squares_list, board_status, previous_board_status):
    for move in possible_moves:
        ## check to see if the new position created by this move stops check
        ## if not, remove the move from possible_moves
        board_status_copy = deepcopy(board_status)

        board_status[original_square] = "empty"
        board_status[move] = piece

        causes_check = check_for_check(color, squares_list, board_status, previous_board_status, False)
        print("move:", move)
        print("causes_check:", causes_check)
        if causes_check == True:
            possible_moves.pop(possible_moves.index(move))
        board_status = board_status_copy
    return possible_moves

selected_piece = None
selected_square = None
original_piece = "empty"
print(datetime.now() - start)
to_move = "White"
right_color = True

white_king_has_moved = False
white_a1_rook_has_moved = False
white_h1_rook_has_moved = False

black_king_has_moved = False
black_a8_rook_has_moved = False
black_h8_rook_has_moved = False


white_king_moving = False
black_king_moving = False
white_a1_rook_moving = False
white_h1_rook_moving = False
black_a8_rook_moving = False
black_h8_rook_moving = False

white_can_castle_right = False
white_can_castle_left = False
black_can_castle_right = False
black_can_castle_left = False

previous_board_status = deepcopy(board_status)
white_en_passant = None
black_en_passant = None
while True:

    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            exit()
        elif event.type == p.MOUSEBUTTONDOWN:

            if selected_piece == None:
                selected_piece = mp.select_piece(pieces_dict)
                if selected_piece == None:
                    print("Please select a piece")
                else: 
                    print(f"You selected {selected_piece}")

                    square = get_key(selected_piece, pieces_dict)
                    piece = board_status[square]
                    piece_color = "White" if "White" in piece else "Black"
                    print("piece_color = ", piece_color)

                    if to_move == piece_color:
                        white_en_passant = None
                        black_en_passant = None

                        if piece == "White_Rook":
                            possible_moves = cgl.move_rook("White", square, board_squares, board_status)
                            possible_moves = check_legal_moves(possible_moves, "White_Rook", square, "White", board_squares, board_status, previous_board_status)
                            draw_highlight(possible_moves, board_squares)
                            if "A" in square:
                                white_a1_rook_moving = True if white_a1_rook_moving == False else None
                            elif "H" in square:
                                white_h1_rook_moving = True if white_h1_rook_moving == False else None

                        elif piece == "White_Knight":
                            possible_moves = cgl.move_knight("White", square, board_squares, board_status)
                            possible_moves = check_legal_moves(possible_moves, "White_Knight", square, "White", board_squares, board_status, previous_board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "White_Bishop":
                            possible_moves = cgl.move_bishop("White", square, board_squares, board_status)
                            possible_moves = check_legal_moves(possible_moves, "White_Bishop", square, "White", board_squares, board_status, previous_board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "White_Queen":
                            possible_moves = cgl.move_queen("White", square, board_squares, board_status)
                            possible_moves = check_legal_moves(possible_moves, "White_Queen", square, "White", board_squares, board_status, previous_board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "White_King":
                            possible_moves = cgl.move_king("White", square, board_squares, board_status, white_king_has_moved, white_h1_rook_has_moved, white_a1_rook_has_moved)
                            possible_moves = check_legal_moves(possible_moves, "White_King", square, "White", board_squares, board_status, previous_board_status)
                            draw_highlight(possible_moves, board_squares)
                            white_king_moving = True if white_king_moving == False else None

                        elif piece == "White_Pawn":
                            possible_moves, white_en_passant = cgl.move_pawn("White", square, board_squares, board_status, previous_board_status, first_move=True if "2" in square else False)      # make sure to add code for determining if captures are possible
                            possible_moves = check_legal_moves(possible_moves, "White_Pawn", square, "White", board_squares, board_status, previous_board_status)
                            print(possible_moves)
                            draw_highlight(possible_moves, board_squares)

 

                        elif piece == "Black_Rook":
                            possible_moves = cgl.move_rook("Black", square, board_squares, board_status)
                            possible_moves = check_legal_moves(possible_moves, "Black_Rook", square, "Black", board_squares, board_status, previous_board_status)
                            draw_highlight(possible_moves, board_squares)
                            if "A" in square:
                                black_a8_rook_moving = True if black_a8_rook_moving == False else None
                            elif "H" in square:
                                black_h8_rook_moving = True if black_h8_rook_moving == False else None

                        elif piece == "Black_Knight":
                            possible_moves = cgl.move_knight("Black", square, board_squares, board_status)
                            possible_moves = check_legal_moves(possible_moves, "Black_Knight", square, "Black", board_squares, board_status, previous_board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "Black_Bishop":
                            possible_moves = cgl.move_bishop("Black", square, board_squares, board_status)
                            possible_moves = check_legal_moves(possible_moves, "Black_Knight", square, "Black", board_squares, board_status, previous_board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "Black_Queen":
                            possible_moves = cgl.move_queen("Black", square, board_squares, board_status)
                            possible_moves = check_legal_moves(possible_moves, "Black_Knight", square, "Black", board_squares, board_status, previous_board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "Black_King":
                            possible_moves = cgl.move_king("Black", square, board_squares, board_status, black_king_has_moved, black_h8_rook_has_moved, black_a8_rook_has_moved)
                            possible_moves = check_legal_moves(possible_moves, "Black_King", square, "Black", board_squares, board_status, previous_board_status)
                            draw_highlight(possible_moves, board_squares)
                            black_king_moving = True if black_king_moving == False else None

                        elif piece == "Black_Pawn":
                            possible_moves, black_en_passant = cgl.move_pawn("Black", square, board_squares, board_status, previous_board_status, first_move=True if "7" in square else False)     # make sure to add code for determining if captures are possible
                            possible_moves = check_legal_moves(possible_moves, "Black_Pawn", square, "Black", board_squares, board_status, previous_board_status)
                            draw_highlight(possible_moves, board_squares)
                            print(possible_moves)

                        else:
                            print("you done fucked up somewhere")

                        right_color = True

                    else:
                        print(f"Please pick a piece of the right color: {to_move}")
                        right_color = False
                        selected_piece = None

                    
                    

            else:      
                previous_board_status = deepcopy(board_status)
                if right_color == True:
                    selected_square = mp.select_square(squares_dict)
                    print(f"You selected {selected_square}")

                    if selected_square in possible_moves:
                        selected_piece.change_piece_coordinates(square_placement_dict[selected_square][0], square_placement_dict[selected_square][1])
                        to_move = "Black" if to_move == "White" else "White"
                        print("to_move = ", to_move)
                        board_status[square] = "empty"
                        board_status[selected_square] = piece
                        pieces_dict[selected_square] = selected_piece
                        del pieces_dict[square]

                        if piece == "White_Pawn" and "8" in selected_square:
                            print("Please choose a piece to promote to")
                            new_piece = input()
                            if new_piece.lower() == 'queen':
                                print(new_piece)
                                piece = "White_Queen"
                                white_queen = bd_pc.White_Queen(square_placement_dict[selected_square][0], square_placement_dict[selected_square][1], selected_square)
                                white_queen_group = bd_pc.ExtendedGroupSingle()
                                white_queen_group.add(white_queen)
                                pieces_dict[selected_square] = white_queen_group
                                board_status[selected_square] = piece
                            elif new_piece.lower() == "rook":
                                print(new_piece)
                                piece = "White_Rook"
                                white_rook = bd_pc.White_Rook(square_placement_dict[selected_square][0], square_placement_dict[selected_square][1], selected_square)
                                white_rook_group = bd_pc.ExtendedGroupSingle()
                                white_rook_group.add(white_rook)
                                pieces_dict[selected_square] = white_rook_group
                                board_status[selected_square] = piece
                            elif new_piece.lower() == "bishop":
                                print(new_piece)
                                piece = "White_Bishop"
                                white_bishop = bd_pc.White_Bishop(square_placement_dict[selected_square][0], square_placement_dict[selected_square][1], selected_square)
                                white_bishop_group = bd_pc.ExtendedGroupSingle()
                                white_bishop_group.add(white_bishop)
                                pieces_dict[selected_square] = white_bishop_group
                                board_status[selected_square] = piece
                            elif new_piece.lower() == "knight":
                                print(new_piece)
                                piece = "White_Knight"
                                white_knight = bd_pc.White_Knight(square_placement_dict[selected_square][0], square_placement_dict[selected_square][1], selected_square)
                                white_knight_group = bd_pc.ExtendedGroupSingle()
                                white_knight_group.add(white_knight)
                                pieces_dict[selected_square] = white_knight_group
                                board_status[selected_square] = piece

                        elif piece == "Black_Pawn" and "1" in selected_square:
                            print("Please choose a piece to promote to")
                            new_piece = input()
                            if new_piece.lower() == 'queen':
                                print(new_piece)
                                piece = "Black_Queen"
                                black_queen = bd_pc.Black_Queen(square_placement_dict[selected_square][0], square_placement_dict[selected_square][1], selected_square)
                                black_queen_group = bd_pc.ExtendedGroupSingle()
                                black_queen_group.add(black_queen)
                                pieces_dict[selected_square] = black_queen_group
                                board_status[selected_square] = piece
                            elif new_piece.lower() == "rook":
                                print(new_piece)
                                piece = "Black_Rook"
                                black_rook = bd_pc.Black_Rook(square_placement_dict[selected_square][0], square_placement_dict[selected_square][1], selected_square)
                                black_rook_group = bd_pc.ExtendedGroupSingle()
                                black_rook_group.add(black_rook)
                                pieces_dict[selected_square] = black_rook_group
                                board_status[selected_square] = piece
                            elif new_piece.lower() == "bishop":
                                print(new_piece)
                                piece = "Black_Bishop"
                                black_bishop = bd_pc.Black_Bishop(square_placement_dict[selected_square][0], square_placement_dict[selected_square][1], selected_square)
                                black_bishop_group = bd_pc.ExtendedGroupSingle()
                                black_bishop_group.add(black_bishop)
                                pieces_dict[selected_square] = black_bishop_group
                                board_status[selected_square] = piece
                            elif new_piece.lower() == "knight":
                                print(new_piece)
                                piece = "Black_Knight"
                                black_knight = bd_pc.Black_Knight(square_placement_dict[selected_square][0], square_placement_dict[selected_square][1], selected_square)
                                black_knight_group = bd_pc.ExtendedGroupSingle()
                                black_knight_group.add(black_knight)
                                pieces_dict[selected_square] = black_knight_group
                                board_status[selected_square] = piece


                        if white_en_passant == "right":
                            en_passant_square_index = board_squares.index(square) + 1
                            en_passant_square = board_squares[en_passant_square_index]
                            board_status[en_passant_square] = "empty"
                            del pieces_dict[en_passant_square]
                        elif white_en_passant == "left":
                            en_passant_square_index = board_squares.index(square) - 1
                            en_passant_square = board_squares[en_passant_square_index]
                            board_status[en_passant_square] = "empty"
                            del pieces_dict[en_passant_square]
                        elif black_en_passant == "right":
                            en_passant_square_index = board_squares.index(square) + 1
                            en_passant_square = board_squares[en_passant_square_index]
                            board_status[en_passant_square] = "empty"
                            del pieces_dict[en_passant_square]
                        elif black_en_passant == "left":
                            en_passant_square_index = board_squares.index(square) - 1
                            en_passant_square = board_squares[en_passant_square_index]
                            board_status[en_passant_square] = "empty"
                            del pieces_dict[en_passant_square]

                        if selected_square == "G1" and piece == "White_King" and white_king_has_moved == False and white_h1_rook_has_moved == False:
                            pieces_dict["H1"].change_piece_coordinates(square_placement_dict["F1"][0], square_placement_dict["F1"][1])
                            board_status["H1"] = "empty"
                            board_status["F1"] = "White_Rook"
                            pieces_dict["F1"] = pieces_dict["H1"]
                            del pieces_dict["H1"]
                            white_can_castle_right = False
                            white_king_has_moved = True
                            white_h1_rook_has_moved = True
                        
                        if selected_square == "C1" and piece == "White_King" and white_king_has_moved == False and white_a1_rook_has_moved == False:
                            pieces_dict["A1"].change_piece_coordinates(square_placement_dict["D1"][0], square_placement_dict["D1"][1])
                            board_status["A1"] = "empty"
                            board_status["D1"] = "White_Rook"
                            pieces_dict["D1"] = pieces_dict["A1"]
                            del pieces_dict["A1"]
                            white_can_castle_left = False
                            white_king_has_moved = True
                            white_a1_rook_has_moved = True

                        if selected_square == "G8" and piece == "Black_King" and black_king_has_moved == False and black_h8_rook_has_moved == False:
                            pieces_dict["H8"].change_piece_coordinates(square_placement_dict["F8"][0], square_placement_dict["F8"][1])
                            board_status["H8"] = "empty"
                            board_status["F8"] = "Black_Rook"
                            pieces_dict["F8"] = pieces_dict["H8"]
                            del pieces_dict["H8"]
                            black_can_castle_right = False
                            black_king_has_moved = True
                            black_h8_rook_has_moved = True

                        if selected_square == "C8" and piece == "Black_King" and black_king_has_moved == False and black_a8_rook_has_moved == False:
                            pieces_dict["A8"].change_piece_coordinates(square_placement_dict["D8"][0], square_placement_dict["D8"][1])
                            board_status["A8"] = "empty"
                            board_status["D8"] = "Black_Rook"
                            pieces_dict["D8"] = pieces_dict["A8"]
                            del pieces_dict["A8"]
                            black_can_castle_left = False
                            black_king_has_moved = True
                            black_a1_rook_has_moved = True


                        if white_a1_rook_moving == True:
                            white_a1_rook_has_moved = True
                            white_a1_rook_moving = None
                        
                        if white_h1_rook_moving == True:
                            white_h1_rook_has_moved = True
                            white_h1_rook_moving = None

                        if black_a8_rook_moving == True:
                            black_a8_rook_has_moved = True
                            black_a8_rook_moving = None

                        if black_h8_rook_moving == True:
                            black_a8_rook_has_moved = True
                            black_a8_rook_moving = None
                        
                        if white_king_moving == True:
                            white_king_has_moved = True
                            white_king_moving = None

                        if black_king_moving == True:
                            black_king_has_moved = True
                            black_king_moving = True

                        is_in_check = check_for_check(to_move, board_squares, board_status, previous_board_status, True)
                        print(to_move, "is in check = ", is_in_check)

                    else: 
                        if white_a1_rook_moving == True:
                            white_a1_rook_has_moved = False
                            white_a1_rook_moving = False
                        
                        if white_h1_rook_moving == True:
                            white_h1_rook_has_moved = False
                            white_h1_rook_moving = False

                        if black_a8_rook_moving == True:
                            black_a8_rook_has_moved = False
                            black_a8_rook_moving = False

                        if black_h8_rook_moving == True:
                            black_a8_rook_has_moved = False
                            black_a8_rook_moving = False
                        
                        if white_king_moving == True:
                            white_king_has_moved = False
                            white_king_moving = False

                        if black_king_moving == True:
                            black_king_has_moved = False
                            black_king_moving = False

                    squares_init()
                    pieces_draw(pieces_dict) 
                selected_square = None
                selected_piece = None
            

    p.display.update()

    clock.tick(max_fps)


# Current goals: be able to click a piece and move it. Possibly make the pieces sprites, learn about sprite class. might need to move the existing code for pieces to that class


# Make sure if a square is clicked that the piece can't move, to, don't allow the move.
