import pandas as pd

class GameState:

    # constructor used for creating the board later
    def __init__(self):
        self.files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
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
    "White Rook", "White Knight", "White Bishop", "White Queen", "White King", "White Bishop", "White Knight", "White Rook", \
    "White Pawn", "White Pawn", "White Pawn", "White Pawn", "White Pawn", "White Pawn", "White Pawn", "White Pawn", \
    "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", \
    "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", \
    "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", \
    "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", \
    "Black Pawn", "Black Pawn", "Black Pawn", "Black Pawn", "Black Pawn", "Black Pawn", "Black Pawn", "Black Pawn", \
    "Black Rook", "Black Knight", "Black Bishop", "Black Queen", "Black King", "Black Bishop", "Black Knight", "Black Rook"]

    # function that matches up each piece with its respective square on the board in a dictionary. Exepction if the board list and pieces list aren't the same length
    def piece_position(self, board, pieces=square_status):
        pieces_and_squares = {}
        board_list_len = len(board)
        pieces_list_len = len(pieces)
        if board_list_len is not pieces_list_len:
            raise Exception("The list containing all the squares on the board and the list containing what is on each square must be the same length")

        for square in range(board_list_len):
            pieces_and_squares[board[square]] = pieces[square]

        print(pieces_and_squares)
        return pieces_and_squares
