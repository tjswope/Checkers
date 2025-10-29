# makes an actual copy of the object not just a reference
# to the object, boxes!
from copy import deepcopy

# constants used to determine who's turn it is.
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# current_board will be a Board object that represents a simulated move.
# depth - how far down our decision tree we want to go. We'll start at n and we'll count down to zero.
# max_player - a boolean that determines if the player is trying to minimize or maximize the score.
def minimax(current_board, depth, max_player):
    return current_board.evaluate(), current_board


# This function will simulate a move when the algorithm explores a branch of the decision tree.
def simulate_move(piece, move, board, skip):
  board.move(piece, move[0], move[1]) # move the piece on the board row and col
  if skip:
    board.remove(skip)

  return board


# This functions creates a deep copy of the current board, determines all possible moves that color can make, and returns a list that contains the boards that would result from the possible moves.
def get_all_moves(board, color):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)
    
    return moves
 
