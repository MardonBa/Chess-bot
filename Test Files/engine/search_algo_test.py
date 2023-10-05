import chess_game_logic_test as cgl
from copy import deepcopy

class SearchAlgorithm: 
    def __init__(self, board_status, board_squares, previous_board_status, white_king_has_moved, white_h1_rook_has_moved, white_a1_rook_has_move, black_king_has_moved, black_h8_rook_has_moved, black_a8_rook_has_moved, evaluation_function):
        self.previous_board_status = previous_board_status
        self.board_status = board_status
        self.board_squares = board_squares
        self.white_king_has_moved = white_king_has_moved
        self.white_h1_rook_has_moved = white_h1_rook_has_moved
        self.white_a1_rook_has_moved = white_a1_rook_has_move
        self.black_king_has_moved = black_king_has_moved
        self.black_h8_rook_has_moved = black_h8_rook_has_moved
        self.black_a8_rook_has_moved = black_a8_rook_has_moved
        self.evaluation_function = evaluation_function ## Will eventually be the neural net
    
    def _call_movement_function(self, piece, square):
        if piece == "White_Rook":
            possible_moves = cgl.move_rook("White", square, self.board_squares, self.board_status, self.previous_board_status, self.white_king_has_moved, self.white_h1_rook_has_moved, self.white_a1_rook_has_moved)

        elif piece == "White_Knight":
            possible_moves = cgl.move_knight("White", square, self.board_squares, self.board_status, self.previous_board_status, self.white_king_has_moved, self.white_h1_rook_has_moved, self.white_a1_rook_has_moved)

        elif piece == "White_Bishop":
            possible_moves = cgl.move_bishop("White", square, self.board_squares, self.board_status, self.previous_board_status, self.white_king_has_moved, self.white_h1_rook_has_moved, self.white_a1_rook_has_moved)

        elif piece == "White_Queen":
            possible_moves = cgl.move_queen("White", square, self.board_squares, self.board_status, self.previous_board_status, self.white_king_has_moved, self.white_h1_rook_has_moved, self.white_a1_rook_has_moved)

        elif piece == "White_King":
            possible_moves = cgl.move_king("White", square, self.board_squares, self.board_status, self.previous_board_status, self.white_king_has_moved, self.white_h1_rook_has_moved, self.white_a1_rook_has_moved)

        elif piece == "White_Pawn":
            possible_moves, white_en_passant = cgl.move_pawn("White", square, self.board_squares, self.board_status, self.previous_board_status, self.white_king_has_moved, self.white_h1_rook_has_moved, self.white_a1_rook_has_moved, first_move=True if "2" in square else False)      # make sure to add code for determining if captures are possible



        elif piece == "Black_Rook":
            possible_moves = cgl.move_rook("Black", square, self.board_squares, self.board_status, self.previous_board_status, self.black_king_has_moved, self.black_h8_rook_has_moved, self.black_a8_rook_has_moved)

        elif piece == "Black_Knight":
            possible_moves = cgl.move_knight("Black", square, self.board_squares, self.board_status, self.previous_board_status, self.black_king_has_moved, self.black_h8_rook_has_moved, self.black_a8_rook_has_moved)

        elif piece == "Black_Bishop":
            possible_moves = cgl.move_bishop("Black", square, self.board_squares, self.board_status,self.previous_board_status, self.black_king_has_moved, self.black_h8_rook_has_moved, self.black_a8_rook_has_moved)

        elif piece == "Black_Queen":
            possible_moves = cgl.move_queen("Black", square, self.board_squares, self.board_status, self.previous_board_status, self.black_king_has_moved, self.black_h8_rook_has_moved, self.black_a8_rook_has_moved)

        elif piece == "Black_King":
            possible_moves = cgl.move_king("Black", square, self.board_squares, self.board_status, self.previous_board_status, self.black_king_has_moved, self.black_h8_rook_has_moved, self.black_a8_rook_has_moved)

        elif piece == "Black_Pawn":
            possible_moves, black_en_passant = cgl.move_pawn("Black", square, self.board_squares, self.board_status, self.previous_board_status, self.black_king_has_moved, self.black_h8_rook_has_moved, self.black_a8_rook_has_moved, first_move=True if "7" in square else False)     # make sure to add code for determining if captures are possible
            
        return possible_moves


    def _find_legal_moves(self): ## Inputs should be things that need to be tracked about previous movements
        self.possible_moves = []
        ## Iterate over the board to see what pieces are on the board
        for key, value in self.board_status:
            if value != "empty":
                piece_moves = self._call_movement_function(key, value)
                for move in piece_moves:
                    self.possible_moves.append((value, key, move)) ## Adds the piece, original square, new square to the possible_moves list so that that can be used to update the board status for each recursive call

    def _check_game_is_over(self):
        return True

    def minimax(self, color, is_maximizing, depth, board_status):
        ## Base case: game is over OR depth has been reached
        if self._check_game_is_over() or depth == 0:
            return [self.evaluation_function(), ""] ## Evaluate the board at that point
        
        ## If the game isn't over OR the depth hasn't been reached
        if is_maximizing == True:
            best_value = -float('Inf')
        else:
            best_value = float('Inf')

        for move in self.possible_moves:
            next_board_status = deepcopy(board_status)
            ## Changes the next_board_status so that the move being selected is made on the new status
            next_board_status[move[1]] = 'empty'
            next_board_status[move[2]] = move[0]

            next_color = "White" if color == "Black" else "Black"
            hypothetical_value = self.minimax(next_color, not is_maximizing, depth-1, next_board_status)[0]

            if is_maximizing == True and hypothetical_value > best_value:
                best_value = hypothetical_value
                best_move = move
            elif is_maximizing == False and hypothetical_value < best_value:
                best_value = hypothetical_value
                best_move = move
            
        return [best_value, best_move]

