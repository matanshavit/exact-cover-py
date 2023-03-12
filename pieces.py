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