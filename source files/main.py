from datetime import datetime
start = datetime.now()
import board_and_pieces as bd_pc
import pygame as p
from sys import exit

board = bd_pc.GameState()
board_squares = board.create_board()
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
print(square_placement)


square_placement_dict = {}   
for x in range(len(board_squares)):
    square_placement_dict[board_squares[x]] = square_placement[x]


# function that draws the board (squares). Uses the Board() class and object.draw(surface) to draw each square on the board, with Board() taking inputs of which square to draw(for image files), and the x and y position of each square
square_groups = [
    "A1_group", "B1_group", "C1_group", "D1_group", "E1_group", "F1_group", "G1_group", "H1_group", \
    "A2_group", "B2_group", "C2_group", "D2_group", "E2_group", "F2_gruop", "G2_group", "H2_group", \
    "A3_group", "B3_group", "C3_group", "D3_group", "E3_group", "F3_group", "G3_group", "H3_group", \
    "A4_group", "B4_group", "C4_group", "D4_group", "E4_group", "F4_group", "G4_group", "H4_group", \
    "A5_group", "B5_group", "C5_group", "D5_group", "E5_group", "F5_group", "G5_group", "H5_group", \
    "A6_group", "B6_group", "C6_group", "D6_group", "E6_group", "F6_group", "G6_group", "H6_group", \
    "A7_group", "B7_group", "C7_group", "D7_group", "E7_group", "F7_group", "G7_group", "H7_group", \
    "A8_group", "B8_group", "C8_group", "D8_group", "E8_group", "F8_group", "G8_group", "H8_group" ]

def squares_init():
    squares_dict = {}
    for i in range(64):     # board_squares[i] and square_groups[i] and square_placement[i]
        square_name = board_squares[i]
        square = bd_pc.Board(board_squares[i], square_placement[i])
        squares_dict[square_name] = p.sprite.GroupSingle()
        squares_dict[square_name].add(square)
        squares_dict[square_name].draw(screen)

    return squares_dict

squares_dict = squares_init()
print(squares_dict)


# The following lines initalize and draw the pieces in their starting squares
white_rook1 = bd_pc.White_Rook(square_placement_dict["A1"][0], square_placement_dict["A1"][1], "A1")
white_rook1_group= p.sprite.GroupSingle()       # When a piece gets taken, can the group get changed to None, and the piece goes away?
white_rook1_group.add(white_rook1)
white_rook1_group.draw(screen)

white_knight1 = bd_pc.White_Knight(square_placement_dict["B1"][0], square_placement_dict["B1"][1], "B1")
white_knight1_group = p.sprite.GroupSingle()
white_knight1_group.add(white_knight1)
white_knight1_group.draw(screen)

white_bishop1 = bd_pc.White_Bishop(square_placement_dict["C1"][0], square_placement_dict["C1"][1], "C1")
white_bishop1_group = p.sprite.GroupSingle()
white_bishop1_group.add(white_bishop1)
white_bishop1_group.draw(screen)

white_queen = bd_pc.White_Queen(square_placement_dict["D1"][0], square_placement_dict["D1"][1], "D1")
white_queen_group = p.sprite.GroupSingle()
white_queen_group.add(white_queen)
white_queen_group.draw(screen)

white_king = bd_pc.White_King(square_placement_dict["E1"][0], square_placement_dict["E1"][1], "E1")
white_king_group = p.sprite.GroupSingle()
white_king_group.add(white_king)
white_king_group.draw(screen)

white_bishop2 = bd_pc.White_Bishop(square_placement_dict["F1"][0], square_placement_dict["F1"][1], "F1")
white_bishop2_group = p.sprite.GroupSingle()
white_bishop2_group.add(white_bishop2)
white_bishop2_group.draw(screen)

white_knight2 = bd_pc.White_Knight(square_placement_dict["G1"][0], square_placement_dict["G1"][1], "G1")
white_knight2_group = p.sprite.GroupSingle()
white_knight2_group.add(white_knight2)
white_knight2_group.draw(screen)

white_rook2 = bd_pc.White_Rook(square_placement_dict["H1"][0], square_placement_dict["H1"][1], "H1")
white_rook2_group = p.sprite.GroupSingle()
white_rook2_group.add(white_rook2)
white_rook2_group.draw(screen)

white_pawn1 = bd_pc.White_Pawn(square_placement_dict["A2"][0], square_placement_dict["A2"][1], "A2")
white_pawn1_group = p.sprite.GroupSingle()
white_pawn1_group.add(white_pawn1)
white_pawn1_group.draw(screen)

white_pawn2 = bd_pc.White_Pawn(square_placement_dict["B2"][0], square_placement_dict["B2"][1], "B2")
white_pawn2_group = p.sprite.GroupSingle()
white_pawn2_group.add(white_pawn2)
white_pawn2_group.draw(screen)

white_pawn3 = bd_pc.White_Pawn(square_placement_dict["C2"][0], square_placement_dict["C2"][1], "C2")
white_pawn3_group = p.sprite.GroupSingle()
white_pawn3_group.add(white_pawn3)
white_pawn3_group.draw(screen)

white_pawn4 = bd_pc.White_Pawn(square_placement_dict["D2"][0], square_placement_dict["D2"][1], "D2")
white_pawn4_group = p.sprite.GroupSingle()
white_pawn4_group.add(white_pawn4)
white_pawn4_group.draw(screen)

white_pawn5 = bd_pc.White_Pawn(square_placement_dict["E2"][0], square_placement_dict["E2"][1], "E2")
white_pawn5_group = p.sprite.GroupSingle()
white_pawn5_group.add(white_pawn5)
white_pawn5_group.draw(screen)

