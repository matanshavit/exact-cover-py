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
        "Thur": (7, 4),
        "Fri": (7, 5),
        "Sat": (7, 6),
    }


# the squares that need to be covered for a certain day
# defining the exact cover problem
def get_calendar_squares(month, date, day):
    return [
        square for
        key, square in EMPTY_CALENDAR_SQUARES.items()
        if key not in (month, date, day)
    ]
