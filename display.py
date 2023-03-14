def print_arrangement_old(arrangement):
    horizontal = [
        [False] * 7
        for _ in range(9)
    ]
    vertical = [
        [False] * 8
        for _ in range(8)
    ]
    for piece in arrangement:
        for space in piece:
            if (space[0] - 1, space[1]) not in piece:
                horizontal[space[0]][space[1]] = True
            if (space[0] + 1, space[1]) not in piece:
                horizontal[space[0] + 1][space[1]] = True
            if (space[0], space[1] - 1) not in piece:
                vertical[space[0]][space[1]] = True
            if (space[0], space[1] + 1) not in piece:
                vertical[space[0]][space[1] + 1] = True

    arrangement_string = ""
    for row in range(8):
        horizontal_string = "" 
        for column in range(7):
            horizontal_string += " "
            horizontal_string += "---" if horizontal[row][column] else "   "
        vertical_string = ""
        for column in range(8):
            vertical_string += "|" if vertical[row][column] else " "
            vertical_string += "   "
        arrangement_string += horizontal_string + "\n" + vertical_string + "\n"
    horizontal_string = ""
    for column in range(7):
        horizontal_string += " "
        horizontal_string += "---" if horizontal[8][column] else "   "
    arrangement_string += horizontal_string
    print(arrangement_string)


def _symbol_directions(arrangement):
    symbol_directions = [
        [
            {
                "left": False,
                "right": False,
                "up": False,
                "down": False,
            }
            for _ in range(7 + 8)
        ]
        for _ in range(9)
    ]

    for piece in arrangement:
        for space in piece:
            if (space[0] - 1, space[1]) not in piece:
                symbol_directions[space[0]][space[1] * 2]["right"] = True
                symbol_directions[space[0]][space[1] * 2 + 1]["left"] = True
                symbol_directions[space[0]][space[1] * 2 + 1]["right"] = True
                symbol_directions[space[0]][space[1] * 2 + 2]["left"] = True
            if (space[0] + 1, space[1]) not in piece:
                symbol_directions[space[0] + 1][space[1] * 2]["right"] = True
                symbol_directions[space[0] + 1][space[1] * 2 + 1]["left"] = True
                symbol_directions[space[0] + 1][space[1] * 2 + 1]["right"] = True
                symbol_directions[space[0] + 1][space[1] * 2 + 2]["left"] = True
            if (space[0], space[1] - 1) not in piece:
                symbol_directions[space[0]][space[1] * 2]["down"] = True
                symbol_directions[space[0] + 1][space[1] * 2]["up"] = True
            if (space[0], space[1] + 1) not in piece:
                symbol_directions[space[0]][space[1] * 2 + 2]["down"] = True
                symbol_directions[space[0] + 1][space[1] * 2 + 2]["up"] = True

    return symbol_directions


SYMBOLS = [
    " ", # blank space
    "╵", # up,
    "╶", # right
    "└", # up right
    "╷", # down
    "│", # up down
    "┌", # right down
    "├", # up right down
    "╴", # left
    "┘", # up left
    "─", # right left
    "┴", # up right left
    "┐", # down left
    "┤", # up down left
    "┬", # right down left
    "┼", # up right down left
]


def _symbol_for_directions(symbol_directions_dict):
    if symbol_directions_dict["left"]:
        if symbol_directions_dict["down"]:
            if symbol_directions_dict["right"]:
                if symbol_directions_dict["up"]:
                    return SYMBOLS[15]
                else:
                    return SYMBOLS[14]
            else:
                if symbol_directions_dict["up"]:
                    return SYMBOLS[13]
                else:
                    return SYMBOLS[12]
        else:
            if symbol_directions_dict["right"]:
                if symbol_directions_dict["up"]:
                    return SYMBOLS[11]
                else:
                    return SYMBOLS[10]
            else:
                if symbol_directions_dict["up"]:
                    return SYMBOLS[9]
                else:
                    return SYMBOLS[8]
    else:
        if symbol_directions_dict["down"]:
            if symbol_directions_dict["right"]:
                if symbol_directions_dict["up"]:
                    return SYMBOLS[7]
                else:
                    return SYMBOLS[6]
            else:
                if symbol_directions_dict["up"]:
                    return SYMBOLS[5]
                else:
                    return SYMBOLS[4]
        else:
            if symbol_directions_dict["right"]:
                if symbol_directions_dict["up"]:
                    return SYMBOLS[3]
                else:
                    return SYMBOLS[2]
            else:
                if symbol_directions_dict["up"]:
                    return SYMBOLS[1]
                else:
                    return SYMBOLS[0]


def arrangement_string(arrangement):
    symbol_directions = _symbol_directions(arrangement)
    return "\n".join(
        "".join(
            _symbol_for_directions(symbol_dict)
            for symbol_dict in row
        ) for row in symbol_directions
    )


def print_arrangement(arrangement):
    print(arrangement_string(arrangement))
