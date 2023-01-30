
import pygame as p


class ExtendedGroupSingle(p.sprite.GroupSingle):

    def change_piece_coordinates(self, arg1, arg2):       # allows the method to be called on a GroupSingle
        for spr in self.sprites():

            if hasattr(spr, "change_piece_coordinates"):
               spr.change_piece_coordinates(arg1, arg2)


class GameState:

    # constructor used for creating the board later
    def __init__(self):
        self.files = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.ranks = [1, 2, 3, 4, 5, 6, 7, 8]

    # this function creates the squares on the board, a1-h8
    def create_board(self):
        board_squares = []
        for rank in self.ranks:
            for file in self.files:
                board_squares.append(f"{file}{rank}")
        return board_squares

    # dictionary that tracks the status of each square. a1-h8, left to right, bottom to top on the board corresponds to left to right, top to bottom in the list
    square_status = [
    "White_Rook", "White_Knight", "White_Bishop", "White_Queen", "White_King", "White_Bishop", "White_Knight", "White_Rook", \
    "White_Pawn", "White_Pawn", "White_Pawn", "White_Pawn", "White_Pawn", "White_Pawn", "White_Pawn", "White_Pawn", \
    "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", \
    "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", \
    "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", \
    "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", \
    "Black_Pawn", "Black_Pawn", "Black_Pawn", "Black_Pawn", "Black_Pawn", "Black_Pawn", "Black_Pawn", "Black_Pawn", \
    "Black_Rook", "Black_Knight", "Black_Bishop", "Black_Queen", "Black_King", "Black_Bishop", "Black_Knight", "Black_Rook"]

    # function that matches up each piece with its respective square on the board in a dictionary. Exepction if the board list and pieces list aren't the same length
    def piece_position(self, board, pieces=square_status):
        pieces_and_squares = {}
        board_list_len = len(board)
        pieces_list_len = len(pieces)
        if board_list_len is not pieces_list_len:
            raise Exception("The list containing all the squares on the board and the list containing what is on each square must be the same length")

        for square in range(board_list_len):
            pieces_and_squares[board[square]] = pieces[square]

        #print(pieces_and_squares)
        return pieces_and_squares


# Board class. Used for drawing the pieces in main.py, as well as for moving the pieces
class Board(p.sprite.Sprite):

    # constructor for loading the image file of the square for drawing in the future, determining x and y position, create rect over the image for collision detection. Input of (self, square, x_pos, y_pos)
    def __init__(self, square, x_y_pos):
        super().__init__()

        self.square = square        # square should be in format FILErank (example: A1)
        self.x_y_pos = x_y_pos

        # load image of the square
        self.image = p.image.load(f"images/board/{square}.png")

        # create rect, align it
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x_y_pos)

        # no need for an update() right now, possibly in the future
        # for moving the pieces, be sure to change board status in the Gamestate() class, either here or in main.py

                


# Pieces superclass. Used as a superclass to store methods and variables to be used in all the individual piece classes
# Movement logic will most likely be in the subclasses
class Pieces(p.sprite.Sprite):

    # constructor for getting the x and y positions, piece name, point value, square the piece is on. This class should never be created, only the subclasses. Do not load image in this class, do it in the other classes
    def __init__(self, piece, x_pos, y_pos, square_current, point_value):
        super().__init__()

        self.piece = piece
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.square_current = square_current
        self.point_value = point_value


    def change_piece_coordinates(self, new_x, new_y):
        self.x_pos = new_x
        self.y_pos = new_y

        self.rect.topleft = (self.x_pos + 3, self.y_pos + 5)


    # This class is incomplete. For now, there is only the constructor, but methods for moving pieces, etc need to be added in the future


