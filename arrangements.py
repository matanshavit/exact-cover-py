import random


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

            full_arrangements += _get_valid_arrangements(new_arrangement, next_possible_placements)
            if return_first and len(full_arrangements) > 0:
                return full_arrangements

        return full_arrangements

    possible_placement_indices = [
        list(range(len(possible_placement_indices)))
        for possible_placement_indices in compatible_indices
    ]
    return _get_valid_arrangements([], possible_placement_indices)
