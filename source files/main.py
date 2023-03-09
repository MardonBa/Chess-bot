from datetime import datetime
start = datetime.now()
import board_and_pieces as bd_pc
import move_pieces as mp
import chess_game_logic as cgl
import pygame as p
from sys import exit

board = bd_pc.GameState()
print(type(board))
board_squares = board.create_board()
print(type(board_squares))
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
# gamestate was initialized lines 6-16


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

    white_rook1 = bd_pc.White_Rook(square_placement_dict["A1"][0], square_placement_dict["A1"][1], "A1")
    white_rook1_group = bd_pc.ExtendedGroupSingle()       # When a piece gets taken, can the group get changed to None, and the piece goes away?
    white_rook1_group.add(white_rook1)
    pieces_dict["A1"] = white_rook1_group

    white_knight1 = bd_pc.White_Knight(square_placement_dict["B1"][0], square_placement_dict["B1"][1], "B1")
    white_knight1_group = bd_pc.ExtendedGroupSingle()
    white_knight1_group.add(white_knight1)
    pieces_dict["B1"] = white_knight1_group

    white_bishop1 = bd_pc.White_Bishop(square_placement_dict["C1"][0], square_placement_dict["C1"][1], "C1")
    white_bishop1_group = bd_pc.ExtendedGroupSingle()
    white_bishop1_group.add(white_bishop1)
    pieces_dict["C1"] = white_bishop1_group

    white_queen = bd_pc.White_Queen(square_placement_dict["D1"][0], square_placement_dict["D1"][1], "D1")
    white_queen_group = bd_pc.ExtendedGroupSingle()
    white_queen_group.add(white_queen)
    pieces_dict["D1"] = white_queen_group

    white_king = bd_pc.White_King(square_placement_dict["E1"][0], square_placement_dict["E1"][1], "E1")
    white_king_group = bd_pc.ExtendedGroupSingle()
    white_king_group.add(white_king)
    pieces_dict["E1"] = white_king_group

    white_bishop2 = bd_pc.White_Bishop(square_placement_dict["F1"][0], square_placement_dict["F1"][1], "F1")
    white_bishop2_group = bd_pc.ExtendedGroupSingle()
    white_bishop2_group.add(white_bishop2)
    pieces_dict["F1"] = white_bishop2_group

    white_knight2 = bd_pc.White_Knight(square_placement_dict["G1"][0], square_placement_dict["G1"][1], "G1")
    white_knight2_group = bd_pc.ExtendedGroupSingle()
    white_knight2_group.add(white_knight2)
    pieces_dict["G1"] = white_knight2_group

    white_rook2 = bd_pc.White_Rook(square_placement_dict["H1"][0], square_placement_dict["H1"][1], "H1")
    white_rook2_group = bd_pc.ExtendedGroupSingle()
    white_rook2_group.add(white_rook2)
    pieces_dict["H1"] = white_rook2_group

    white_pawn1 = bd_pc.White_Pawn(square_placement_dict["A2"][0], square_placement_dict["A2"][1], "A2")
    white_pawn1_group = bd_pc.ExtendedGroupSingle()
    white_pawn1_group.add(white_pawn1)
    pieces_dict["A2"] = white_pawn1_group

    white_pawn2 = bd_pc.White_Pawn(square_placement_dict["B2"][0], square_placement_dict["B2"][1], "B2")
    white_pawn2_group = bd_pc.ExtendedGroupSingle()
    white_pawn2_group.add(white_pawn2)
    pieces_dict["B2"] = white_pawn2_group

    white_pawn3 = bd_pc.White_Pawn(square_placement_dict["C2"][0], square_placement_dict["C2"][1], "C2")
    white_pawn3_group = bd_pc.ExtendedGroupSingle()
    white_pawn3_group.add(white_pawn3)
    pieces_dict["C2"] = white_pawn3_group

    white_pawn4 = bd_pc.White_Pawn(square_placement_dict["D2"][0], square_placement_dict["D2"][1], "D2")
    white_pawn4_group = bd_pc.ExtendedGroupSingle()
    white_pawn4_group.add(white_pawn4)
    pieces_dict["D2"] = white_pawn4_group

    white_pawn5 = bd_pc.White_Pawn(square_placement_dict["E2"][0], square_placement_dict["E2"][1], "E2")
    white_pawn5_group = bd_pc.ExtendedGroupSingle()
    white_pawn5_group.add(white_pawn5)
    pieces_dict["E2"] = white_pawn5_group

    white_pawn6 = bd_pc.White_Pawn(square_placement_dict["F2"][0], square_placement_dict["F2"][1], "F2")
    white_pawn6_group = bd_pc.ExtendedGroupSingle()
    white_pawn6_group.add(white_pawn6)
    pieces_dict["F2"] = white_pawn6_group

    white_pawn7 = bd_pc.White_Pawn(square_placement_dict["G2"][0], square_placement_dict["G2"][1], "G2")
    white_pawn7_group = bd_pc.ExtendedGroupSingle()
    white_pawn7_group.add(white_pawn7)
    pieces_dict["G2"] = white_pawn7_group

    white_pawn8 = bd_pc.White_Pawn(square_placement_dict["H2"][0], square_placement_dict["H2"][1], "H2")
    white_pawn8_group = bd_pc.ExtendedGroupSingle()
    white_pawn8_group.add(white_pawn8)
    pieces_dict["H2"] = white_pawn8_group



    black_rook1 = bd_pc.Black_Rook(square_placement_dict["A8"][0], square_placement_dict["A8"][1], "A8")
    black_rook1_group = bd_pc.ExtendedGroupSingle()       # When a piece gets taken, can the group get changed to None, and the piece goes away?
    black_rook1_group.add(black_rook1)
    pieces_dict["A8"] = black_rook1_group

    black_knight1 = bd_pc.Black_Knight(square_placement_dict["B8"][0], square_placement_dict["B8"][1], "B8")
    black_knight1_group = bd_pc.ExtendedGroupSingle()
    black_knight1_group.add(black_knight1)
    pieces_dict["B8"] = black_knight1_group

    black_bishop1 = bd_pc.Black_Bishop(square_placement_dict["C8"][0], square_placement_dict["C8"][1], "C8")
    black_bishop1_group = bd_pc.ExtendedGroupSingle()
    black_bishop1_group.add(black_bishop1)
    pieces_dict["C8"] = black_bishop1_group

    black_queen = bd_pc.Black_Queen(square_placement_dict["D8"][0], square_placement_dict["D8"][1], "D8")
    black_queen_group = bd_pc.ExtendedGroupSingle()
    black_queen_group.add(black_queen)
    pieces_dict["D8"] = black_queen_group

    black_king = bd_pc.Black_King(square_placement_dict["E8"][0], square_placement_dict["E8"][1], "E8")
    black_king_group = bd_pc.ExtendedGroupSingle()
    black_king_group.add(black_king)
    pieces_dict["E8"] = black_king_group

    black_bishop2 = bd_pc.Black_Bishop(square_placement_dict["F8"][0], square_placement_dict["F8"][1], "F8")
    black_bishop2_group = bd_pc.ExtendedGroupSingle()
    black_bishop2_group.add(black_bishop2)
    pieces_dict["F8"] = black_bishop2_group


    black_knight2 = bd_pc.Black_Knight(square_placement_dict["G8"][0], square_placement_dict["G8"][1], "G8")
    black_knight2_group = bd_pc.ExtendedGroupSingle()
    black_knight2_group.add(black_knight2)
    pieces_dict["G8"] = black_knight2_group

    black_rook2 = bd_pc.Black_Rook(square_placement_dict["H8"][0], square_placement_dict["H8"][1], "H8")
    black_rook2_group = bd_pc.ExtendedGroupSingle()
    black_rook2_group.add(black_rook2)
    pieces_dict["H8"] = black_rook2_group

    black_pawn1 = bd_pc.Black_Pawn(square_placement_dict["A7"][0], square_placement_dict["A7"][1], "A7")
    black_pawn1_group = bd_pc.ExtendedGroupSingle()
    black_pawn1_group.add(black_pawn1)
    pieces_dict["A7"] = black_pawn1_group

    black_pawn2 = bd_pc.Black_Pawn(square_placement_dict["B7"][0], square_placement_dict["B7"][1], "B7")
    black_pawn2_group = bd_pc.ExtendedGroupSingle()
    black_pawn2_group.add(black_pawn2)
    pieces_dict["B7"] = black_pawn2_group

    black_pawn3 = bd_pc.Black_Pawn(square_placement_dict["C7"][0], square_placement_dict["C7"][1], "C7")
    black_pawn3_group = bd_pc.ExtendedGroupSingle()
    black_pawn3_group.add(black_pawn3)
    pieces_dict["C7"] = black_pawn3_group

    black_pawn4 = bd_pc.Black_Pawn(square_placement_dict["D7"][0], square_placement_dict["D7"][1], "D7")
    black_pawn4_group = bd_pc.ExtendedGroupSingle()
    black_pawn4_group.add(black_pawn4)
    pieces_dict["D7"] = black_pawn4_group

    black_pawn5 = bd_pc.Black_Pawn(square_placement_dict["E7"][0], square_placement_dict["E7"][1], "E7")
    black_pawn5_group = bd_pc.ExtendedGroupSingle()
    black_pawn5_group.add(black_pawn5)
    pieces_dict["E7"] = black_pawn5_group

    black_pawn6 = bd_pc.Black_Pawn(square_placement_dict["F7"][0], square_placement_dict["F7"][1], "F7")
    black_pawn6_group = bd_pc.ExtendedGroupSingle()
    black_pawn6_group.add(black_pawn6)
    pieces_dict["F7"] = black_pawn6_group

    black_pawn7 = bd_pc.Black_Pawn(square_placement_dict["G7"][0], square_placement_dict["G7"][1], "G7")
    black_pawn7_group = bd_pc.ExtendedGroupSingle()
    black_pawn7_group.add(black_pawn7)
    pieces_dict["G7"] = black_pawn7_group

    black_pawn8 = bd_pc.Black_Pawn(square_placement_dict["H7"][0], square_placement_dict["H7"][1], "H7")
    black_pawn8_group = bd_pc.ExtendedGroupSingle()
    black_pawn8_group.add(black_pawn8)
    pieces_dict["H7"] = black_pawn8_group

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




