from pieces import PIECE_ORIENTATION_SQUARES


# bring the first coordinate of a piece to new coordinates
# return the cooridnates of the translated piece
def translate_piece_to(piece, new_coordinate):
    delta_row = new_coordinate[0] - piece[0][0]
    delta_column = new_coordinate[1] - piece[0][1]
    return [
        (coordinate[0] + delta_row, coordinate[1] + delta_column)
        for coordinate in piece
    ]


def is_piece_in_board(board_squares, piece_squares):
    return all(piece_square in board_squares for piece_square in piece_squares)


# get every placement of a piece on an empty board
# by translating the first square of the piece given to
# each empty square of the board, and checking if the rest of the piece is still in the board
def get_piece_placements(board_squares):
    def get_piece_orientations_placements(piece_orientations):
        result = []
        for piece_orientation in piece_orientations:
            for square in board_squares:
                translated_piece = translate_piece_to(piece_orientation, square)
                if is_piece_in_board(board_squares, translated_piece):
                    result.append(translated_piece)
        return result

    return [
        get_piece_orientations_placements(piece_orientations)
        for piece_orientations in PIECE_ORIENTATION_SQUARES
    ]
