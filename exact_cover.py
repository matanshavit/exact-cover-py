import random
import sys

from calendar_squares import get_calendar_squares
from pieces import PIECE_ORIENTATION_SQUARES
from display import print_arrangement


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


# return valid arrangements of piece placements without overlaps
# return value is a list of placement indices in order of piece index
# for example, a return value of [10, 11, 12, ...]
# represents placements [0][10], [1][11], [2][12], ...
def get_valid_arrangements(compatible_indices, return_first, random_order):
    last_piece_index = len(compatible_indices) - 1

    def _get_valid_arrangements(partial_arrangement, remaining_possible_placement_indices):
        full_arrangements = []
        next_piece_index = len(partial_arrangement)
        pieces_compatible_indices = compatible_indices[next_piece_index]
        if random_order:
            random.shuffle(remaining_possible_placement_indices[0])
        for next_placement_index in remaining_possible_placement_indices[0]:
            new_arrangement = partial_arrangement + [next_placement_index]

            # print progress tracking by first and second piece
            if next_piece_index == 1:
                print(new_arrangement)

            if next_piece_index == last_piece_index:
                # the arrangement is done and valid
                print(new_arrangement)
                full_arrangements.append(new_arrangement)
                if return_first:
                    return full_arrangements
                continue

            placement_compatible_indices = pieces_compatible_indices[next_placement_index]
            next_possible_placements = []
            for future_piece_index, future_placement_indicies in enumerate(
                remaining_possible_placement_indices[1:], next_piece_index + 1
            ):
                next_possible_placements.append([
                    future_placement_index
                    for future_placement_index in future_placement_indicies
                    if placement_compatible_indices[(future_piece_index, future_placement_index)]
                ])
            if any(
                len(next_possible_placements_for_piece) == 0
                for next_possible_placements_for_piece in next_possible_placements
            ):
                # if placements eliminate all possiblities for a future piece,
                # there is no valid arrangement for this placement
                continue

            full_arrangements = full_arrangements + _get_valid_arrangements(new_arrangement, next_possible_placements)
            if return_first and len(full_arrangements) > 0:
                return full_arrangements

        return full_arrangements

    possible_placement_indices = [
        list(range(len(possible_placement_indices)))
        for possible_placement_indices in compatible_indices
    ]
    return _get_valid_arrangements([], possible_placement_indices)


def find_arrangements_for_date(month, date, day, return_first=True, random_order=True):
    board_squares = get_calendar_squares(month, date, day)
    piece_placements = get_piece_placements(board_squares)
    compatible_indices = get_compatabile_placement_indicies(piece_placements)
    valid_arrangements = get_valid_arrangements(compatible_indices, return_first, random_order)
    return [
        [
            piece_placements[piece][placement]
            for piece, placement in enumerate(arrangement)
        ]
        for arrangement in valid_arrangements
    ]


def print_arrangements_for_date(month, date, day):
    arrangements = find_arrangements_for_date(month, date, day)
    if len(arrangements) > 1:
        print()
        print(f'{len(arrangements)} valid arrangements')
    for arrangement in arrangements:
        print()
        print_arrangement(arrangement)

print_arrangements_for_date(sys.argv[1], sys.argv[2], sys.argv[3])