# White pieces subclasses
# White Rook class. Inherits from the Pieces class
class White_Rook(Pieces):

    # constructor needs all the inputs of the parent class, and load the image and creates a rect. 
    def __init__(self, x_pos, y_pos, square_current):
        super().__init__("White_Rook", x_pos, y_pos, square_current, 5)

        self.image = p.image.load(f"images/White_Rook.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos + 3, y_pos + 5)

    # This class is incomplete. For now, there is only the constructor, but methods for finding legal moves, etc need to be added in the future


# White Knight class. Inherits from the Pieces class
class White_Knight(Pieces):

    # constructor needs all the inputs of the parent class, and load the image and creates a rect. 
    def __init__(self, x_pos, y_pos, square_current):
        super().__init__("White_Knight", x_pos, y_pos, square_current, 3)

        self.image = p.image.load(f"images/White_Knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos + 3, y_pos + 5)

    # This class is incomplete. For now, there is only the constructor, but methods for finding legal moves, etc need to be added in the future


# White Bishop class. Inherits from the Pieces class
class White_Bishop(Pieces):

    # constructor needs all the inputs of the parent class, and load the image and creates a rect. 
    def __init__(self, x_pos, y_pos, square_current):
        super().__init__("White_Bishop", x_pos, y_pos, square_current, 3)

        self.image = p.image.load(f"images/White_Bishop.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos + 3, y_pos + 5)

    # This class is incomplete. For now, there is only the constructor, but methods for finding legal moves, etc need to be added in the future


# White Queen class. Inherits from the Pieces class
class White_Queen(Pieces):

    # constructor needs all the inputs of the parent class, and load the image and creates a rect. 
    def __init__(self, x_pos, y_pos, square_current):
        super().__init__("White_Queen", x_pos, y_pos, square_current, 9)

        self.image = p.image.load(f"images/White_Queen.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos + 3, y_pos + 5)

    # This class is incomplete. For now, there is only the constructor, but methods for finding legal moves, etc need to be added in the future


# White King class. Inherits from the Pieces class
class White_King(Pieces):

    # constructor needs all the inputs of the parent class, and load the image and creates a rect. 
    def __init__(self, x_pos, y_pos, square_current):
        super().__init__("White_King", x_pos, y_pos, square_current, 0)

        self.image = p.image.load(f"images/White_King.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos + 3, y_pos + 5)

    # This class is incomplete. For now, there is only the constructor, but methods for finding legal moves, etc need to be added in the future


# White Pawn class. Inherits from the Pieces class
class White_Pawn(Pieces):

    # constructor needs all the inputs of the parent class, and load the image and creates a rect. 
    def __init__(self, x_pos, y_pos, square_current):
        super().__init__("White_Pawn", x_pos, y_pos, square_current, 1)

        self.image = p.image.load(f"images/White_Pawn.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos + 3, y_pos + 5)

    # This class is incomplete. For now, there is only the constructor, but methods for finding legal moves, etc need to be added in the future



# Black pieces subclasses
# Black Rook class. Inherits from the Pieces class
class Black_Rook(Pieces):

    # constructor needs all the inputs of the parent class, and load the image and creates a rect. 
    def __init__(self, x_pos, y_pos, square_current):
        super().__init__("Black_Rook", x_pos, y_pos, square_current, -5)

        self.image = p.image.load(f"images/Black_Rook.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos + 3, y_pos + 5)

    # This class is incomplete. For now, there is only the constructor, but methods for finding legal moves, etc need to be added in the future


# Black Knight class. Inherits from the Pieces class
class Black_Knight(Pieces):

    # constructor needs all the inputs of the parent class, and load the image and creates a rect. 
    def __init__(self, x_pos, y_pos, square_current):
        super().__init__("Black_Knight", x_pos, y_pos, square_current, -3)

        self.image = p.image.load(f"images/Black_Knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos + 3, y_pos + 5)

    # This class is incomplete. For now, there is only the constructor, but methods for finding legal moves, etc need to be added in the future


# Black Bishop class. Inherits from the Pieces class
class Black_Bishop(Pieces):

    # constructor needs all the inputs of the parent class, and load the image and creates a rect. 
    def __init__(self, x_pos, y_pos, square_current):
        super().__init__("Black_Bishop", x_pos, y_pos, square_current, -3)

        self.image = p.image.load(f"images/Black_Bishop.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos + 3, y_pos + 5)

    # This class is incomplete. For now, there is only the constructor, but methods for finding legal moves, etc need to be added in the future


# Black Queen class. Inherits from the Pieces class
class Black_Queen(Pieces):

    # constructor needs all the inputs of the parent class, and load the image and creates a rect. 
    def __init__(self, x_pos, y_pos, square_current):
        super().__init__("Black_Queen", x_pos, y_pos, square_current, -9)

        self.image = p.image.load(f"images/Black_Queen.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos + 3, y_pos + 5)

    # This class is incomplete. For now, there is only the constructor, but methods for finding legal moves, etc need to be added in the future


# Black King class. Inherits from the Pieces class
class Black_King(Pieces):

    # constructor needs all the inputs of the parent class, and load the image and creates a rect. 
    def __init__(self, x_pos, y_pos, square_current):
        super().__init__("Black_King", x_pos, y_pos, square_current, 0)

        self.image = p.image.load(f"images/Black_King.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos + 3, y_pos + 5)

    # This class is incomplete. For now, there is only the constructor, but methods for finding legal moves, etc need to be added in the future


# Black Pawn class. Inherits from the Pieces class
class Black_Pawn(Pieces):

    # constructor needs all the inputs of the parent class, and load the image and creates a rect. 
    def __init__(self, x_pos, y_pos, square_current):
        super().__init__("Black_Pawn", x_pos, y_pos, square_current, -1)

        self.image = p.image.load(f"images/Black_Pawn.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos + 3, y_pos + 5)

    # This class is incomplete. For now, there is only the constructor, but methods for finding legal moves, etc need to be added in the future


class Hightlighted_Square:

    def __init__(self, x_pos, y_pos):
        self.image = p.image.load("images/highlighted_square.png")
        self.rect = self.image.get_rect()
        self.rect.top_left = (x_pos + 3, y_pos + 5)