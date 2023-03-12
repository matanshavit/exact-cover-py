from empty_calendar import EMPTY_CALENDAR_SQUARES
from pieces import PIECE_ORIENTATION_SQUARES


# the squares that need to be covered for a certain day
# defining the exact cover problem
def get_calendar_squares(month, date, day):
    return [
        square for
        key, square in EMPTY_CALENDAR_SQUARES.items()
        if key not in (month, date, day)
    ]


def print_piece(piece_coordinates):
    for row in range(4):
        print("".join(
            "X" if (row, column) in piece_coordinates
            else "_"
            for column in range(4)
        ))
    print()


def print_all_piece_orientations():
    for i, piece_orientations in enumerate(PIECE_ORIENTATION_SQUARES):
        print(f'piece # {i + 1}\n')
        for piece_orientation in piece_orientations:
            print_piece(piece_orientation)
            print()


# print_all_piece_orientations()


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


# example:
# board_squares = get_calendar_squares('Mar', '12', 'Sun')
# placements = get_piece_placements(board_squares)
# lengths = [len(placement_options) for placement_options in placements]
# print(lengths)
# print(sum(lengths))


def get_every_placement_for_every_day():
    for month in [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
    ]:
        for day in [
            'Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat'
        ]:
            for date in [
                "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                "31",         
            ]:
                board_squares = get_calendar_squares(month, date, day)
                placements = get_piece_placements(board_squares)
                lengths = [len(placement_options) for placement_options in placements]


# timed - 24 seconds for every possible puzzle definition (combination of 3 squares)
# get_every_placement_for_every_day()


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
    compatible_indices = [
        [
            {} for _ in range(len(placements))    
        ] for placements in piece_placements
    ]

    for piece_index, placements in enumerate(piece_placements):
        for placement_index, placement in enumerate(placements):
            for other_piece_index, other_placements in enumerate(piece_placements[piece_index+1:], piece_index+1):
                for other_placement_index, other_placement in enumerate(other_placements):
                    compatible_indices[piece_index][placement_index][
                        (other_piece_index, other_placement_index)
                    ] = are_compatible(placement, other_placement)

    return compatible_indices


def placements_and_compatability(month, date, day):
    board_squares = get_calendar_squares(month, date, day)
    piece_placements = get_piece_placements(board_squares)
    compatible_indices = get_compatabile_placement_indicies(piece_placements)


placements_and_compatability("Mar", "12", "Sun")