selected_piece = None
selected_square = None
original_piece = "empty"
print(datetime.now() - start)
to_move = "White"
right_color = True

while True:

    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            exit()
        elif event.type == p.MOUSEBUTTONDOWN:

            if selected_piece == None:
                selected_piece = mp.select_piece(pieces_dict)
                print(type(selected_piece))
                if selected_piece == None:
                    print("Please select a piece")
                else: 
                    print(f"You selected {selected_piece}")

                    square = get_key(selected_piece, pieces_dict)
                    print(square)
                    piece = board_status[square]
                    print(piece)
                    piece_color = "White" if "White" in piece else "Black"
                    print("piece_color = ", piece_color)

                    if to_move == piece_color:

                        if piece == "White_Rook":
                            possible_moves = cgl.move_rook("White", square, board_squares, board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "White_Knight":
                            possible_moves = cgl.move_knight("White", square, board_squares, board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "White_Bishop":
                            possible_moves = cgl.move_bishop("White", square, board_squares, board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "White_Queen":
                            possible_moves = cgl.move_queen("White", square, board_squares, board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "White_King":
                            possible_moves = cgl.move_king("White", square, board_squares, board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "White_Pawn":
                            possible_moves = cgl.move_pawn("White", square, board_squares)      # make sure to add code for determining if captures are possible
                            draw_highlight(possible_moves, board_squares)

 

                        elif piece == "Black_Rook":
                            possible_moves = cgl.move_rook("Black", square, board_squares, board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "Black_Knight":
                            possible_moves = cgl.move_knight("Black", square, board_squares, board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "Black_Bishop":
                            possible_moves = cgl.move_bishop("Black", square, board_squares, board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "Black_Queen":
                            possible_moves = cgl.move_queen("Black", square, board_squares, board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "Black_King":
                            possible_moves = cgl.move_king("Black", square, board_squares, board_status)
                            draw_highlight(possible_moves, board_squares)

                        elif piece == "Black_Pawn":
                            possible_moves = cgl.move_pawn("Black", square, board_squares)     # make sure to add code for determining if captures are possible
                            draw_highlight(possible_moves, board_squares)

                        else:
                            print("you done fucked up somewhere")

                        right_color = True

                    else:
                        print(f"Please pick a piece of the right color: {to_move}")
                        right_color = False
                        selected_piece = None

                    

            else:
                if right_color == True:
                    selected_square = mp.select_square(squares_dict)
                    print(f"You selected {selected_square}")
                    if selected_square != None and selected_square in possible_moves:
                        selected_piece.change_piece_coordinates(square_placement_dict[selected_square][0], square_placement_dict[selected_square][1])
                        to_move = "Black" if to_move == "White" else "White"
                        print("to_move = ", to_move)
                        board_status[square] = "empty"
                        board_status[selected_square] = piece
                        del pieces_dict[square]
                        pieces_dict[selected_square] = selected_piece
                    squares_init()
                    pieces_draw(pieces_dict)
                selected_square = None
                selected_piece = None



    p.display.update()

    clock.tick(max_fps)


# Current goals: be able to click a piece and move it. Possibly make the pieces sprites, learn about sprite class. might need to move the existing code for pieces to that class


# Make sure if a square is clicked that the piece can't move, to, don't allow the move.
# Find a way to see if individual pawns have been moved. Possibly do this by keeping track of moves in the game, would be easy for first move tracking for castling, en passant, etc