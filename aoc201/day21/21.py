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
                                            moves_to_wins_count[moves] = (
                                                moves_to_wins_count.get(moves, 0) + wins
                                            )

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


m_to_win_6 = {
    4: 26822560212,
    5: 88587243178,
    6: 94929047696,
    3: 1445317965,
    7: 43424408482,
    8: 4771758131,
    9: 93570393,
    10: 90072,
}

m_to_win_8 = {
    4: 27139388969,
    6: 83018964028,
    7: 31874798949,
    8: 2796325042,
    5: 91570267187,
    9: 41517882,
    10: 32562,
    3: 1424729390,
}

m_to_win_4 = {
    4: 29358366758,
    3: 3794886144,
    5: 54109363378,
    6: 59798047876,
    7: 26751761239,
    8: 3046459262,
    9: 60751215,
    10: 53217,
}

m_to_loose_8 = {
    1: 27,
    2: 729,
    3: 17953,
    4: 254050,
    5: 1411009,
    6: 3520415,
    7: 2121762,
    8: 219716,
    9: 1206,
}


def solve(initial_position_player_1, initial_position_player_2):
    move_to_win_count = get_number_of_moves_to_win_count_map(initial_position_player_1)
    move_to_not_winning_count = get_number_of_moves_to_loose_count_map(
        initial_position_player_2
    )
    result = 0
    for m in move_to_win_count:
        result += move_to_win_count[m] * move_to_not_winning_count[m - 1]
    return result


print(solve(4, 8))
print(444356092776315)


def solve_2(initial_position_player_1, initial_position_player_2):
    class player_1_won(Exception):
        pass

    class player_2_won(Exception):
        pass

    class invalid_roll(Exception):
        pass

    three_rolls_sum_count = {}
    for r1 in range(1, 4):
        for r2 in range(1, 4):
            for r3 in range(1, 4):
                s = r1 + r2 + r3
                three_rolls_sum_count[s] = three_rolls_sum_count.get(s, 0) + 1

    all_combinations_count = pow(2, 42)
    print(all_combinations_count)
    bit_mask = 0b111
    player_1_wins = 0
    for combination in range(all_combinations_count):
        try:
            count_per_combination = 1
            positions_and_scores = [
                (initial_position_player_1, 0),
                (initial_position_player_2, 0),
            ]
            bit_shift = 0
            while True:
                for i in range(2):
                    three_rolls_sum = (
                        combination & (bit_mask << bit_shift)
                    ) >> bit_shift

                    if three_rolls_sum == 7:
                        raise invalid_roll

                    three_rolls_sum += 3
                    bit_shift += 3

                    new_position = (
                        (positions_and_scores[i][0] - 1 + three_rolls_sum) % 10
                    ) + 1
                    new_score = positions_and_scores[i][1] + new_position

                    if new_score >= 21 and i == 0:
                        raise player_1_won
                    if new_score >= 21 and i == 1:
                        raise player_2_won

                    positions_and_scores[i] = (new_position, new_score)
                    count_per_combination *= three_rolls_sum_count[three_rolls_sum]
        except player_1_won:
            if combination % 10000000 == 0:
                print("here")
            player_1_wins += count_per_combination
        except player_2_won:
            pass
        except invalid_roll:
            pass
    return player_1_wins


# print(solve_2(4, 8))
