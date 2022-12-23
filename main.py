import board_and_pieces as bd_pc
import pygame as p
from sys import exit
import math

board = bd_pc.GameState()
board_squares = board.create_board()
board_status = board.piece_position(board=board_squares, pieces=board.square_status)
screen_width = 1400
screen_height = 800
board_width = 73
board_height = 73
max_fps = 30
images_dict = {}
images_list = []

# takes the images from their respective png files based on what piece it is, skips if it is empty(no piece)
def load_images():
    for square in board_status:
        if board_status[square] != "empty":
            # for the future, I might add some buttons, etc, so the board won't take up the entire screen. remember to change the square size for scaling these images, or maybe the screen will get bigger and the board will stay the same size, with buttons on the sides.
            images_dict[board_status[square]] = p.image.load(f"C:/Users/mardo/Chess bot/images/{board_status[square]}.png")
          
        images_list.append(p.image.load(f"C:/Users/mardo/Chess bot/images/board/{square.upper()}.png"))


p.init()        # initializes pygame window
screen = p.display.set_mode((screen_width, screen_height))
screen.fill("gray34")
p.display.set_caption("Chess Bot")
clock = p.time.Clock()
# gamestate was initialized lines 4-15
load_images()

# function that draws the board (squares). Also adds the positioning of each square to a list, returns the list. This is used for calculations of where the piece should be placed in the square. Call only once
def create_board():
    x_y_square_placement = []
    x_square_placement = []
    y_square_placement = []
    for i in range(8):
        for val in range(8):
            x_movement = 80 + ((val + 1) * 73)

            y_movement = 692 - ((i + 1) * 73)

            screen.blit(images_list[val + (i * 8)], (x_movement, y_movement))
            x_y_square_placement.append((x_movement, y_movement))
    return x_y_square_placement

square_placement = create_board()

# function to place the pieces on the board. Takes an input of board, board position, dictionary of pieces and their respective files, and the square placement, places the pieces in their respective squares with some offset from the square position for the piece to be in the center of the square
def place_pieces(board_local=board_squares,current_position=board_status, images_and_files=images_dict, square_placement_on_screen=square_placement):
    current_square_index = 0
    for square in board_local:
        if current_position[square] != "empty":
            current_square_index = board_local.index(square)
            screen.blit(images_and_files[current_position[square].title()], (square_placement_on_screen[current_square_index][0] + 5, square_placement_on_screen[current_square_index][1] + 5))


while True:

    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            exit()
        elif event.type == p.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = p.mouse.get_pos()
            print(mouse_x, mouse_y)
    place_pieces()
    p.display.update()
    clock.tick(max_fps)


# Current goals: be able to click a piece and move it. Possibly make the pieces sprites, learn about sprite class. might need to move the existing code for pieces to that class
