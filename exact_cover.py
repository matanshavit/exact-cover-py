# this is the shape of the empty puzzle

# +------+------+------+------+------+------+
# | Jan  | Feb  | Mar  | Apr  | May  | Jun  |
# +------+------+------+------+------+------+
# | Jan  | Feb  | Mar  | Apr  | May  | Jun  |
# +------+------+------+------+------+------+------+
# | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
# +------+------+------+------+------+------+------+
# | 8    | 9    | 10   | 11   | 12   | 13   | 14   |
# +------+------+------+------+------+------+------+
# | 15   | 16   | 17   | 18   | 19   | 20   | 21   |
# +------+------+------+------+------+------+------+
# | 22   | 23   | 24   | 25   | 26   | 27   | 28   |
# +------+------+------+------+------+------+------+
# | 29   | 30   | 31   | Sun  | Mon  | Tues | Wed  |
# +------+------+------+------+------+------+------+
#                             | Thur | Fri  | Sat  |
#                             +------+------+------+

EMPTY_CALENDAR_SQUARES = {
        "Jan": (0, 0),
        "Feb": (0, 1),
        "Mar": (0, 2),
        "Apr": (0, 3),
        "May": (0, 4),
        "Jun": (0, 5),
        "Jul": (1, 0),
        "Aug": (1, 1),
        "Sep": (1, 2),
        "Oct": (1, 3),
        "Nov": (1, 4),
        "Dec": (1, 5),

        "1": (2, 0),
        "2": (2, 1),
        "3": (2, 2),
        "4": (2, 3),
        "5": (2, 4),
        "6": (2, 5),
        "7": (2, 6),
        "8": (3, 0),
        "9": (3, 1),
        "10": (3, 2),
        "11": (3, 3),
        "12": (3, 4),
        "13": (3, 5),
        "14": (3, 6),
        "15": (4, 0),
        "16": (4, 1),
        "17": (4, 2),
        "18": (4, 3),
        "19": (4, 4),
        "20": (4, 5),
        "21": (4, 6),
        "22": (5, 0),
        "23": (5, 1),
        "24": (5, 2),
        "25": (5, 3),
        "26": (5, 4),
        "27": (5, 5),
        "28": (5, 6),
        "29": (6, 0),
        "30": (6, 1),
        "31": (6, 2),

        "Sun": (6, 3),
        "Mon": (6, 4),
        "Tues": (6, 5),
        "Wed": (6, 6),
        "Thur": (6, 4),
        "Fri": (6, 5),
        "Sat": (6, 6),
    }


# the squares that need to be covered for a certain day
# defining the exact cover problem
def get_calendar_squares(month, date, day):
    return [
        square for
        key, square in EMPTY_CALENDAR_SQUARES.items()
        if key not in (month, date, day)
    ]


# these are the shapes of the pieces
# the reflections and rotations are included

# future work may include calculating the reflections and rotations,
# and eliminating repeated orientations do to symetries

PIECE_ORIENTATION_SQUARES = [
    # +--+--+--+--+
    # |  |  |  |  |
    # +--+--+--+--+
    [
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
    ],
    # +--+--+--+
    # |  |  |  |
    # +--+--+--+
    # |  |
    # +--+
    [ #2, 8 orientations
        [(0, 0), (0, 1), (0, 2), (1, 0)],
        [(0, 0), (0, 1), (0, 2), (1, 2)],
        [(0, 0), (1, 0), (1, 1), (1, 2)],
        [(0, 2), (1, 0), (1, 1), (1, 2)],
        [(0, 0), (0, 1), (1, 0), (2, 0)],
        [(0, 0), (0, 1), (1, 1), (2, 1)],
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        [(0, 1), (1, 1), (2, 0), (2, 1)],
    ],
    # +--+--+--+--+
    # |  |  |  |  |
    # +--+--+--+--+
    # |  |
    # +--+
    [ #3, 8 orientations
        [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0)],
        [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3)],
        [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3)],
        [(0, 3), (1, 0), (1, 1), (1, 2), (1, 3)],
        [(0, 0), (0, 1), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1)],
        [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)],
        [(0, 1), (1, 1), (2, 1), (3, 0), (3, 1)],
    ],
    #    +--+--+--+
    #    |  |  |  | 
    # +--+--+--+--+
    # |  |  |
    # +--+--+
    [ #4, 8 orientations
        [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)],
        [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3)],
        [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2)],
        [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1)],
        [(0, 1), (1, 0), (1, 1), (2, 0), (3, 0)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1)],
        [(0, 1), (1, 1), (2, 0), (2, 1), (3, 0)],
    ],
    # +--+--+--+
    # |  |  |  |
    # +--+--+--+
    # |  |
    # +--+
    # |  |
    # +--+
    [ #5, 4 orientations
        [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)],
        [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)],
    ],
    # +--+
    # |  |
    # +--+--+--+
    # |  |  |  |
    # +--+--+--+
    # |  |
    # +--+
    [ #6, 4 orientations
        [(0, 0), (1, 0), (1, 1), (1, 2), (2, 0)],
        [(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)],
        [(0, 2), (1, 0), (1, 1), (1, 2), (2, 2)],
        [(0, 1), (1, 1), (2, 0), (2, 1), (2, 2)],
    ],
    #    +--+--+
    #    |  |  |
    # +--+--+--+
    # |  |  |
    # +--+--+
    [ #7, 4 orientations
        [(0, 1), (0, 2), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (1, 1), (1, 2)],
        [(0, 0), (1, 0), (1, 1), (2, 1)],
        [(0, 1), (1, 0), (1, 1), (2, 0)],
    ],
    #    +--+--+
    #    |  |  |
    #    +--+--+
    #    |  |
    # +--+--+
    # |  |  |
    # +--+--+
    [ #8, 4 orientations
        [(0, 1), (0, 2), (1, 1), (2, 0), (2, 1)],
        [(0, 1), (0, 2), (1, 1), (2, 0), (2, 1)],
        [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)],
        [(0, 2), (1, 0), (1, 1), (1, 2), (2, 0)],
    ],
    # +--+--+
    # |  |  |
    # +--+--+--+
    # |  |  |  |
    # +--+--+--+
    [ #9, 8 orientations
        [(0, 0), (0, 1), (1, 0), (1, 1), (0, 2)],
        [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2)],
        [(0, 0), (0, 1), (1, 0), (1, 1), (2, 1)],
        [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)],
        [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2)],
        [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2)],
        [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1)],
        [(0, 1), (1, 0), (1, 1), (2, 0), (2, 1)],
    ],
    # +--+  +--+
    # |  |  |  |
    # +--+--+--+
    # |  |  |  |
    # +--+--+--+
    [ #10, 4 orientations
        [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)],
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)],
        [(0, 0), (0, 1), (1, 0), (2, 0), (2, 1)],
        [(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)],
    ],
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
