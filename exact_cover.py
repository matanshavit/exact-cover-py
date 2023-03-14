from calendar_squares import get_calendar_squares
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


# returns True if two piece placements do not overlap
def are_compatible(piece_a, piece_b):
    for square in piece_a:
        if square in piece_b:
            return False
    return True


# checks piece placement of every combination of placements
# from two different pieces if they are compatible
# the result is stored at the index of the piece placement
# with a lower piece index to avaoid repetition
# (i.e. if piece 1 is checked with piece 3, the results are only at index 1)
def get_compatabile_placement_indicies(piece_placements):

    def compatabile_indicies_dict(piece_index, placement):
        return {
            (other_piece_index, other_placement_index): are_compatible(placement, other_placement)
            for other_piece_index, other_placements in enumerate(piece_placements[piece_index+1:], piece_index+1)
            for other_placement_index, other_placement in enumerate(other_placements)
        }

    return [
        [
            compatabile_indicies_dict(piece_index, placement)
            for placement in placements
        ]
        for piece_index, placements in enumerate(piece_placements)
    ]


# example:
# board_squares = get_calendar_squares('Mar', '12', 'Sun')
# placements = get_piece_placements(board_squares)
# lengths = [len(placement_options) for placement_options in placements]
# print(lengths)
# print(sum(lengths))
# compatabile_indicies = get_compatabile_placement_indicies(placements)
# lengths = [
#     sum(
#         len(placement_compatabile_indicies)
#         for placement_compatabile_indicies in piece_compatabile_indicies
#     )
#     for piece_compatabile_indicies in compatabile_indicies
# ]
# print(lengths)
# print(sum(lengths))


def placements_and_compatability(month, date, day):
    board_squares = get_calendar_squares(month, date, day)
    piece_placements = get_piece_placements(board_squares)
    compatible_indices = get_compatabile_placement_indicies(piece_placements)


placements_and_compatability("Mar", "12", "Sun")
