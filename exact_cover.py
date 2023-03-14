import sys

from calendar_squares import get_calendar_squares
from placements import get_piece_placements
from compatible import get_compatabile_placement_indicies
from arrangements import get_valid_arrangements
from display import print_arrangement


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
