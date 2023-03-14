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
