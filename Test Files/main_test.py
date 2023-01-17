from datetime import datetime
start = datetime.now()
import board_and_pieces_test as bd_pc
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
def board_init():
    square_groups = [
    "A1_group", "B1_group", "C1_group", "D1_group", "E1_group", "F1_group", "G1_group", "H1_group", \
    "A2_group", "B2_group", "C2_group", "D2_group", "E2_group", "F2_gruop", "G2_group", "H2_group", \
    "A3_group", "B3_group", "C3_group", "D3_group", "E3_group", "F3_group", "G3_group", "H3_group", \
    "A4_group", "B4_group", "C4_group", "D4_group", "E4_group", "F4_group", "G4_group", "H4_group", \
    "A5_group", "B5_group", "C5_group", "D5_group", "E5_group", "F5_group", "G5_group", "H5_group", \
    "A6_group", "B6_group", "C6_group", "D6_group", "E6_group", "F6_group", "G6_group", "H6_group", \
    "A7_group", "B7_group", "C7_group", "D7_group", "E7_group", "F7_group", "G7_group", "H7_group", \
    "A8_group", "B8_group", "C8_group", "D8_group", "E8_group", "F8_group", "G8_group", "H8_group" ]

    square_group = p.sprite.Group()
    for i in range(len(board_squares)):
        square = board_squares[i]
        new_square = bd_pc.Board(square, square_placement[i])
        square_group.add(new_square)
    square_group.draw(screen)

#board_init()

A1 = bd_pc.Board("A1", square_placement[0])
A1_group = p.sprite.GroupSingle()
A1_group.add(A1)
A1_group.draw(screen)
B1 = bd_pc.Board("B1", square_placement[1])
B1_group = p.sprite.GroupSingle()
B1_group.add(B1)
B1_group.draw(screen)
C1 = bd_pc.Board("C1", square_placement[2])
C1_group = p.sprite.GroupSingle()
C1_group.add(C1)
C1_group.draw(screen)
D1 = bd_pc.Board("D1", square_placement[3])
D1_group = p.sprite.GroupSingle()
D1_group.add(D1)
D1_group.draw(screen)
E1 = bd_pc.Board("E1", square_placement[4])
E1_group = p.sprite.GroupSingle()
E1_group.add(E1)
E1_group.draw(screen)
F1 = bd_pc.Board("F1", square_placement[5])
F1_group = p.sprite.GroupSingle()
F1_group.add(F1)
F1_group.draw(screen)
G1 = bd_pc.Board("G1", square_placement[6])
G1_group = p.sprite.GroupSingle()
G1_group.add(G1)
G1_group.draw(screen)
H1 = bd_pc.Board("H1", square_placement[7])
H1_group = p.sprite.GroupSingle()
H1_group.add(H1)
H1_group.draw(screen)

A2 = bd_pc.Board("A2", square_placement[8])
A2_group = p.sprite.GroupSingle()
A2_group.add(A2)
A2_group.draw(screen)
B2 = bd_pc.Board("B2", square_placement[9])
B2_group = p.sprite.GroupSingle()
B2_group.add(B2)
B2_group.draw(screen)
C2 = bd_pc.Board("C2", square_placement[10])
C2_group = p.sprite.GroupSingle()
C2_group.add(C2)
C2_group.draw(screen)
D2 = bd_pc.Board("D2", square_placement[11])
D2_group = p.sprite.GroupSingle()
D2_group.add(D2)
D2_group.draw(screen)
E2 = bd_pc.Board("E2", square_placement[12])
E2_group = p.sprite.GroupSingle()
E2_group.add(E2)
E2_group.draw(screen)
F2 = bd_pc.Board("F2", square_placement[13])
F2_group = p.sprite.GroupSingle()
F2_group.add(F2)
F2_group.draw(screen)
G2 = bd_pc.Board("G2", square_placement[14])
G2_group = p.sprite.GroupSingle()
G2_group.add(G2)
G2_group.draw(screen)
H2 = bd_pc.Board("H2", square_placement[15])
H2_group = p.sprite.GroupSingle()
H2_group.add(H2)
H2_group.draw(screen)

