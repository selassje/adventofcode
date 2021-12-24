def roll_result(move):
    a = 1 + 3 * move
    return a + a + 1 + a + 2


def play(initial_position_player_1, initial_position_player_2):
    victorious_player = None
    move = 0
    positions_and_scores = [
        (initial_position_player_1, 0),
        (initial_position_player_2, 0),
    ]

    while victorious_player is None:
        for i in range(2):
            new_position = (
                (positions_and_scores[i][0] - 1 + roll_result(move)) % 10
            ) + 1
            move += 1
            new_score = positions_and_scores[i][1] + new_position
            positions_and_scores[i] = (new_position, new_score)
            if new_score >= 1000:
                victorious_player = i
                break

    loosing_player = (victorious_player + 1) % 2
    return positions_and_scores[loosing_player][1] * move * 3


assert play(4, 8) == 739785
print(play(6, 10))

three_rolls_sum_count = {}
for r1 in range(1, 4):
    for r2 in range(1, 4):
        for r3 in range(1, 4):
            s = r1 + r2 + r3
            three_rolls_sum_count[s] = three_rolls_sum_count.get(s, 0) + 1


def get_all_games_count(moves_count):
    return pow(27, moves_count)


def get_number_of_moves_to_win_count_map(initial_position):
    checked_comb = set()
    moves_to_wins_count = {}
    for k1, v1 in three_rolls_sum_count.items():
        for k2, v2 in three_rolls_sum_count.items():
            for k3, v3 in three_rolls_sum_count.items():
                for k4, v4 in three_rolls_sum_count.items():
                    for k5, v5 in three_rolls_sum_count.items():
                        for k6, v6 in three_rolls_sum_count.items():
                            for k7, v7 in three_rolls_sum_count.items():
                                for k8, v8 in three_rolls_sum_count.items():
                                    for k9, v9 in three_rolls_sum_count.items():
                                        for k10, v9 in three_rolls_sum_count.items():
                                            rolls = [
                                                k1,
                                                k2,
                                                k3,
                                                k4,
                                                k5,
                                                k6,
                                                k7,
                                                k8,
                                                k9,
                                                k10,
                                            ]
                                            score = 0
                                            moves = 0
                                            position = initial_position
                                            wins = 1
                                            while score < 21:
                                                position = (
                                                    (position - 1 + rolls[moves]) % 10
                                                ) + 1
                                                score += position
                                                wins *= three_rolls_sum_count[
                                                    rolls[moves]
                                                ]
                                                moves += 1
                                            h = hash(tuple(rolls[0:moves]))

                                            if h not in checked_comb:
                                                moves_to_wins_count[moves] = (
                                                    moves_to_wins_count.get(moves, 0)
                                                    + wins
                                                )
                                                checked_comb.add(h)

    return moves_to_wins_count


def get_number_of_moves_to_loose_count_map(initial_position):

    moves_to_loose_count = {}

    for k1, v1 in three_rolls_sum_count.items():
        position_1 = ((initial_position - 1 + k1) % 10) + 1
        score_1 = position_1
        if score_1 < 21:
            moves_to_loose_count[1] = moves_to_loose_count.get(1, 0) + v1
        for k2, v2 in three_rolls_sum_count.items():
            position_2 = ((position_1 - 1 + k2) % 10) + 1
            score_2 = score_1 + position_2
            if score_2 < 21:
                moves_to_loose_count[2] = moves_to_loose_count.get(2, 0) + v1 * v2
            for k3, v3 in three_rolls_sum_count.items():
                position_3 = ((position_2 - 1 + k3) % 10) + 1
                score_3 = score_2 + position_3
                if score_3 < 21:
                    moves_to_loose_count[3] = (
                        moves_to_loose_count.get(3, 0) + v1 * v2 * v3
                    )
                for k4, v4 in three_rolls_sum_count.items():
                    position_4 = ((position_3 - 1 + k4) % 10) + 1
                    score_4 = score_3 + position_4
                    if score_4 < 21:
                        moves_to_loose_count[4] = (
                            moves_to_loose_count.get(4, 0) + v1 * v2 * v3 * v4
                        )
                    for k5, v5 in three_rolls_sum_count.items():
                        position_5 = ((position_4 - 1 + k5) % 10) + 1
                        score_5 = score_4 + position_5
                        if score_5 < 21:
                            moves_to_loose_count[5] = (
                                moves_to_loose_count.get(5, 0) + v1 * v2 * v3 * v4 * v5
                            )
                        for k6, v6 in three_rolls_sum_count.items():
                            position_6 = ((position_5 - 1 + k6) % 10) + 1
                            score_6 = score_5 + position_6
                            if score_6 < 21:
                                moves_to_loose_count[6] = (
                                    moves_to_loose_count.get(6, 0)
                                    + v1 * v2 * v3 * v4 * v5 * v6
                                )
                            for k7, v7 in three_rolls_sum_count.items():
                                position_7 = ((position_6 - 1 + k7) % 10) + 1
                                score_7 = score_6 + position_7
                                if score_7 < 21:
                                    moves_to_loose_count[7] = (
                                        moves_to_loose_count.get(7, 0)
                                        + v1 * v2 * v3 * v4 * v5 * v6 * v7
                                    )
                                for k8, v8 in three_rolls_sum_count.items():
                                    position_8 = ((position_7 - 1 + k8) % 10) + 1
                                    score_8 = score_7 + position_8
                                    if score_8 < 21:
                                        moves_to_loose_count[8] = (
                                            moves_to_loose_count.get(8, 0)
                                            + v1 * v2 * v3 * v4 * v5 * v6 * v7 * v8
                                        )
                                    for k9, v9 in three_rolls_sum_count.items():
                                        position_9 = ((position_8 - 1 + k9) % 10) + 1
                                        score_9 = score_8 + position_9
                                        if score_9 < 21:
                                            moves_to_loose_count[9] = (
                                                moves_to_loose_count.get(9, 0)
                                                + v1
                                                * v2
                                                * v3
                                                * v4
                                                * v5
                                                * v6
                                                * v7
                                                * v8
                                                * v9
                                            )
                                        for k10, v10 in three_rolls_sum_count.items():
                                            position_10 = (
                                                (position_9 - 1 + k10) % 10
                                            ) + 1
                                            score_10 = score_9 + position_10
                                            if score_10 < 21:
                                                moves_to_loose_count[10] = (
                                                    moves_to_loose_count.get(10, 0)
                                                    + v1
                                                    * v2
                                                    * v3
                                                    * v4
                                                    * v5
                                                    * v6
                                                    * v7
                                                    * v8
                                                    * v9
                                                    * v10
                                                )

    return moves_to_loose_count


def solve(initial_position_player_1, initial_position_player_2):
    move_to_win_count = get_number_of_moves_to_win_count_map(initial_position_player_1)
    move_to_not_winning_count = get_number_of_moves_to_loose_count_map(
        initial_position_player_2
    )
    result = 0
    for m in move_to_win_count:
        result += move_to_win_count[m] * move_to_not_winning_count[m - 1]
    return result


print(solve(6, 10))
