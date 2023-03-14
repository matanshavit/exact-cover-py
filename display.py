def print_arrangement(arrangement):
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
