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

# print(get_number_of_moves_to_win_count_map(8))
print(get_all_games_count(10))
result = 444356092776315
# result = 0
for k in m_to_win_4:
    # result += m_to_win_4[k] * (get_all_games_count(k - 1) - m_to_win_8.get(k - 1, 0))
    pass
print(result)


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