A3 = bd_pc.Board("A3", square_placement[16])
A3_group = p.sprite.GroupSingle()
A3_group.add(A3)
A3_group.draw(screen)
B3 = bd_pc.Board("B3", square_placement[17])
B3_group = p.sprite.GroupSingle()
B3_group.add(B3)
B3_group.draw(screen)
C3 = bd_pc.Board("C3", square_placement[18])
C3_group = p.sprite.GroupSingle()
C3_group.add(C3)
C3_group.draw(screen)
D3 = bd_pc.Board("d3", square_placement[19])
D3_group = p.sprite.GroupSingle()
D3_group.add(D3)
D3_group.draw(screen)
E3 = bd_pc.Board("E3", square_placement[20])
E3_group = p.sprite.GroupSingle()
E3_group.add(E3)
E3_group.draw(screen)
F3 = bd_pc.Board("F3", square_placement[21])
F3_group = p.sprite.GroupSingle()
F3_group.add(F3)
F3_group.draw(screen)
G3 = bd_pc.Board("G3", square_placement[22])
G3_group = p.sprite.GroupSingle()
G3_group.add(G3)
G3_group.draw(screen)
H3 = bd_pc.Board("H3", square_placement[23])
H3_group = p.sprite.GroupSingle()
H3_group.add(H3)
H3_group.draw(screen)

A4 = bd_pc.Board("A4", square_placement[24])
A4_group = p.sprite.GroupSingle()
A4_group.add(A4)
A4_group.draw(screen)
B4 = bd_pc.Board("B4", square_placement[25])
B4_group = p.sprite.GroupSingle()
B4_group.add(B4)
B4_group.draw(screen)
C4 = bd_pc.Board("C4", square_placement[26])
C4_group = p.sprite.GroupSingle()
C4_group.add(C4)
C4_group.draw(screen)
D4 = bd_pc.Board("D4", square_placement[27])
D4_group = p.sprite.GroupSingle()
D4_group.add(D4)
D4_group.draw(screen)
E4 = bd_pc.Board("E4", square_placement[28])
E4_group = p.sprite.GroupSingle()
E4_group.add(E4)
E4_group.draw(screen)
F4 = bd_pc.Board("F4", square_placement[29])
F4_group = p.sprite.GroupSingle()
F4_group.add(F4)
F4_group.draw(screen)
G4 = bd_pc.Board("G4", square_placement[30])
G4_group = p.sprite.GroupSingle()
G4_group.add(G4)
G4_group.draw(screen)
H4 = bd_pc.Board("H4", square_placement[31])
H4_group = p.sprite.GroupSingle()
H4_group.add(H4)
H4_group.draw(screen)

A5 = bd_pc.Board("A5", square_placement[32])
A5_group = p.sprite.GroupSingle()
A5_group.add(A5)
A5_group.draw(screen)
B5 = bd_pc.Board("B5", square_placement[33])
B5_group = p.sprite.GroupSingle()
B5_group.add(B5)
B5_group.draw(screen)
C5 = bd_pc.Board("C5", square_placement[34])
C5_group = p.sprite.GroupSingle()
C5_group.add(C5)
C5_group.draw(screen)
D5 = bd_pc.Board("D5", square_placement[35])
D5_group = p.sprite.GroupSingle()
D5_group.add(D5)
D5_group.draw(screen)
E5 = bd_pc.Board("E5", square_placement[36])
E5_group = p.sprite.GroupSingle()
E5_group.add(E5)
E5_group.draw(screen)
F5 = bd_pc.Board("F5", square_placement[37])
F5_group = p.sprite.GroupSingle()
F5_group.add(F5)
F5_group.draw(screen)
G5 = bd_pc.Board("G5", square_placement[38])
G5_group = p.sprite.GroupSingle()
G5_group.add(G5)
G5_group.draw(screen)
H5 = bd_pc.Board("H5", square_placement[39])
H5_group = p.sprite.GroupSingle()
H5_group.add(H5)
H5_group.draw(screen)

