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