white_pawn6 = bd_pc.White_Pawn(square_placement_dict["F2"][0], square_placement_dict["F2"][1], "F2")
white_pawn6_group = p.sprite.GroupSingle()
white_pawn6_group.add(white_pawn6)
white_pawn6_group.draw(screen)

white_pawn7 = bd_pc.White_Pawn(square_placement_dict["G2"][0], square_placement_dict["G2"][1], "G2")
white_pawn7_group = p.sprite.GroupSingle()
white_pawn7_group.add(white_pawn7)
white_pawn7_group.draw(screen)

white_pawn8 = bd_pc.White_Pawn(square_placement_dict["H2"][0], square_placement_dict["H2"][1], "H2")
white_pawn8_group = p.sprite.GroupSingle()
white_pawn8_group.add(white_pawn8)
white_pawn8_group.draw(screen)



black_rook1 = bd_pc.Black_Rook(square_placement_dict["A8"][0], square_placement_dict["A8"][1], "A8")
black_rook1_group= p.sprite.GroupSingle()       # When a piece gets taken, can the group get changed to None, and the piece goes away?
black_rook1_group.add(black_rook1)
black_rook1_group.draw(screen)

black_knight1 = bd_pc.Black_Knight(square_placement_dict["B8"][0], square_placement_dict["B8"][1], "B8")
black_knight1_group = p.sprite.GroupSingle()
black_knight1_group.add(black_knight1)
black_knight1_group.draw(screen)

black_bishop1 = bd_pc.Black_Bishop(square_placement_dict["C8"][0], square_placement_dict["C8"][1], "C8")
black_bishop1_group = p.sprite.GroupSingle()
black_bishop1_group.add(black_bishop1)
black_bishop1_group.draw(screen)

black_queen = bd_pc.Black_Queen(square_placement_dict["D8"][0], square_placement_dict["D8"][1], "D8")
black_queen_group = p.sprite.GroupSingle()
black_queen_group.add(black_queen)
black_queen_group.draw(screen)

black_king = bd_pc.Black_King(square_placement_dict["E8"][0], square_placement_dict["E8"][1], "E8")
black_king_group = p.sprite.GroupSingle()
black_king_group.add(black_king)
black_king_group.draw(screen)

black_bishop2 = bd_pc.Black_Bishop(square_placement_dict["F8"][0], square_placement_dict["F8"][1], "F8")
black_bishop2_group = p.sprite.GroupSingle()
black_bishop2_group.add(black_bishop2)
black_bishop2_group.draw(screen)

black_knight2 = bd_pc.Black_Knight(square_placement_dict["G8"][0], square_placement_dict["G8"][1], "G8")
black_knight2_group = p.sprite.GroupSingle()
black_knight2_group.add(black_knight2)
black_knight2_group.draw(screen)

black_rook2 = bd_pc.Black_Rook(square_placement_dict["H8"][0], square_placement_dict["H8"][1], "H8")
black_rook2_group = p.sprite.GroupSingle()
black_rook2_group.add(black_rook2)
black_rook2_group.draw(screen)

black_pawn1 = bd_pc.Black_Pawn(square_placement_dict["A7"][0], square_placement_dict["A7"][1], "A7")
black_pawn1_group = p.sprite.GroupSingle()
black_pawn1_group.add(black_pawn1)
black_pawn1_group.draw(screen)

black_pawn2 = bd_pc.Black_Pawn(square_placement_dict["B7"][0], square_placement_dict["B7"][1], "B7")
black_pawn2_group = p.sprite.GroupSingle()
black_pawn2_group.add(black_pawn2)
black_pawn2_group.draw(screen)

black_pawn3 = bd_pc.Black_Pawn(square_placement_dict["C7"][0], square_placement_dict["C7"][1], "C7")
black_pawn3_group = p.sprite.GroupSingle()
black_pawn3_group.add(black_pawn3)
black_pawn3_group.draw(screen)

black_pawn4 = bd_pc.Black_Pawn(square_placement_dict["D7"][0], square_placement_dict["D7"][1], "D7")
black_pawn4_group = p.sprite.GroupSingle()
black_pawn4_group.add(black_pawn4)
black_pawn4_group.draw(screen)

black_pawn5 = bd_pc.Black_Pawn(square_placement_dict["E7"][0], square_placement_dict["E7"][1], "E7")
black_pawn5_group = p.sprite.GroupSingle()
black_pawn5_group.add(black_pawn5)
black_pawn5_group.draw(screen)

black_pawn6 = bd_pc.Black_Pawn(square_placement_dict["F7"][0], square_placement_dict["F7"][1], "F7")
black_pawn6_group = p.sprite.GroupSingle()
black_pawn6_group.add(black_pawn6)
black_pawn6_group.draw(screen)

black_pawn7 = bd_pc.Black_Pawn(square_placement_dict["G7"][0], square_placement_dict["G7"][1], "G7")
black_pawn7_group = p.sprite.GroupSingle()
black_pawn7_group.add(black_pawn7)
black_pawn7_group.draw(screen)

black_pawn8 = bd_pc.Black_Pawn(square_placement_dict["H7"][0], square_placement_dict["H7"][1], "H7")
black_pawn8_group = p.sprite.GroupSingle()
black_pawn8_group.add(black_pawn8)
black_pawn8_group.draw(screen)


print(datetime.now() - start)
#place_pieces()
while True:

    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            exit()
        if event.type == p.MOUSEBUTTONUP:
            mouse_pos = p.mouse.get_pos()
            for key, val in squares_dict:       # val is 1??
                print(val)
                if val.collidepoint:
                    print(mouse_pos)
                else:
                    print("Not clicking a square")


    p.display.update()

    clock.tick(max_fps)


# Current goals: be able to click a piece and move it. Possibly make the pieces sprites, learn about sprite class. might need to move the existing code for pieces to that class