A6 = bd_pc.Board("A6", square_placement[40])
A6_group = p.sprite.GroupSingle()
A6_group.add(A6)
A6_group.draw(screen)
B6 = bd_pc.Board("B6", square_placement[41])
B6_group = p.sprite.GroupSingle()
B6_group.add(B6)
B6_group.draw(screen)
C6 = bd_pc.Board("C6", square_placement[42])
C6_group = p.sprite.GroupSingle()
C6_group.add(C6)
C6_group.draw(screen)
D6 = bd_pc.Board("D6", square_placement[43])
D6_group = p.sprite.GroupSingle()
D6_group.add(D6)
D6_group.draw(screen)
E6 = bd_pc.Board("E6", square_placement[44])
E6_group = p.sprite.GroupSingle()
E6_group.add(E6)
E6_group.draw(screen)
F6 = bd_pc.Board("F6", square_placement[45])
F6_group = p.sprite.GroupSingle()
F6_group.add(F6)
F6_group.draw(screen)
G6 = bd_pc.Board("G6", square_placement[46])
G6_group = p.sprite.GroupSingle()
G6_group.add(G6)
G6_group.draw(screen)
H6 = bd_pc.Board("H6", square_placement[47])
H6_group = p.sprite.GroupSingle()
H6_group.add(H6)
H6_group.draw(screen)

A7 = bd_pc.Board("A7", square_placement[48])
A7_group = p.sprite.GroupSingle()
A7_group.add(A7)
A7_group.draw(screen)
B7 = bd_pc.Board("B7", square_placement[49])
B7_group = p.sprite.GroupSingle()
B7_group.add(B7)
B7_group.draw(screen)
C7 = bd_pc.Board("C7", square_placement[50])
C7_group = p.sprite.GroupSingle()
C7_group.add(C7)
C7_group.draw(screen)
D7 = bd_pc.Board("D7", square_placement[51])
D7_group = p.sprite.GroupSingle()
D7_group.add(D7)
D7_group.draw(screen)
E7 = bd_pc.Board("E7", square_placement[52])
E7_group = p.sprite.GroupSingle()
E7_group.add(E7)
E7_group.draw(screen)
F7 = bd_pc.Board("F7", square_placement[53])
F7_group = p.sprite.GroupSingle()
F7_group.add(F7)
F7_group.draw(screen)
G7 = bd_pc.Board("G7", square_placement[54])
G7_group = p.sprite.GroupSingle()
G7_group.add(G7)
G7_group.draw(screen)
H7 = bd_pc.Board("H7", square_placement[55])
H7_group = p.sprite.GroupSingle()
H7_group.add(H7)
H7_group.draw(screen)

A8 = bd_pc.Board("A8", square_placement[56])
A8_group = p.sprite.GroupSingle()
A8_group.add(A8)
A8_group.draw(screen)
B8 = bd_pc.Board("B8", square_placement[57])
B8_group = p.sprite.GroupSingle()
B8_group.add(B8)
B8_group.draw(screen)
C8 = bd_pc.Board("C8", square_placement[58])
C8_group = p.sprite.GroupSingle()
C8_group.add(C8)
C8_group.draw(screen)
D8 = bd_pc.Board("D8", square_placement[59])
D8_group = p.sprite.GroupSingle()
D8_group.add(D8)
D8_group.draw(screen)
E8 = bd_pc.Board("E8", square_placement[60])
E8_group = p.sprite.GroupSingle()
E8_group.add(E8)
E8_group.draw(screen)
F8 = bd_pc.Board("F8", square_placement[61])
F8_group = p.sprite.GroupSingle()
F8_group.add(F8)
F8_group.draw(screen)
G8 = bd_pc.Board("G8", square_placement[62])
G8_group = p.sprite.GroupSingle()
G8_group.add(G8)
G8_group.draw(screen)
H8 = bd_pc.Board("H8", square_placement[63])
H8_group = p.sprite.GroupSingle()
H8_group.add(H8)
H8_group.draw(screen)




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


    p.display.update()

    clock.tick(max_fps)


# Current goals: be able to click a piece and move it. Possibly make the pieces sprites, learn about sprite class. might need to move the existing code for pieces to that class